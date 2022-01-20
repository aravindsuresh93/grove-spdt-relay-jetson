"""
This file can be used to control Grove 4 channel SPDT relay using Jetson devices via I2C protocol

Generally the device address is 0x11 and the address to which we should write the data is 0x10
writing 1 (0001) to 0x10 would switch on the first relay
writing 2 (0010) to 0x10 would switch on the second relay
writing 3 (0011) to 0x10 would switch on the first & second relays
writing 4 (0100) to 0x10 would switch on the 3rd relay and so on

sample linux commands to do this

i2cset -y 8 0x11 0x10 0

"""
from smbus2 import SMBus

JETSON_BUS = 8
DEVICE_ADDRESS = 0x11
ADDRESS = 0x10
ON = 1
OFF = 0

class GroveSPDTRelay:
    def __init__(self):
        self.bus = SMBus(JETSON_BUS)
        self.current_state = ["0","0","0","0"]

    def change(self, relay, value):
        """method used to set the current state of the relay

        Args:
            relay (int): relay that is to be enabled
            value (int): 0 or 1
        """
        if relay < 1 or relay > 4:
            return # assertion/ exception can be added here according to the requirements
        self.current_state[relay-1] = str(value)

    def push(self):
        """method that joins the array to string, revereses the binary representation and converts to int-base 2
        """
        data = int("".join(self.current_state)[::-1], 2)
        self.bus.write_word_data(DEVICE_ADDRESS, ADDRESS, data)

    def set(self, relay):
        """method to ON the relay

        Args:
            relay (int): index of relay to be switched on
        """
        self.change(relay, ON)
        self.push()

    def reset(self,relay):
        """method of OFF the relay

        Args:
            relay (int): index of relay to be switched off
        """
        self.change(relay, OFF)
        self.push()