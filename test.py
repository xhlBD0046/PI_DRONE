
import collections
from collections.abc import MutableMapping
collections.MutableMapping = collections.abc.MutableMapping

from dronekit import connect,VehicleMode

from serial import Serial
import time
# Connect to the Vehicle (in this case a UDP endpoint)
# 注意 baud 必须是921600
# Connect to the vehicle

# 关于无人机RC
# FS_THR_ENABLE = 0 脱离RC控制
try:
    vehicle = connect('/dev/ttyUSB0', wait_ready=True, baud=921600)
    print("Connected to vehicle successfully.")
except Exception as e:
    print(f"Failed to connect: {e}")
    exit()
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
while count<10:
    
    vehicle.channels.overrides = {'1': 1500, '2': 1500, '3': 1500, '4': 1500}
    print("Waiting to be armable",count)
    print("System status: %s" % vehicle.system_status.state)
    print("Mode: %s" % vehicle.mode.name)
    print("Armed: %s" % vehicle.armed)
    time.sleep(1)
    count+=1

vehicle.close()