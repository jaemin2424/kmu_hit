#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from std_msgs.msg import Float32

def image_callback(msg):
    # 이미지가 촬영된 시간
    image_time = msg.header.stamp
    # 현재 시간 (노드에서 수신한 시간)
    now = rospy.Time.now()
    # 딜레이 계산
    delay = (now - image_time).to_sec()
    # 딜레이 값 퍼블리시
    pub.publish(delay)

if __name__ == '__main__':
    rospy.init_node('camera_delay_checker')
    
    # 딜레이 퍼블리시할 토픽
    pub = rospy.Publisher('/camera/delay', Float32, queue_size=10)
    
    # 카메라 이미지 구독 (실제 사용 중인 토픽 이름으로 바꾸세요!)
    rospy.Subscriber('/usb_cam/image_raw', Image, image_callback)
    
    rospy.spin()

