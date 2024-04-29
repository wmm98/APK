from SDK.OSApi import OSAPiShell, OSApi
from SDK.OSApi.OSApiConstants import OSApiConstants
from SDK.OSApi.OSApiErrorCode import OSApiErrorCode
from SDK.CommonFunction.OperateFile import OperateFile
from SDK.CommonFunction.Config import Config
from jnius import autoclass
import os
import time

fileOperate = OperateFile()
Environment = autoclass('android.os.Environment')
shell = OSAPiShell.OSAPiShell()


class CommFunction:
    def __init__(self):
        pass

    def dealOSErrCode(self, errCode):
        if errCode == OSApiErrorCode.ERR_SYS_TIMEOUT:
            return "%d %s" % (errCode, "超时")
        elif errCode == OSApiErrorCode.ERR_SYS_INVALID:
            return "%d %s" % (errCode, "参数非法")
        elif errCode == OSApiErrorCode.ERR_SYS_NO_DEV:
            return "%d %s" % (errCode, "设备未找到")
        elif errCode == OSApiErrorCode.ERR_SYS_NO_INIT:
            return "%d %s" % (errCode, "设备或资源未初始化")
        elif errCode == OSApiErrorCode.ERR_SYS_ALREADY_INIT:
            return "%d %s" % (errCode, "设备或资源已初始化")
        elif errCode == OSApiErrorCode.ERR_SYS_OVER_FLOW:
            return "%d %s" % (errCode, "缓存不足")
        elif errCode == OSApiErrorCode.ERR_SYS_NOT_SUPPORT:
            return "%d %s" % (errCode, "暂不支持")
        elif errCode == OSApiErrorCode.ERR_SYS_UNEXPECT:
            return "%d %s" % (errCode, "未知错误")
        elif errCode == OSApiErrorCode.ERR_SYS_NO_PERMISSION:
            return "%d %s" % (errCode, "无权限访问")
        elif errCode == OSApiErrorCode.ERR_SYS_DATA_TRANSMIT:
            return "%d %s" % (errCode, "通信失败")

    def initTestResultDirectory(self):
        # 创建存放测试结果的目录， 创建存放测试数据的文件
        # 直接在app文件夹里面记录，再复制出去外部存储里面
        # ExternalStorageDire = self.getExternalStorageAbsolutePath()
        # # self.chDirPath(ExternalStorageDire))
        if Config.testDirectory not in os.listdir(self.getCurrentPath()):
            fileOperate.osCreateDirectory(Config.testDirectory)
        self.chDirPath(Config.testDirectory)
        if Config.screenShotDirectory not in os.listdir(self.getCurrentPath()):
            fileOperate.osCreateDirectory(Config.screenShotDirectory)
        self.chDirPath("..")

    def enableSetGet(self, setFunc, getFunc):
        enableFlag = False
        for i in range(Config.checkTimes):
            if setFunc == OSApiErrorCode.OK:
                self.waitSetResponse()
                if getFunc == OSApiConstants.ABLE_TYPE_ENABLE:
                    enableFlag = True
                    break
        return enableFlag

    def enableGet(self):
        pass

    def disableGet(self):
        pass

    def disableSetGet(self, setFunc, getFunc):
        pass

    def operateSuccess(self, setFunc):
        pass

    def sendCommandSuccess(self, operation):
        pass

    def timeSleep(self, seconds):
        time.sleep(seconds)

    def waitSetResponse(self):
        self.timeSleep(Config.waitSetRespTime)

    def getExternalStorageAbsolutePath(self):
        return Environment.getExternalStorageDirectory().getAbsolutePath()

    def getCurrentPath(self):
        return os.getcwd()

    def chDirPath(self, path):
        os.chdir(path)

    def chRootPath(self):
        os.path.expanduser('~')

    def lsDirePath(self, path=None):
        if path is None:
            shell.SendCommand("ls")
            if shell.result == OSApiErrorCode.OK:
                return shell.successMsg
            else:
                return "Send command->\"ls\" fail, return code is %d pls check !!!" % shell.result
