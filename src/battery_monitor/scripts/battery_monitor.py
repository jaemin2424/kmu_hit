#!/usr/bin/env python3

import rospy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sensor_msgs.msg import BatteryState

# 데이터 저장 리스트
times = []
voltages = []
currents = []
battery_percentage = 0  # 배터리 잔량 (%)

# 적응형 그래프 범위 조정 변수
max_points = 100  # 그래프에 표시할 최대 데이터 개수

def update_graph(i):
    global times, voltages, currents, battery_percentage

    plt.clf()
    
    # 전압 그래프
    plt.subplot(2, 1, 1)
    plt.plot(times, voltages, label="Voltage (V)", color='blue')
    plt.xlabel("Time")
    plt.ylabel("Voltage (V)")
    plt.legend()
    
    # 전류 그래프 (음수값 방지)
    plt.subplot(2, 1, 2)
    plt.plot(times, currents, label="Current (A)", color='red')
    plt.xlabel("Time")
    plt.ylabel("Current (A)")
    plt.legend()

    # 배터리 잔량 표시
    plt.figtext(0.15, 0.02, f"Battery: {battery_percentage:.1f}%", fontsize=12, color="green")

def battery_callback(msg):
    global times, voltages, currents, battery_percentage

    current_time = rospy.Time.now().to_sec()
    
    times.append(current_time)
    voltages.append(msg.voltage)
    currents.append(abs(msg.current))  # 전류값을 절대값으로 변환 (음수 방지)
    battery_percentage = msg.percentage * 100  # 0~1 범위를 0~100%로 변환

    # 적응형 그래프: 데이터가 일정 개수를 넘으면 오래된 데이터 삭제
    if len(times) > max_points:
        times.pop(0)
        voltages.pop(0)
        currents.pop(0)

def listener():
    rospy.init_node('battery_visualizer', anonymous=True)
    rospy.Subscriber('/mavros/battery', BatteryState, battery_callback)

    # 실시간 그래프 애니메이션 실행
    fig = plt.figure()
    ani = animation.FuncAnimation(fig, update_graph, interval=1000)
    plt.show()

if __name__ == '__main__':
    listener()
