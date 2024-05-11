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
import os


if __name__ == '__main__':

    Environment = autoclass('android.os.Environment')
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Context = PythonActivity.mActivity
    packageName = Context.getApplicationContext().getPackageName()
    Api = autoclass('com.android.common.osapi.OSApi')
    testApi = OSApi(Api(Context))
    fileOperate = OperateFile()
    commFunc = CommFunction()
    shell = OSAPiShell()
    # 初始化相关文件
    commFunc.initTestResultDirectory()
    appRunPath = commFunc.getCurrentPath()
    iniFile = OutPutIniResult()
    iniFile.createIniFile()
    logFile = OutPutTestResult()
    logFile.createFile()

    # 创建存放测试结果的目录， 创建存放测试数据的文件,初始化后在sdcard/TestTeam的路径下
    logFile.logInfo("root 设备")
    if commFunc.enableSetGet(testApi.setAppRootEnable(OSApiConstants.ABLE_TYPE_ENABLE), testApi.getAppRootEnable()):
        logFile.logInfo("root 成功")
    else:
        logFile.logErr("root 失败")

    logFile.logInfo("*****EmvRes库测试开始********")
    try:
        section = "EmvRes"
        option = "emv_res"
        iniFile.setSection(section)
        # 获取预期的so库
        shell.SendCommand("cat %s | grep %s" % (commFunc.getIniFilePath(), option))
        soName = os.path.basename(shell.successMsg.split("=")[1])
        logFile.logInfo("Emv_Res: so库名字为：%s" %soName)
        shell.SendCommand("ls /system/lib |grep %s" % soName)
        if soName in shell.successMsg:
            iniFile.addKeyValue(section, "emv_res", "pass")
            logFile.logInfo("系统显示emv_res库存在/system/lib： %s" % soName)
        else:
            iniFile.addKeyValue(section, "emv_res", "fail")
            logFile.logErr("系统显示emv_res库不存存在/system/lib： %s" % soName)

    except Exception as e:
        logFile.logErr(str(e))

    # 测试最后复制log出来
    iniFile.setSection("EndFlag")
    iniFile.addKeyValue("EndFlag", "flag", "end")
    logFile.logInfo("*****测试结束********")
    fileOperate.copyFile("%s/%s" % (appRunPath, Config.testDirectory), commFunc.getExternalStorageAbsolutePath())
