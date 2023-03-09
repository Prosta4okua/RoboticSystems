#!/usr/bin/python3

# Завдання:
#     Створюємо сервіс, що отримує від клієнта напрямок руху, що відповідає напрямку (ліво, право, прямо, вверх). Сервіс відправляє гектору команду рухатися в той напрямок, але через 1 секунду зупиняє його. У якості відповіді пише клієнту, що все ок

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import sys,tty,os,termios,time
from tutorials.srv import move_key, move_keyResponse

# Створюємо сервіс, що отримує від клієнта напрямок руху, що відповідає напрямку (ліво, право, прямо, вверх). Сервіс відправляє гектору команду рухатися в той напрямок, але через 1 секунду зупиняє його. У якості відповіді пише клієнту, що все ок
# Клієнт приймає натиснену клавішу і надсилає сервісу
# Сервіс через паблішера робить рух і відправляє респонс клієнту, що все ОК
service_name = "aservice"

def getkey():
    old_settings = termios.tcgetattr(sys.stdin)
    tty.setcbreak(sys.stdin.fileno())
    try:
        while True:
            b = os.read(sys.stdin.fileno(), 3).decode()
            if len(b) == 3:
                k = ord(b[2])
            else:
                k = ord(b)
            key_mapping = {
                127: 'backspace',
                10: 'return',
                32: 'space',
                9: 'tab',
                27: 'esc',
                65: 'up',
                66: 'down',
                67: 'right',
                68: 'left'
            }
            return key_mapping.get(k, chr(k))
    finally:
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)

def keyboard_check():
    try:
        # while True:
        k = getkey()
        if k == 'esc':
            quit()
        else:
            return k
    except (KeyboardInterrupt, SystemExit):
        os.system('stty sane')
        print('stopping.')

class Robot:
    def __init__(self) -> None:
        self.listener()

    # def callback(self, data):
    #     rospy.loginfo("[RECEIVED DATA] %s [%f:%f]", data.res)

    def listener(self):
        # ініціалізація ноди
        rospy.init_node("lab4_client_service_node", anonymous = True)
        print("lab4_client_service_node was initialised")
        rospy.wait_for_service(service_name)
        rate = rospy.Rate(1)

        while not rospy.is_shutdown():
            try:
                get_message = rospy.ServiceProxy(service_name, move_key)
                key = keyboard_check()
                print("You've printed", key)
                response = get_message(key)
                rospy.loginfo(response.res)
                # rate.sleep()
            except rospy.ServiceException as e:
                print("Service call failed %s", e)

if __name__ == "__main__":
    robot = Robot()
