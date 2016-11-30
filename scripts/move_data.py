import os
import sys

orig = sys.argv[1]
dest = sys.argv[2]
os.chdir(orig)
for f in os.listdir(os.getcwd()):
	if os.path.isdir(f):
		os.chdir(orig + f)
		for f2 in os.listdir(os.getcwd()):
			if os.path.isfile(f2):
				os.system('cp ' + f2 + ' ' + dest + f2)
			else:
				print('error moving %s' %f2)
		os.chdir(orig)
	else:
		print('file %s is not a directory' %f)
