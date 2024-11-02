import collections
from collections.abc import MutableMapping
collections.MutableMapping = collections.abc.MutableMapping

from dronekit import connect,VehicleMode, LocationGlobalRelative

from serial import Serial
import time

# Connection string for Pixhawk flight controller (adjust as necessary)
connection_string = '192.168.0.232:14550'

print('Connecting to vehicle on: %s' % connection_string)
# Connect to the vehicle (replace with appropriate port and baud rate)
vehicle = connect(connection_string, wait_ready=True)

def arm_and_takeoff(aTargetAltitude):
    """
    Arms the vehicle and flies to a target altitude.
    """
    print("Basic pre-arm checks")
    # Wait until the vehicle is ready to arm
    while not vehicle.is_armable:
        print(" Waiting for vehicle to initialize...")
        time.sleep(1)

    print("Arming motors")
    # Set the mode to GUIDED and arm the motors
    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    # Wait until motors are armed
    while not vehicle.armed:
        print(" Waiting for arming...")
        time.sleep(1)

    print("Taking off!")
    # Take off to the target altitude
    vehicle.simple_takeoff(aTargetAltitude)

    # Wait until the vehicle reaches the target altitude
    while True:
        print(" Altitude: ", vehicle.location.global_relative_frame.alt)
        # Break if the altitude is 95% of the target altitude
        if vehicle.location.global_relative_frame.alt >= aTargetAltitude * 0.95:
            print("Reached target altitude")
            break
        time.sleep(1)

# Take off to 10 meters
arm_and_takeoff(10)

print("Set default/target airspeed to 3")
vehicle.airspeed = 3

print("Going towards first point for 30 seconds ...")
point1 = LocationGlobalRelative(-35.361354, 149.165218, 20)
vehicle.simple_goto(point1)

# Fly towards the first point for 30 seconds
time.sleep(30)

print("Going towards second point for 30 seconds (groundspeed set to 10 m/s) ...")
point2 = LocationGlobalRelative(-35.363244, 149.168801, 20)
vehicle.simple_goto(point2, groundspeed=10)

# Fly towards the second point for 30 seconds
time.sleep(30)

print("Returning to Launch")
vehicle.mode = VehicleMode("RTL")  # Return to Launch

print("Close vehicle object")
vehicle.close()  # Close the vehicle connection
