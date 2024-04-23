from jnius import autoclass


class OSAPiShell:
    def __init__(self):
        OSShell = autoclass('com.android.common.telpo.utils.ShellUtils')
        self.Shell = OSShell
        self.isSend = True

    def SendCommand(self, cmd):
        res = self.Shell.execCommand(cmd, self.isSend)
        return {"result": res.result, "successMsg": res.successMsg}

    def getResult(self):
        # print(self.Result.result)
        pass


if __name__ == '__main__':
    shell = OSAPiShell()
    res = shell.SendCommand("ls data")

    # print("返回的结果:", res)
    # print(res.result)
    # print(res.successMsg)
    # print(res.errorMsg)
    # print(list(shell.SendCommand("ls data")))
    # shell.getResult()
