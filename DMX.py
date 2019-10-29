import time
import dmx

class pyDMX:
    def __init__(self, devName = "/dev/ttyUSB0"):
        self.arrayBytes = [0]*512
        self.sender = dmx.DMX_Serial(devName)

    def set_channel(self, ch, val):
        self.arrayBytes[ch-1] = val
        print(bytearray(self.arrayBytes))
        self.sender.set_data(bytearray(self.arrayBytes))
    def run(self):
        print("starting...")
        self.sender.start()

    def halt(self):
        self.sender.stop()

dmx = pyDMX("/dev/ttyUSB2")
dmx.run()
dmx.set_channel(1, 255)
while(True):
    dmx.set_channel(2, 255)
    dmx.set_channel(3, 0)
    time.sleep(0.5)
    dmx.set_channel(2, 0)
    dmx.set_channel(3, 255)
    time.sleep(0.5)

dmx.halt()
