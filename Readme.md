### Grove 4 channel SPDT relay control using Jetson Devices (I2C)

This repository helps us to control Grove 4 channel SPDT relay unit using Jetson devices via I2C protocol. 

####  Get started
1. Connect VCC, GND from the I2C to the any of the VCC, GND pins in your Jetson device
2. Connect SDA to PIN3 and SCL to PIN5, this would now be bus 8 of your Jetson device
3.  Run i2cdetect -y -r 8 to scan devices in bus 8, my case i got the below output

     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f  
00:          -- -- -- -- -- -- -- -- -- -- -- -- --  
10: -- 11 -- -- -- -- -- -- -- -- -- -- -- -- -- --  
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --  
70: -- -- -- -- -- -- -- --  
  
     11 (0x11) is the address of the device, usually Grove SPDT devices are at 0x11 or 0x12, find more details [here](https://wiki.seeedstudio.com/Grove-4-Channel_SPDT_Relay/)  

4. From github repo for [grove-ardiuno](https://github.com/Seeed-Studio/Multi_Channel_Relay_Arduino_Library) i found that the address to for controlling relays is 0x10
5. Run "i2cset -y 8 0x11 0x10 1" in your cmd to activate the first relay.

#### A brief walkthrough on how to activate relays
writing 1 (0001) to 0x10 would switch on the first relay  
writing 2 (0010) to 0x10 would switch on the second relay  
writing 3 (0011) to 0x10 would switch on the first & second relays  
writing 4 (0100) to 0x10 would switch on the 3rd relay  
and so on  
