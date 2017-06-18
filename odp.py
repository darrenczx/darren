#!/usr/bin/env python
#encoding=utf-8
import thread
import socket
obj = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
def khi(id):
	while True:
		a=raw_input()
		obj.sendto(a,('127.0.0.1',5050))
	obj.close()
def kho(id):
	while True:
		ret = str(obj.recv(1024))
	
		print(ret)
	obj.close()
try:
	thread.start_new_thread(khi,(1,))
	thread.start_new_thread(kho,(3,))
except:
	print"Error: unable to start thread"
while 1:
	pass
