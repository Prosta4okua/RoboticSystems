#!/usr/bin/python3
import rospy
from tutorials.srv import multiplier, multiplierResponse

serviceName = "multiplier"

def multuplier_client(x, y):
    rospy.init_node("client_service_node")
    rospy.wait_for_service(serviceName)
    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        try:
            multiply_two_ints = rospy.ServiceProxy(serviceName, multiplier)
            response = multiply_two_ints(x, y)
            rospy.loginfo(response.result)
            rate.sleep()
        except rospy.ServiceException as e:
            print("Service call failed %s", e)

if  __name__ == '__main__':
    multuplier_client(7, 2)
