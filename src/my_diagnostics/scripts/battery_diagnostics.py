#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import BatteryState
from diagnostic_updater import Updater, DiagnosticTask
from diagnostic_msgs.msg import DiagnosticStatus

class BatteryMonitor(DiagnosticTask):
    def __init__(self):
        super(BatteryMonitor, self).__init__("Battery Status")
        self.battery_voltage = 12.6  

    def battery_callback(self, msg):
        self.battery_voltage = msg.voltage

    def run(self, stat):
        if self.battery_voltage < 10.5:
            stat.summary(DiagnosticStatus.WARN, "Low Battery!")
        elif self.battery_voltage < 9.5:
            stat.summary(DiagnosticStatus.ERROR, "Critical Battery Level!")
        else:
            stat.summary(DiagnosticStatus.OK, "Battery Normal")

        stat.add("Voltage", self.battery_voltage)
        return stat

rospy.init_node("battery_diagnostics")
updater = Updater()

updater.setHardwareID("none")  # 하드웨어 ID가 없는 경우 'none'으로 설정

battery_monitor = BatteryMonitor()
updater.add(battery_monitor)
rospy.Subscriber("/battery_status", BatteryState, battery_monitor.battery_callback)

while not rospy.is_shutdown():
    updater.update()
    rospy.sleep(1.0)

