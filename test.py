
import collections
from collections.abc import MutableMapping
collections.MutableMapping = collections.abc.MutableMapping

from dronekit import connect

from serial import Serial
import time
# Connect to the Vehicle (in this case a UDP endpoint)
# 注意 baud 必须是921600
vehicle = connect('/dev/ttyUSB0', wait_ready=True, baud=921600)

# vehicle is an instance of the Vehicle class
print("Autopilot Firmware version: %s" % vehicle.version)
print("Autopilot capabilities (supports ftp): %s" % vehicle.capabilities.ftp)
print("Global Location: %s" % vehicle.location.global_frame)
print("Global Location (relative altitude): %s" % vehicle.location.global_relative_frame)
print("Local Location: %s" % vehicle.location.local_frame)  # NED
print("Attitude: %s" % vehicle.attitude)
print("Velocity: %s" % vehicle.velocity)
print("GPS: %s" % vehicle.gps_0)
print("Groundspeed: %s" % vehicle.groundspeed)
print("Airspeed: %s" % vehicle.airspeed)
print("Gimbal status: %s" % vehicle.gimbal)
print("Battery: %s" % vehicle.battery)
print("EKF OK?: %s" % vehicle.ekf_ok)
print("Last Heartbeat: %s" % vehicle.last_heartbeat)
print("Rangefinder: %s" % vehicle.rangefinder)
print("Rangefinder distance: %s" % vehicle.rangefinder.distance)
print("Rangefinder voltage: %s" % vehicle.rangefinder.voltage)
print("Heading: %s" % vehicle.heading)
print("Is Armable?: %s" % vehicle.is_armable)
print("System status: %s" % vehicle.system_status.state)
print("Mode: %s" % vehicle.mode.name)  # settable
print("Armed: %s" % vehicle.armed)  # settable


# test to arm the drone:
count = 0
vehicle.armed = True
while vehicle.armed==False:
    print("Waiting to be armable",count)
    print("System status: %s" % vehicle.system_status.state)
    print("Mode: %s" % vehicle.mode.name)
    print("Armed: %s" % vehicle.armed)
    time.sleep(1)
    count+=1
print("vehicle is now armed")