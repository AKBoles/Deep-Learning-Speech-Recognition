import os
import sys
import shutil

dest = sys.argv[1]
os.chdir(dest)

for f in os.listdir(os.getcwd()):
	if os.path.isdir(f):
		os.chdir(dest + f)
		for f2 in os.listdir(os.getcwd()):
			if os.path.isdir(f2):
				print('deleting: %s' %f2)
				shutil.rmtree(os.getcwd() + '/' + f2)			
			if '.txt' in f2:
				print('deleting: %s' %f2)
				os.remove(f2)
			if '.wav' in f2:
				print('deleting: %s' %f2)
				os.remove(f2)
		os.chdir(dest)
