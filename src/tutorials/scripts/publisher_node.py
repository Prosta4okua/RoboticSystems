#!/usr/bin/python3

import rospy
from std_msgs.msg import String
from tutorials.msg import Danylo
import random

def talk_to_me():
    pub = rospy.Publisher("talking_topic", Danylo, queue_size=10)
    rospy.init_node("publisher_node", anonymous=True)
    rate = rospy.Rate(1)
    rospy.loginfo("Publisher Node Started, now publishing messages...")
    while not rospy.is_shutdown():
        # msg = "Hello Danylo - %s" % rospy.get_time()
        msg = Danylo()
        msg.message = "My Position is: "
        msg.x = random.random()
        msg.y = random.random()
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        print("Wow!!!")
        talk_to_me()
    except rospy.ROSInterruptException:
        pass

# before run:
# roscore

# to run:
# rosrun tutorials publisher_node.py

# to view topic lists
# rostopic list

# to print what topic list says:
# rostopic echo /talking_topic

# build
# catkin_make
# in python_catkin:
# source devel/setup.bash
