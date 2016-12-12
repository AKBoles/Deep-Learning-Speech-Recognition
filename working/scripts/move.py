import os 
import speech_data

data = '/home/cc/working/data/devclean/'
new_data = '/home/cc/working/data/devclean_mfccs/'
os.chdir(data)
files = os.listdir(data)
back = []
c = 0
for f in files:
  if 'Speaker' in f: continue
  back.append(f)
print(len(back))
for b in back:
  os.system('cp ' + b + ' ' + new_data + speech_data.speaker(f) + '_back' + str(c) + '.wav')
  c = c + 1
