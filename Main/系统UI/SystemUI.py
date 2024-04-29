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

    logFile.logInfo("*****系统UI测试开始********")

    try:
        iniFile.setSection("SystemUI")
        logFile.logInfo("检查状态栏状态")
        statusBar = testApi.getStatusbarEnable()
        if statusBar == OSApiConstants.ABLE_TYPE_ENABLE:
            iniFile.addKeyValue("SystemUI", "status_bar", "on")
            logFile.logInfo("status_bar status： on")
        elif statusBar == OSApiConstants.ABLE_TYPE_DISABLE:
            iniFile.addKeyValue("SystemUI", "status_bar", "off")
            logFile.logInfo("status_bar status： off")
        else:
            iniFile.addKeyValue("SystemUI", "status_bar", "fail->%d" % statusBar)
            logFile.logErr("status_bar status： %s" % commFunc.dealOSErrCode(statusBar))

        logFile.logInfo("检查状态栏下拉状态")
        dropdownBar = testApi.getStatusbarDrop()
        if dropdownBar == OSApiConstants.ABLE_TYPE_ENABLE:
            iniFile.addKeyValue("SystemUI", "statusbar_drop", "on")
            logFile.logInfo("statusbar_drop status： on")
        elif dropdownBar == OSApiConstants.ABLE_TYPE_DISABLE:
            iniFile.addKeyValue("SystemUI", "statusbar_drop", "off")
            logFile.logInfo("statusbar_drop status： off")
        else:
            iniFile.addKeyValue("SystemUI", "statusbar_drop", "fail->%d" % dropdownBar)
            logFile.logErr("statusbar_drop status： %s" % commFunc.dealOSErrCode(dropdownBar))

        logFile.logInfo("检查导航栏下拉状态")
        navigationBar = testApi.getNavigationBarEnable()
        if navigationBar == OSApiConstants.ABLE_TYPE_ENABLE:
            iniFile.addKeyValue("SystemUI", "navigation_bar", "on")
            logFile.logInfo("navigation_bar status： on")
        elif navigationBar == OSApiConstants.ABLE_TYPE_DISABLE:
            iniFile.addKeyValue("SystemUI", "navigation_bar", "off")
            logFile.logInfo("navigation_bar status： off")
        else:
            iniFile.addKeyValue("SystemUI", "navigation_bar", "fail->%d" % navigationBar)
            logFile.logErr("navigation_bar status： %s" % commFunc.dealOSErrCode(navigationBar))

    except Exception as e:
        logFile.logErr(str(e))

    # 测试最后复制log出来
    iniFile.setSection("EndFlag")
    iniFile.addKeyValue("EndFlag", "flag", "end")
    logFile.logInfo("*****测试结束********")
    fileOperate.copyFile("%s/%s" % (appRunPath, Config.testDirectory), commFunc.getExternalStorageAbsolutePath())
