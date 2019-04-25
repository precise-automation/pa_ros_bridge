#!/usr/bin/env python

import rospy
import time
import telnetlib

from TCSClient import TCSClient

from pa_tcs_bridge.srv import TCSService, TCSServiceResponse


# Default values (overridden if launch file used)
HOST = "192.168.0.1"
PORT = "10100"

class Setup:

	tcs_client = None

	# INITIALIZE

	def run(self):

		# Get IP and port from parameters
		if rospy.has_param("TCS_IP"):
			HOST = rospy.get_param("TCS_IP")
		if rospy.has_param("TCS_PORT"):
			PORT = rospy.get_param("TCS_PORT")


		# Initialize ROS Node
		rospy.loginfo("initializing nodes")
		rospy.init_node("TCS", anonymous=False)

		# Initialize ROS Service
		rospy.loginfo("Connecting to port " + str(PORT) + "...")
		rospy.Service("TCS/CommandService", TCSService, self.CommandHandler)
		rospy.loginfo("Connected.")
		rospy.loginfo("Ready for commands.")

		# Start Telnet connection and initialize TCS
		self.tcs_client = TCSClient(HOST, PORT)

		# Keep alive
		rospy.spin()



	# HANDLER

	def CommandHandler(self, command):
		rospy.loginfo("Sending command: " + command.input)
		response = self.tcs_client.SendCommand(command.input)
		rospy.loginfo("Received response: " + response.output)
		return response


if __name__ == "__main__":
	Setup().run()