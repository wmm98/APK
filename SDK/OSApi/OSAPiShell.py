from jnius import autoclass

OSShell = autoclass('com.android.common.telpo.utils.ShellUtils')


class OSAPiShell:
    def __init__(self):
        self.Shell = OSShell
        self.isSend = True
        self.result = -1
        self.successMsg = ""

    def SendCommand(self, cmd):
        res = self.Shell.execCommand(cmd, self.isSend)
        self.result = res.result
        self.successMsg = res.successMsg

    def getResult(self):
        return self.result

    def getCmdResult(self):
        return self.successMsg


if __name__ == '__main__':
    shell = OSAPiShell()
    shell.SendCommand("ls data")

    # print("返回的结果:", res)
    # print(res.result)
    # print(res.successMsg)
    # print(res.errorMsg)
    # print(list(shell.SendCommand("ls data")))
    # shell.getResult()
