#!/usr/bin/python3
import rospy
from tutorials.srv import multiplier, multiplierResponse


def multiply():
    rospy.init_node("multiplier_service")
    service = rospy.Service("multiplier", multiplier, callback)
    rospy.spin()

def callback(request):
    return multiplierResponse(request.a * request.b)

if __name__ == '__main__':
    multiply()
