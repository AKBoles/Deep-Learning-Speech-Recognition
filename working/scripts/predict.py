import os
import librosa
import tflearn
import speech_data
from pydub import AudioSegment as audio

speakers = speech_data.get_speakers('/home/cc/working/data/devclean_seg/')
net = tflearn.input_data(shape=[None, 13, 44])
net = tflearn.fully_connected(net, 64)
net = tflearn.dropout(net, 0.5)
net = tflearn.fully_connected(net, len(speakers), activation='softmax')
net = tflearn.regression(net, optimizer='adam', loss='categorical_crossentropy')
model = tflearn.DNN(net, tensorboard_verbose=3)
model.load('/home/cc/working/models/devclean/devclean_train.tflearn')
os.chdir('/home/cc/working/data/devclean_test/')
test = []
for f1 in os.listdir(os.getcwd()):
  y, sr = librosa.load(f1)
  test.append(librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13))
result=model.predict(test)
c = 0
for f,r in zip(os.listdir(os.getcwd()), result):
  res = speech_data.one_hot_to_item(r, speakers)
  if res in f:
    c = c + 1
print('correct: %s ; total: %s' %(str(c), str(len(test))))
