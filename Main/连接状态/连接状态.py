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
from android.permissions import request_permissions, Permission
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
    iniFile.createIniFile(appRunPath, Config.actualResultFileName)
    logFile = OutPutTestResult()
    logFile.createFile(appRunPath, Config.automationLog)

    # # 创建存放测试结果的目录， 创建存放测试数据的文件,初始化后在sdcard/TestTeam的路径下
    logFile.logInfo("root 设备")
    if commFunc.enableSetGet(testApi.setAppRootEnable(OSApiConstants.ABLE_TYPE_ENABLE), testApi.getAppRootEnable()):
        logFile.logInfo("root 成功")

    else:
        logFile.logErr("root 失败")

    logFile.logInfo("*****连接状态测试开始********")
    try:
        iniFile.setSection("Connection")
        logFile.logInfo("检查wifi连接状态")
        wifiStatus = testApi.getWifiEnable()
        if wifiStatus == OSApiConstants.ABLE_TYPE_ENABLE:
            iniFile.addKeyValue("Connection", "wifi", "on")
            logFile.logInfo("wifi status： on")
        elif wifiStatus == OSApiConstants.ABLE_TYPE_DISABLE:
            iniFile.addKeyValue("Connection", "wifi", "off")
            logFile.logInfo("wifi status： off")
        else:
            iniFile.addKeyValue("Connection", "wifi", "fail->%d" % wifiStatus)
            logFile.logErr("wifi status： %s" % commFunc.dealOSErrCode(wifiStatus))

        # mobile
        logFile.logInfo("检查mobile连接状态")
        mobileStatus = testApi.getMobileDataEnable()
        if mobileStatus == OSApiConstants.ABLE_TYPE_ENABLE:
            iniFile.addKeyValue("Connection", "mobile", "on")
            logFile.logInfo("mobile status： on")
        elif mobileStatus == OSApiConstants.ABLE_TYPE_DISABLE:
            iniFile.addKeyValue("Connection", "mobile", "off")
            logFile.logInfo("mobile status： off")
        else:
            iniFile.addKeyValue("Connection", "mobile", "fail->%d" % mobileStatus)
            logFile.logErr("mobile status： %s" % commFunc.dealOSErrCode(mobileStatus))

        # bt
        logFile.logInfo("检查蓝牙连接状态")
        btStatus = testApi.getBluetoothEnable()
        if btStatus == OSApiConstants.ABLE_TYPE_ENABLE:
            iniFile.addKeyValue("Connection", "bt", "on")
            logFile.logInfo("bt status： on")
        elif btStatus == OSApiConstants.ABLE_TYPE_DISABLE:
            iniFile.addKeyValue("Connection", "bt", "off")
            logFile.logInfo("bt status： off")
        else:
            iniFile.addKeyValue("Connection", "bt", "fail->%d" % btStatus)
            logFile.logErr("bt status： %s" % commFunc.dealOSErrCode(btStatus))

        # gps
        logFile.logInfo("检查GPS接状态")
        locationStatus = testApi.getLocationEnable()
        if locationStatus == OSApiConstants.ABLE_TYPE_ENABLE:
            iniFile.addKeyValue("Connection", "gps", "on")
            logFile.logInfo("gps status： on")
        elif locationStatus == OSApiConstants.ABLE_TYPE_DISABLE:
            iniFile.addKeyValue("Connection", "gps", "off")
            logFile.logInfo("gps status： off")
        else:
            iniFile.addKeyValue("Connection", "bt", "fail->%d" % locationStatus)
            logFile.logErr("gps status： %s" % commFunc.dealOSErrCode(locationStatus))
    except Exception as e:
        logFile.logErr(str(e))
    finally:
        # 测试最后复制log出来
        iniFile.setSection("EndFlag")
        iniFile.addKeyValue("EndFlag", "flag", "end")
        logFile.logInfo("*****测试结束********")
        fileOperate.copyFile("%s/%s" % (appRunPath, Config.testDirectory), commFunc.getExternalStorageAbsolutePath())