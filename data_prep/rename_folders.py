import os
import sys

# this script will move all folders in input directory to another location
original = sys.argv[1]
dest = sys.argv[2]

# also rename all folders to: Speaker#
speak = 'Speaker'

os.chdir(original)
print('New directory: %s' %(os.getcwd()))
c = 0
for f in os.listdir(os.getcwd()):
	if os.path.isdir(f):
		# this is a directory! need to rename
		os.rename(f, speak + str(c))
		c = c + 1
	else:
		print('Error, %s is not a directory.' %f)
