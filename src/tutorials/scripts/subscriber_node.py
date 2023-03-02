#!/usr/bin/python3
import rospy
# from std_msgs.msg import String
from tutorials.msg import Danylo

def callback(data):
    rospy.loginfo("[RECEIVED DATA] %s [%f:%f]", data.message, data.x, data.y)


def listener():
    rospy.init_node("Subscriber_Node", anonymous = True)
    rospy.Subscriber("talking_topic", Danylo, callback)
    # run node continuosly
    rospy.spin()


if __name__ == '__main__':
    try:
        print("Subscriber works!!!")
        listener()
    except rospy.ROSInterruptException:
        pass

# rosrun tutorials subscriber_node.py
