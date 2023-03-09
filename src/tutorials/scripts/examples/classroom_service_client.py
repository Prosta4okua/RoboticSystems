#!/usr/bin/python

import rospy
# Import the service message used by the service /trajectory_by_name
from simple_rosservise.srv import MySrvType, MySrvTypeRequest
import sys

# Initialise a ROS node with the name service_client
rospy.init_node('service_client')

# Wait for the service client /trajectory_by_name to be running
rospy.wait_for_service('/my_service')

# Create the connection to the service
first_service = rospy.ServiceProxy('/my_service', MySrvType)

# Create an object of type TrajByNameRequest
my_request_object = MySrvTypeRequest()

# Fill the variable traj_name of this object with the desired value
my_request_object.msg_data = "Yeah, I`ve did it"

# Send through the connection the name of the trajectory to be executed by the robot
result = first_service(my_request_object)

# Print the result given by the service called
print(result)
