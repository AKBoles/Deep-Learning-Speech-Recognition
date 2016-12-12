import os

os.chdir('/home/cc/working/data/')
files = os.listdir(os.getcwd())
c = 0
while c < 50:
  os.system('cp train100clean/Speaker' + str(c) + '* /home/cc/working/data/devclean3/')
  c = c + 1
