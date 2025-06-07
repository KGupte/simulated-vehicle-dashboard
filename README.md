# Simulated Vehicle Dashboard over CAN
This project emulates a vehicle ECU communication system over a virtual CAN interface (vcan0) using Raspberry Pi and Python. It simulates basic CAN messaging for speed, RPM, and fuel level and visualizes the received data.

Project Components

-CAN Transmitter (Sender)
  -Sends simulated CAN messages for speed, rpm, and fuel level.
  -Messages are sent on vcan0 using python-can.
  -Uses arbitration IDs:
    -0x100 for speed
    -0x101 for rpm
    -0x102 for fuel level

-CAN Receiver (Listener)
  -Listens on vcan0 and parses received CAN messages.
  -Based on arbitration ID, prints the signal with its respective unit.
  -Uses bitwise operations to decode speed and rpm (2-byte values) and fuel level (1-byte value).

-CAN Message Debugging with candump
  -To monitor live CAN traffic on your virtual CAN interface, use:
   "candump vcan0"
  -This command displays messages in the format:
   "vcan0 100 [2] 3C 00"

  -Explanation:
   "vcan0": Name of the virtual CAN interface.
   "100": Arbitration ID in hexadecimal (here, 0x100 for speed).
   "[2]": Number of data bytes (2 in this case).
   "3C 00": Hex representation of the message payload bytes.
   Each message line shows what the receiver would be parsing in real time. It's a valuable tool for verifying if messages are correctly sent and formatted.
   
Future Enhancements

-Add abstract typedefs like speed_t, rpm_t, fuel_level_t for AUTOSAR-style portability.
-Add a GUI using tkinter with sliders to dynamically simulate sensor values.
-Add logging of received messages with timestamps.
-Modularize components to simulate SW-Cs and connect them via a software-simulated RTE.

Setup Instructions

-Create virtual CAN interface:
  -Run these commands in terminal:
   "sudo modprobe vcan"
   "sudo ip link add dev vcan0 type vcan"
   "sudo ip link set up vcan0"

-Install required Python packages (in venv or global):
   "pip install python-can"
   "pip install tkinter" (tkinter may already be included in some Python distributions)

Transmitter code example:
-Uses can.interface.Bus to send messages over vcan0 with defined arbitration IDs and data bytes.

Receiver code example:
-Uses can.interface.Bus to receive messages over vcan0, checks arbitration ID, and parses byte data using bitwise operations.

Stop the receiver safely:
-Press Ctrl+C. Note: socket may show a warning; in future updates, implement a context manager to close the bus cleanly.

Important Terms

-CAN (Controller Area Network): A vehicle communication protocol for inter-ECU data exchange.
-python-can: Python library to interface with CAN hardware or virtual CAN.
-vcan: A virtual CAN network used for testing on Linux without actual CAN hardware.
-Arbitration ID: Unique identifier of a CAN message used for prioritization and parsing.
-DBC: A database file format that defines how CAN signals are encoded and scaled in CAN messages.
-Typedef abstraction: Creating custom types like speed_t for portability and platform independence.
-Runnables: Software entities in AUTOSAR that represent independent functional blocks.
-RTE: Runtime Environment in AUTOSAR that routes data between runnables and ECUs.