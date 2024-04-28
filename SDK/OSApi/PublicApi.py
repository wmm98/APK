class TelApi:
    def __init__(self, osApi):
        self.TelOSApi = osApi

    def getSystemControl(self):
        return self.TelOSApi.getSystemControl()

    def getApplicationControl(self):
        return self.TelOSApi.getApplicationControl()

    def getDisplayControl(self):
        return self.TelOSApi.getDisplayControl()

    def getDeviceInfoControl(self):
        return self.TelOSApi.getDeviceInfoControl()

    def getNetworkControl(self):
        return self.TelOSApi.getNetworkControl()

    def getMiscControl(self):
        return self.TelOSApi.getMiscControl()

    def getCommonControl(self):
        return self.TelOSApi.getCommonControl()

    def getSelfCheckControl(self):
        return self.TelOSApi.getSelfCheckControl()