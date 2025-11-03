#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Imu
from tf2_ros import TransformBroadcaster
from geometry_msgs.msg import TransformStamped

# 로봇의 중앙 위치 (예: x=0.5, y=0, z=0.2)
CENTER_X = 1.0
CENTER_Y = 0.5
CENTER_Z = 0.2

def imu_callback(data):
    br = TransformBroadcaster()
    t = TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "world"
    t.child_frame_id = "base_link"
    
    # 로봇의 중앙 위치로 회전축 중심 이동
    t.transform.translation.x = CENTER_X
    t.transform.translation.y = CENTER_Y
    t.transform.translation.z = CENTER_Z
    t.transform.rotation = data.orientation
    
    br.sendTransform(t)

def main():
    rospy.init_node('pixhawk_tf_publisher')
    rospy.Subscriber('/mavros/imu/data', Imu, imu_callback)
    rospy.spin()

if __name__ == '__main__':
    main()

