from phue import Bridge

class lights:
    bridge = ""
    lights = ""

    def __init__(self, ip):
        self.bridge = self.getBridge(ip)
        if self.bridge != False:
            self.lights = self.getLights()

    def getBridge(self,ip):
        try:
            bridge = Bridge(ip)
            return bridge
        except ConnectionError as e:
            return False

    def getLights(self):
        self.bridge.connect()
        lights = self.bridge.lights
        return lights

    def turnOFF(self):
        for l in self.lights:
            l.on = False

    def getStatus(self):
        for l in self.lights:
            if l.on:
                return True
        return False

