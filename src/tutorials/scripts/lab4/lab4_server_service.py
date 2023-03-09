#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist
from tutorials.srv import move_key, move_keyResponse
import time

service_name = "aservice"

# Створюємо сервіс, що отримує від клієнта напрямок руху, що відповідає напрямку (ліво, право, прямо, вверх). Сервіс відправляє гектору команду рухатися в той напрямок, але через 1 секунду зупиняє його. У якості відповіді пише клієнту, що все ок
# Клієнт приймає натиснену клавішу і надсилає сервісу
# Сервіс через паблішера робить рух і відправляє респонс клієнту, що все ОК


class MyService:
    def __init__(self) -> None:
        # ініціалузаємо ноду
        rospy.init_node("lab4_server_service_node")
        rate = rospy.Rate(60)
        print("lab4_server_service_node was initialised")

        # ініціалізуємо сервіс
        self.service_init()

        # ініціалізуємо клас руху
        self.movement = Movement()

        # ініціалізуємо паблішера
        # self.publisher_init()


    def service_init(self):
        self.service = rospy.Service("aservice", move_key, self.callback)
        rospy.spin()


    # def publisher_init(self):
        # self.publisher = rospy.Publisher("/cmd_vel", Twist, queue_size=1)


    def callback(self, request):
        print(request)
        # publisher = rospy.Publisher("/cmd_vel", move_key, queue_size=1)
        key = request.key
        twist = Twist()
        # twist = Movement.movement_handler(key, twist)
        twist = Movement.movement_handler(key, twist)
        Movement.print_twist(twist)
        publisher = MyPublisher()
        publisher.publish(twist)
        time.sleep(1)
        twist = Movement.reset_any_move(twist)
        publisher.publish(twist)
        msg = "OK"
        return move_keyResponse(msg)


class MyPublisher:
    def __init__(self) -> None:
        self.publisher = rospy.Publisher("/cmd_vel", move_key, queue_size=2)
        rospy.init_node("publisher_node", anonymous=True)
        # self.rate = rospy.Rate(1)
    def publish(self, twist):
        while not rospy.is_shutdown():
            self.publisher.publish(twist)


class Movement:
    @staticmethod
    def movement_handler(key, twist):
        if key == 'w':
            Movement.move_forward(twist)
        elif key == 's':
            Movement.move_back(twist)
        elif key == "a":
            Movement.move_left(twist)
        elif key == "d":
            Movement.move_right(twist)
        elif key == "up":
            Movement.move_up(twist)
        elif key == "down":
            Movement.move_down(twist)
        elif key == "r":
            Movement.reset_any_move(twist)

        Movement.print_twist(twist)

        return twist

    @staticmethod
    def move_forward(twist):
        print("move forward")
        twist.linear.x += 1.0
        return twist

    @staticmethod
    def move_back(twist):
        print("move back")
        twist.linear.x -= 1.0
        return twist

    @staticmethod
    def move_left(twist):
        twist.linear.y -= 1.0
        print("move left")
        return twist

    @staticmethod
    def move_right(twist):
        print("move right")
        twist.linear.y += 1.0
        return twist

    @staticmethod
    def move_up(twist):
        print("move_up")
        twist.linear.z += 1.0
        return twist

    def move_down(twist):
        print("move_down")
        twist.linear.z -= 1.0
        return twist
    @staticmethod
    def reset_any_move(twist):
        print("resetting any move...")
        return Twist()

    @staticmethod
    def print_twist(twist):
        str = f"Linear: [{twist.linear.x}|{twist.linear.y}|{twist.linear.z}] Angular: [{twist.angular.x}|{twist.angular.y}|{twist.angular.z}]"
        print (str)

if __name__ == '__main__':
    publisher = MyService()

