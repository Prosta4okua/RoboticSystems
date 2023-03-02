#!/usr/bin/python3
import rospy
# from std_msgs.msg import Int32
from geometry_msgs.msg import Twist
#import random
# \\wsl.localhost\Ubuntu-20.04\home\nalitnyk\python_catkin/src/tutorials/launch/start.launch
rospy.init_node("forward")
print("node init")
rate = rospy.Rate(60)
pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
twist = Twist()

# for i in range(5):
#     twist.linear.z = 4
#     pub.publish(twist)
#     rate.sleep()
# twist.linear.z = 0
while not rospy.is_shutdown():
    print("it's working")
    # Створіть:

    # Створюємо змінну:

    twist.linear.x = 1.0
    twist.linear.y = 1.0

    twist.angular.z = 1.0
    twist.linear.z = 1.0
    pub.publish(twist)
    print(twist.angular)
    rate.sleep()  # sleep to maintain rate above 2Hz
