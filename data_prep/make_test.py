import os
from pydub import AudioSegment as audio
import random

os.chdir('/home/cc/working/data/train100clean_seg/')
data = '/home/cc/working/data/train100clean_test/'

files = os.listdir(os.getcwd())
c = 0
random.shuffle(files)
for f in files:
	if  c < 4000:
		os.system('mv ' + f + ' ' + data + f)
	c = c + 1
