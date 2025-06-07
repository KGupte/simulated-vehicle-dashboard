import can

# Create CAN bus interface
bus = can.interface.Bus(channel='vcan0', interface='socketcan')

def parse_speed(data):
    speed = data[0] | (data[1] << 8)
    print(f"Received Speed: {speed} km/h")

def parse_rpm(data):
    rpm = data[0] | (data[1] << 8)
    print(f"Received RPM: {rpm}")

def parse_fuel(data):
    level = data[0]
    print(f"Received Fuel Level: {level} %")

if __name__ == "__main__":
    print("Listening for CAN messages...")
    while True:
        message = bus.recv()
        if message.arbitration_id == 0x100:
            parse_speed(message.data)
        elif message.arbitration_id == 0x101:
            parse_rpm(message.data)
        elif message.arbitration_id == 0x102:
            parse_fuel(message.data)
	# else:
            # print(f"Undefined arbitration id {hex(message.arbitration_id)}")
