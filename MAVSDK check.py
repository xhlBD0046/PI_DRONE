import asyncio
from mavsdk import System

async def get_drone_info():
    # Connect to the vehicle (e.g., via USB)
    drone = System()
    await drone.connect(system_address="serial:///dev/ttyUSB0:921600")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"Drone discovered with UUID: {state}")
            break

    # Retrieve various information about the drone
    async for position in drone.telemetry.position():
        print(f"Global Location: {position.latitude_deg}, {position.longitude_deg}, {position.absolute_altitude_m}")
        print(f"Relative Altitude: {position.relative_altitude_m}")
        break

    async for attitude in drone.telemetry.altitude():
        print(f"Attitude: Roll: {attitude.roll_deg}, Pitch: {attitude.pitch_deg}, Yaw: {attitude.yaw_deg}")
        break

    async for velocity in drone.telemetry.velocity_ned():
        print(f"Velocity (NED): North: {velocity.north_m_s} m/s, East: {velocity.east_m_s} m/s, Down: {velocity.down_m_s} m/s")
        break

    async for battery in drone.telemetry.battery():
        print(f"Battery: {battery.remaining_percent * 100}% remaining")
        break

    async for gps_info in drone.telemetry.gps_info():
        print(f"GPS: Satellites used: {gps_info.num_satellites}, Fix type: {gps_info.fix_type}")
        break

    async for health in drone.telemetry.health():
        print(f"EKF OK?: {health.is_ekf_ok}")
        break

    async for in_air in drone.telemetry.in_air():
        print(f"Is the drone flying?: {in_air}")
        break

    async for armed in drone.telemetry.armed():
        print(f"Armed: {armed}")
        break

    async for flight_mode in drone.telemetry.flight_mode():
        print(f"Flight Mode: {flight_mode}")
        break

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_drone_info())
