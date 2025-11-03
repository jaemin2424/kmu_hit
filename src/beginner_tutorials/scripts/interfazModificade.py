#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
import tkinter as tk

class DroneControlGUI:
    def __init__(self, master):
        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        rospy.init_node('drone_control_gui', anonymous=True)
        self.twist = Twist()

        master.title("Drone Control")

        # 버튼 생성
        tk.Button(master, text="전진", command=self.forward, width=15).grid(row=0, column=1)
        tk.Button(master, text="후진", command=self.backward, width=15).grid(row=2, column=1)
        tk.Button(master, text="좌회전", command=self.left, width=15).grid(row=1, column=0)
        tk.Button(master, text="우회전", command=self.right, width=15).grid(row=1, column=2)
        tk.Button(master, text="상승", command=self.up, width=15).grid(row=0, column=2)
        tk.Button(master, text="하강", command=self.down, width=15).grid(row=2, column=2)
        tk.Button(master, text="정지", command=self.stop, width=15, bg='red').grid(row=1, column=1)

    # 각 버튼의 동작
    def forward(self):
        self.twist.linear.x = 1.0
        self.twist.angular.z = 0.0
        self.pub.publish(self.twist)

    def backward(self):
        self.twist.linear.x = -1.0
        self.twist.angular.z = 0.0
        self.pub.publish(self.twist)

    def left(self):
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.5
        self.pub.publish(self.twist)

    def right(self):
        self.twist.linear.x = 0.0
        self.twist.angular.z = -0.5
        self.pub.publish(self.twist)

    def up(self):
        self.twist.linear.z = 1.0
        self.pub.publish(self.twist)

    def down(self):
        self.twist.linear.z = -1.0
        self.pub.publish(self.twist)

    def stop(self):
        self.twist = Twist()
        self.pub.publish(self.twist)

if __name__ == '__main__':
    root = tk.Tk()
    gui = DroneControlGUI(root)
    root.mainloop()

