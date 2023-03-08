#!/usr/bin/python3
import rospy
# you import the service message python classes generated from Empty.srv.
from simple_rosservise.srv import MySrvType, MySrvTypeResponse


def my_callback(request):
    print(request.msg_data)
    my_response = MySrvTypeResponse()
    my_response = 3
    return my_response  # the service Response class, in this case EmptyResponse
    # return MyServiceResponse(len(request.words.split()))


rospy.init_node('service_server')
# create the Service called my_service with the defined callback
my_service = rospy.Service('/my_service', MySrvType, my_callback)
rospy.spin()  # maintain the service open.
