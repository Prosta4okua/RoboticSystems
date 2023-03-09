#!/usr/bin/python3
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
import sys,tty,os,termios,time
# import tkinter as tk
class GUI:

    def __init__(self) -> None:
        # creating toplevel widget
        self.master = Tk()
        self.master.title = "Керування дроном 'Гектор'"

        # creating frame
        self.frame1 = Frame(self.master)
        self.frame1.pack(expand=True, fill=BOTH)

        # creating buttons
        button1 = Button(self.frame1, text="Уперед")
        button1.grid(row=0, column=1)
        button2 = Button(self.frame1, text="Назад")
        button2.grid(row=2, column=1)
        button3 = Button(self.frame1, text="Ліворуч")
        button3.grid(row=1, column=0)
        button4 = Button(self.frame1, text="Праворуч")
        button4.grid(row=1, column=2)

        # binding buttons
        self.master.bind_all("w", move_forward)
        self.master.bind_all("s", move_back)
        self.master.bind_all("a", move_left)
        self.master.bind_all("d", move_right)
        button1.bind("<Button-1>", move_back)
        button2.bind("<Button-1>", move_forward)
        button3.bind("<Button-1>", move_left)
        button4.bind("<Button-1>", move_right)

        # launching event loop
        self.master.mainloop()





        # rospy.init_node("Subscriber_Node", anonymous = True)

        # rospy.Subscriber("/ground_truth/state", Odometry , self.callback)
        # rospy.spin()

# Створюємо сервіс, що отримує від клієнта напрямок руху, що відповідає напрямку (ліво, право, прямо, вверх). Сервіс відправляє гектору команду рухатися в той напрямок, але через 1 секунду зупиняє його. У якості відповіді пише клієнту, що все ок


def move_forward(twist):
    print("move forward")
    twist.linear.x += 1.0
    return twist

def move_back(twist):
    print("move back")
    twist.linear.x -= 1.0
    return twist


def move_left(twist):
    twist.linear.y -= 1.0
    print("move left")
    return twist

def move_right(twist):
    print("move right")
    twist.linear.y += 1.0
    return twist

def move_up(twist):
    print("move_up")
    twist.linear.z += 1.0
    return twist

def move_down(twist):
    print("move_down")
    twist.linear.z -= 1.0
    return twist

def reset_any_move(twist):
    print("resetting any move...")
    return Twist()


def print_twist(twist):
    str = f"Linear: [{twist.linear.x}|{twist.linear.y}|{twist.linear.z}] Angular: [{twist.angular.x}|{twist.angular.y}|{twist.angular.z}]"
    print (str)





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
        while True:
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

    def callback(self, data):
        rospy.loginfo("[RECEIVED DATA] %s [%f:%f]", data.message, data.x, data.y)

    def listener(self):
        rospy.init_node("danylo_controlling_node", anonymous = True)
        print("node init")
        rate = rospy.Rate(60)
        pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)

        while not rospy.is_shutdown():
            print("it's working")
            twist = Twist()
            twist = self.movement_handler(keyboard_check(), twist)
            pub.publish(twist)

            time.sleep(1)
            pub.publish(reset_any_move(twist))

            # sleep to maintain rate above 2Hz
            # rate.sleep()

    def movement_handler(self, key, twist):
        if key == 'w':
            move_forward(twist)
        elif key == 's':
            move_back(twist)
        elif key == "a":
            move_left(twist)
        elif key == "d":
            move_right(twist)
        elif key == "up":
            move_up(twist)
        elif key == "down":
            move_down(twist)
        elif key == "r":
            reset_any_move(twist)

        print_twist(twist)

        return twist


if __name__ == "__main__":
    # gui = GUI()
    robot = Robot()
