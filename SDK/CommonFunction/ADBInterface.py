from .BaseInterface import BaseInterface
from SDK.OSApi.OSAPiShell import OSAPiShell

shell = OSAPiShell()


class ADBInterface(BaseInterface):
    def __init__(self):
        pass

    def getTimeFormat(self):
        shell.SendCommand("settings get system time_12_24")
        return shell.successMsg

