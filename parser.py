#CAN Frame Parser
#Autored by Vivek Sreenivasan
#Email: vns9@njit.edu
from __future__ import print_function
import can

def __init__(self):
	can_interface = 'vcan0'
	bus = can.interface.Bus(can_interface, bustype = 'socketcan')


while(True):
	message = bus.recv()

	if message is None:
		print('Timeout occured, no message.')
	parseFrame(message)

def parseFrame(frame):
	id = frame.arbitration_id
	data = frame.data

	if():  #need address
		pack_pwr_sum["SOC"] = data[1]
		pack_pwr_sum["PACK_1"] = data[2:3]
		pack_pwr_sum["PACK_5"] = data[4:5]
	if():
		vehicle_state["GND_SPD"] = data[3:4]
		vehicle_state["T_ON"] = data[5:8]
