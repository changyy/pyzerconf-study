from Zeroconf import *
import socket
import signal
import sys

class MyListener(object):
	def __init__(self, zeroconf):
		self.zeroconf = zeroconf
		pass

	def removeService(self, zeroconf, type, name, record):
		print "Service", str(name), "removed"

	def addService(self, zeroconf, type, name, record):
		print "Name ["+str(name)+"] added"
		print "Type ["+str(type)+"]"
		print "Record:", record
		print "service:", zeroconf.services
		#print "Address is", str(socket.inet_ntoa(info.getAddress()))
		#print "Port is", info.getPort()
		#print "Weight is", info.getWeight()
		#print "Priority is", info.getPriority()
		#print "Server is", info.getServer()
		#print "Text is", info.getText()
		#print "Properties are", info.getProperties()

r = Zeroconf()
def signal_handler(signal, frame):
	print "press ctrl+c"
	r.close()
        sys.exit(0)

if __name__ == '__main__':	
	print "Multicast DNS Service Discovery for Python Browser test"
	listener = MyListener(r)
	print "1. Testing browsing for a service..."
	type = "_aireplay._tcp.local."
	type = "_changyytcp._tcp.local."
	browser = ServiceBrowser(r, type, listener)

	#print Zeroconf().getServiceInfo("_changyytcp._tcp.local.","device1._changyytcp._tcp.local.",10000)

	signal.signal(signal.SIGINT, signal_handler)
	signal.pause()
