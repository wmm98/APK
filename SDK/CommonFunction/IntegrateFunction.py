from SDK.OSApi import OSAPiShell, OSApi
from SDK.OSApi.OSApiConstants import OSApiConstants
from SDK.OSApi.OSApiErrorCode import OSApiErrorCode
from SDK.CommonFunction.OperateFile import OperateFile, OutPutIniResult, OutPutTestResult
from SDK.CommonFunction.Config import Config
from SDK.CommonFunction.ADBInterface import ADBInterface
from jnius import autoclass
import os
import time

PythonActivity = autoclass('org.kivy.android.PythonActivity')
Context = PythonActivity.mActivity
Api = autoclass('com.android.common.osapi.OSApi')

testApi = OSApi.OSApi(Api(Context))
fileOperate = OperateFile()
Environment = autoclass('android.os.Environment')
shell = OSAPiShell.OSAPiShell()
iniFile = OutPutIniResult()
logFile = OutPutTestResult()


class CommFunction(ADBInterface):
    def __init__(self):
        pass

    def getConfigDirePath(self):
        expectResultPath = os.path.join(self.getExternalStorageAbsolutePath(), Config.expectResult)
        shell.SendCommand("ls %s" % expectResultPath)
        configDireName = shell.successMsg.strip()
        configDirePath = os.path.join(expectResultPath, configDireName)
        return configDirePath

    def getConfigDireName(self):
        return os.path.basename(self.getConfigDirePath())

    def getIniFileName(self):
        return os.path.basename(self.getIniFilePath())

    def getIniFilePath(self):
        shell.SendCommand("ls %s | grep ini" % self.getConfigDirePath())
        iniFileName = shell.successMsg.strip()
        iniPath = os.path.join(self.getConfigDirePath(), iniFileName)
        return iniPath

    def getKeyStatus(self, section, key):
        logFile.logInfo("%s状态" % key)
        keyStatus = testApi.getKeyEnable(OSApiConstants.KEY_TYPE_BACK)
        if keyStatus == OSApiConstants.ABLE_TYPE_ENABLE:
            iniFile.addKeyValue(section, key, "on")
            logFile.logInfo("%s status： on" % key)
        elif keyStatus == OSApiConstants.ABLE_TYPE_DISABLE:
            iniFile.addKeyValue(section, key, "off")
            logFile.logInfo("%s status： off" % key)
        else:
            iniFile.addKeyValue(section, key, "fail->%d" % keyStatus)
            logFile.logErr("back_key status： %s" % self.dealOSErrCode(keyStatus))

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
        # if Config.expectResult not in os.listdir(self.getCurrentPath()):
        #     fileOperate.osCreateDirectory(Config.expectResult)
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
        if enableFlag:
            logFile.logInfo("enable的状态：1")
        else:
            logFile.logInfo("enable的状态：0")
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

    def waitSetResponse(self):
        self.timeSleep(Config.waitSetRespTime)


