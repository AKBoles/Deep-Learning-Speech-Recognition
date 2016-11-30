import os
import sys

# change directory to first argument
original_dir = os.getcwd()
data_dir = sys.argv[1]
os.chdir(data_dir)
print('Input data directory: %s' %data_dir)

# change each Speaker's flac file to flac#.flac
for f1 in os.listdir(os.getcwd()):
	os.chdir(data_dir + f1)
	c = 0
	for f2 in os.listdir(os.getcwd()):
		if os.path.isdir(f2):
			os.chdir(os.getcwd() + '/' + f2)
			for f3 in os.listdir(os.getcwd()):
				print(f3)
				if '.flac' in f3:
					os.system('mv * ../')
			os.chdir(data_dir + f1)
