#!/usr/bin/env PYTHONIOENCODING="utf-8" python
import tflearn
import os
import sys
import librosa
import speech_data as data

# training and testing data sets
train_data = sys.argv[1]
test_data = sys.argv[2]

# grab the speakers from the training directory
speakers = data.get_speakers(train_data)
number_classes = len(speakers)

# create the MFCC arrays from the data for training
audio_files = os.listdir(train_data)
X = []
Y = []
for f in audio_files:
    Y.append(data.one_hot_from_item(data.speaker(f), speakers))
    y, sr = librosa.load(train_data + f)
    X.append(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13))

# define the network and the model
tflearn.init_graph(num_cores=8, gpu_memory_fraction=0.5)

net = tflearn.input_data(shape=[None, 13, 44]) 
net = tflearn.fully_connected(net, 64)
net = tflearn.dropout(net, 0.5)
net = tflearn.fully_connected(net, number_classes, activation='softmax')
net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy')

model = tflearn.DNN(net)
model.fit(X, Y, n_epoch=2000, show_metric=True, snapshot_step=100)

# test the model using the testing directory
test = []
for f1 in os.listdir(test_data):
    y, sr = librosa.load(test_data + f1)
    test.append(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13))
result = model.predict(test)
c = 0
for f,r in zip(os.listdir(test_data), result):
    res = data.one_hot_to_item(r, speakers)
    if res in f:
      c = c + 1
acc = float(c) / float(len(test))
print('Test set accuracy: %s' %str(acc))
