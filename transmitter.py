import can
import time

# Setup CAN bus interface (vcan0 for simulation)
bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

def send_speed(speed_kph):
    msg = can.Message(
        arbitration_id=0x100,
        data=[speed_kph & 0xFF, (speed_kph >> 8) & 0xFF],
        is_extended_id=False
    )
    bus.send(msg)
    print(f"Sent Speed: {speed_kph} km/h")

# TODO: Define send_rpm(rpm)
def send_rpm(rpm):
    msg = can.Message(
        arbitration_id=0x101,
        data=[rpm & 0xFF, (rpm >> 8) & 0xFF], #to split data which is more than 255 bit long
	is_extended_id=False
    )
    bus.send(msg)
    print(f"Sent RPM: {rpm}")

# TODO: Define send_fuel(level)
def send_fuel(level):
    msg = can.Message(
        arbitration_id=0x102,
        data=[level],
        is_extended_id=False
    )
    bus.send(msg)
    print(f"Sent Fuel Level: {level} %")

if __name__ == "__main__":
    while True:
        send_speed(60)  # example speed
        send_rpm(2500)  # example rpm
        send_fuel(87)   # example fuel level
        time.sleep(1)
