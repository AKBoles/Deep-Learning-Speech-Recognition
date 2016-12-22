import os
import sys

dest = sys.argv[1]
os.chdir(dest)
print('new directory: %s' %os.getcwd())
for f in os.listdir(os.getcwd()):
	if os.path.isdir(f):
		print('entering %s' %f)
		os.chdir(dest + f)
		for f2 in os.listdir(os.getcwd()):
			if os.path.isdir(f2):
				print('entering %s' %f2)
				os.chdir(os.getcwd() + '/' + f2)
				os.system('track2track -t wav *.flac')
				os.chdir(dest + f)
				break
			else:
				print('error %s is not a directory' %f2)
		os.chdir(dest)
		break
	else:
		print('file %s is not a directory' %f)
