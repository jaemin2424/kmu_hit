#!/usr/bin/env python3
import rospy
import subprocess
from diagnostic_updater import Updater, DiagnosticTask
from diagnostic_msgs.msg import DiagnosticStatus

class CPUMonitor(DiagnosticTask):
    def __init__(self):
        super(CPUMonitor, self).__init__("CPU Temperature")
        self.cpu_temp = 0.0

    def update_cpu_temp(self):
        try:
            # `sensors` 명령어 실행 후 결과 가져오기
            result = subprocess.check_output(["sensors"]).decode("utf-8")
            for line in result.split("\n"):
                if "Core 0" in line:
                    self.cpu_temp = float(line.split("+")[1].split("°")[0])
        except Exception as e:
            rospy.logerr(f"Error reading CPU temperature: {e}")

    def run(self, stat):
        self.update_cpu_temp()
        
        if self.cpu_temp > 80:
            stat.summary(DiagnosticStatus.WARN, "CPU Overheating!")
        else:
            stat.summary(DiagnosticStatus.OK, "CPU Normal")

        stat.add("CPU Temperature (C)", self.cpu_temp)
        return stat

rospy.init_node("cpu_monitor")
updater = Updater()
updater.setHardwareID("cpu")
cpu_diag = CPUMonitor()
updater.add(cpu_diag)

while not rospy.is_shutdown():
    updater.update()
    rospy.sleep(1.0)
