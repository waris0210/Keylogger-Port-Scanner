#!/bin/python3
import platform
import pyfiglet
import sys
import socket
import nmap
from datetime import datetime
import time
nm = nmap.PortScanner()

a_b = pyfiglet.figlet_format("PORT SCANNER")
print("-" * 50)
print(a_b)

#defining our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1])		#Translating hostname to Ipv4.
else:
	print("Invalid amount of argumnets\n")
	print("Syntax : python3 <filename>.py <target_ip>")

#adding a banner
start_time = datetime.now()
print("-" * 50)
print("Scanning target {}".format(target))
print("Time : " + str(datetime.now()))
print("-" * 50)

#Creating the list to save ports that are open to show as a last statement.
op = [] 

try:
	for port in range(0,1025):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		#print("checking port {}".format(port))
		if result == 0:
		#print("checking port {}".format(port))
			print("Port {} is open.".format(port))
			op.append(port)

		s.close()

except KeyboardInterrupt:
	print("\n ***** Exiting process. *****\n")
	sys.exit()

except socket.gaierror:
	print("Hostname couldn't be resolved.\n")
	print("\n ***** Exiting process. *****\n")
	sys.exit()

except socket.error:
	print("Couldn't connect to the server.\n")
	print("\n ***** Exiting process. *****\n")
	sys.exit()

#Showing all the open ports 
print("Open ports are : ", op)

#For getting system info
print("Scanning for OS detection.")
machine = nm.scan(target, arguments='-O')
print(machine['scan'][target]['osmatch'][0]['osclass'][0]['osfamily']) 

#Calculating Time
t_d = datetime.now() - start_time
print("wohoooo, Scan Complete...................")
print("Time taken is -> {}".format(t_d))




'''import time 
import sys


ani = ["/", "^", "-", "#", "*", "+", "$", "@", "<"]
i = 0

while :
        time.sleep(0.3)
        sys.stdout.write("\rLoading" + ani[i % len(ani)])
        sys.stdout.flush
        i += 1
print("\n")'''
