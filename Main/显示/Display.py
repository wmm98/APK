from jnius import autoclass
from SDK.OSApi.OSApi import OSApi
from SDK.OSApi.OSAPiShell import OSAPiShell
from SDK.OSApi.OSApiConstants import OSApiConstants
from SDK.OSApi.OSApiErrorCode import OSApiErrorCode
from SDK.CommonFunction.IntegrateFunction import CommFunction
from SDK.CommonFunction.OperateFile import OperateFile
from SDK.CommonFunction.OperateFile import OutPutTestResult, OutPutIniResult
from SDK.CommonFunction.Config import Config
from kivy.app import App
import sys
from kivy.app import App
from jnius import autoclass
# from android.permissions import request_permissions, Permission
import os

if __name__ == '__main__':
    # request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Context = PythonActivity.mActivity
    packageName = Context.getApplicationContext().getPackageName()
    Api = autoclass('com.android.common.osapi.OSApi')
    testApi = OSApi(Api(Context))
    fileOperate = OperateFile()
    commFunc = CommFunction()
    shell = OSAPiShell()
    # 初始化测试结果文件相关

    commFunc.initTestResultDirectory()
    appRunPath = commFunc.getCurrentPath()
    iniFile = OutPutIniResult()
    iniFile.createIniFile()
    logFile = OutPutTestResult()
    logFile.createFile()

    # # 创建存放测试结果的目录， 创建存放测试数据的文件,初始化后在sdcard/TestTeam的路径下
    logFile.logInfo("root 设备")
    if commFunc.enableSetGet(testApi.setAppRootEnable(OSApiConstants.ABLE_TYPE_ENABLE), testApi.getAppRootEnable()):
        logFile.logInfo("root 成功")

    else:
        logFile.logErr("root 失败")

    logFile.logInfo("*****显示测试开始********")

    try:
        iniFile.setSection("Display")
        logFile.logInfo("检查当前亮度")
        brightness = testApi.getBrightness()
        if brightness < OSApiErrorCode.OK:
            iniFile.addKeyValue("Display", "brightness", "fail->%d" % brightness)
            logFile.logErr("brightness： %s" % commFunc.dealOSErrCode(brightness))
        else:
            iniFile.addKeyValue("Display", "brightness", str(brightness))
            logFile.logInfo("brightness ： %d" % brightness)

        logFile.logInfo("检查当前字体大小")
        size = testApi.getFontSize()
        if size < OSApiErrorCode.OK:
            iniFile.addKeyValue("Display", "size", "fail->%d" % size)
            logFile.logErr("size： %s" % commFunc.dealOSErrCode(size))
        else:
            iniFile.addKeyValue("Display", "size", str(size))
            logFile.logInfo("size ： %d" % size)

    except Exception as e:
        logFile.logErr(str(e))

    # 测试最后复制log出来
    iniFile.setSection("EndFlag")
    iniFile.addKeyValue("EndFlag", "flag", "end")
    logFile.logInfo("*****测试结束********")
    fileOperate.copyFile("%s/%s" % (appRunPath, Config.testDirectory), commFunc.getExternalStorageAbsolutePath())
