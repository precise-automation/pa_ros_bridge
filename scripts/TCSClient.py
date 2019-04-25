#!/usr/bin/env python

import rospy
import telnetlib
import threading
import time
import math

from pa_tcs_bridge.srv import TCSService, TCSServiceResponse

class TCSClient:

	commandLock = threading.Lock()

	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.connection = None
		self.Connect()
		self.InitConnectionMode()

	def Connect(self):
		self.connection = telnetlib.Telnet(self.host, self.port)

	def Disconnect(self):
		self.connection.close()

	def InitConnectionMode(self):
		self.commandLock.acquire()
		try:	
			if not self.connection:
				self.Connect()

			# Set TCS to machine-readable form
			self.connection.write("mode 0\n")
			self.connection.read_until("\n")
			self.connection.write("selectrobot 1\n")
			self.connection.read_until("\n")

		finally:
			self.commandLock.release()

	def SendCommand(self, command):
		self.commandLock.acquire()
		try:
			if not self.connection:
				self.Connect()
			self.connection.write(command + "\n")
			line = self.connection.read_until("\n").rstrip()
			return TCSServiceResponse(line)

		finally:
			self.commandLock.release()