#!/usr/bin/env PYTHONIOENCODING="utf-8" python
import tflearn
import os
import speech_data as data

# training and testing data sets
train_data = '/home/cc/Data/small-clean-train/'
test_data = '/home/cc/Data/small-clean-test/'

# grab the speakers from the training directory
speakers = data.get_speakers(train_data)
number_classes = len(speakers)

# create the MFCC arrays from the data for training
batch=data.wave_batch_generator(batch_size=1000,source=WORD_WAVs,target=data.Target.speaker,speakers=speakers)
X,Y=next(batch)


# Classification
tflearn.init_graph(num_cores=8, gpu_memory_fraction=0.5)

net = tflearn.input_data(shape=[None, 8192]) #Two wave chunks
net = tflearn.fully_connected(net, 64)
# seems like a higher dropout rate works better -- why is this??
net = tflearn.dropout(net, 0.5)
net = tflearn.fully_connected(net, number_classes, activation='softmax')
net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy')

model = tflearn.DNN(net)
model.fit(X, Y, n_epoch=100, show_metric=True, snapshot_step=100)

# need to make a better testing set!!
test_speakers = data.get_speakers('/home/cc/Data/all_test/')
number_test_classes = len(test_speakers)
test_batch = data.wave_batch_generator(batch_size=1000, source=WORD_WAVs, target=data.Target.speaker, speakers=test_speakers)
X_test, Y_test = next(test_batch)
predict = model.predict(X_test)
for pred in predict:
	print(pred)
for x,y in zip(X_test,Y_test):
	print(x,y)
