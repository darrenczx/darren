#!/usr/bin/env python
#encoding=UTF8
import thread

import socket
sk=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sk.bind(("127.0.0.1",5050))
addr_tmp=[]
def fui(id):
	while True:
   		data,addr = sk.recvfrom(1024)
    		addr_tmp.append(addr[0])
		addr_tmp.append(addr[1])
                print "received from %s: %s"%addr,data
    		print(data)
	sk.close()
def fuo(id):
	while True:
    		a=raw_input()
    		sk.sendto(a,(addr_tmp[0],addr_tmp[1]))
	sk.close()
try:
	thread.start_new_thread(fui,(2,))
	thread.start_new_thread(fuo,(4,))
except:
	print"Error: unable to start thread"

while 1:
	pass


