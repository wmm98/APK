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

    logFile.logInfo("*****修改语言为中文********")

    try:
        iniFile.setSection(Config.section_language)
        logFile.logInfo("检查当前语言")
        if not commFunc.enableSet(testApi.setLanguageConfiguration("zh-cn")):
            logFile.logInfo("修改语言为中文失败")
        logFile.logInfo("修改语言为中文成功")
        commFunc.waitSetResponse()
        currentLanguage = testApi.getLanguageConfiguration()
        iniFile.addKeyValue(Config.section_language, Config.option_language, currentLanguage)
        logFile.logInfo("Language ： %s" % currentLanguage)

    except Exception as e:
        logFile.logErr(str(e))

    # 测试最后复制log出来
    iniFile.setSection("EndFlag")
    iniFile.addKeyValue("EndFlag", "flag", "end")
    logFile.logInfo("*****测试结束********")
    fileOperate.copyFile("%s/%s" % (appRunPath, Config.testDirectory), commFunc.getExternalStorageAbsolutePath())
