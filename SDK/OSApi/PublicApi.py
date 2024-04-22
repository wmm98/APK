
class TelApi:
    def __init__(self, osApi):
        self.OSApi = osApi

    def getSystemControl(self):
        return self.OSApi.getSystemControl()

    def getApplicationControl(self):
        return self.OSApi.getApplicationControl()

    def getDisplayControl(self):
        return self.OSApi.getDisplayControl()

    def getDeviceInfoControl(self):
        return self.OSApi.getDeviceInfoControl()

    def getNetworkControl(self):
        return self.OSApi.getNetworkControl()

    def getMiscControl(self):
        return self.OSApi.getMiscControl()

    def getCommonControl(self):
        return self.OSApi.getCommonControl()

    def getSelfCheckControl(self):
        return self.OSApi.getSelfCheckControl()