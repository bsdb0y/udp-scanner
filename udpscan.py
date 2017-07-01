import socket
import sys
import subprocess
#import pybangrab

def getServiceName(port, proto):
    """ Check and Get service name from port and proto string combination using socket.getservbyport

    @param port string or id
    @param protocol string
    @return Service name if port and protocol are valid, else None
    """

    try:
        name = socket.getservbyport(int(port), proto)
    except:
        return None
    return name



#print("UDP CALLED") Uncomment for debugging purpose
UDP_IP = sys.argv[1]
#scan_id = sys.argv[4]
for RPORT in range(int(sys.argv[2]),int(sys.argv[3])):
#RPORT = 68
	MESSAGE = "ping"

#	print("UDP target IP: ", UDP_IP)
#print("UDP target port: ", RPORT)
#print("message going to send: ", MESSAGE)

	client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM,socket.IPPROTO_UDP)

	if client == -1:
		print("udp socket creation failed")

	sock1 = socket.socket(socket.AF_INET,socket.SOCK_RAW,socket.IPPROTO_ICMP)
	if sock1 == -1:
		print("icmp socket creation failed")
#i=1
	try:
		client.sendto(MESSAGE.encode('utf_8'),(UDP_IP, RPORT))
        	#print("sending message: ", MESSAGE)
        	#client.settimeout(0.5)
		sock1.settimeout(1)

		data , addr = sock1.recvfrom(1024)
        	#print(RPORT,' ','closed')
        	#print("received at: " , addr )

	except socket.timeout:
		#print(RPORT,' ','open')
		serv = getServiceName(RPORT,'udp')
		if not serv:
			pass
		else:
			print(RPORT,serv)
			#result = pybangrab.banner(UDP_IP,RPORT)
			#print(result)
			
			client.close()
			sock1.close()
