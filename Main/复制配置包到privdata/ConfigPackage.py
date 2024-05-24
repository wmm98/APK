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

    logFile.logInfo("*****导入配置包测试开始********")
    try:
        section = "ConfigImport"
        exist_option = "exist"
        import_option = "import"
        iniFile.setSection(section)
        # 获取预期的so库
        # 从sdcard 推送配置包到/privdata下面
        unzipPackageName = commFunc.getConfigDireName()
        # 判断配置包存在与否
        shell.SendCommand("ls %s |grep %s" % (commFunc.getExternalStorageAbsolutePath(), unzipPackageName))
        searchPackageName = shell.successMsg.strip()
        # 判断sdcard是否存在配置包
        try:
            if unzipPackageName in searchPackageName and ".zip" == os.path.splitext(searchPackageName)[1]:
                iniFile.addKeyValue(section, exist_option, "1")
            else:
                iniFile.addKeyValue(section, exist_option, "0")
        except Exception as e:
            logFile.logErr(str(e))
            iniFile.addKeyValue(section, exist_option, "0")

        # 复制到/privdata
        fileOperate.copyFile(os.path.join(commFunc.getExternalStorageAbsolutePath(), searchPackageName), "/privdata/")
        shell.SendCommand("ls /privdata")
        if searchPackageName in shell.successMsg:
            iniFile.addKeyValue(section, import_option, "1")
        else:
            iniFile.addKeyValue(section, import_option, "0")

    except Exception as e:
        logFile.logErr(str(e))

    # 测试最后复制log出来
    iniFile.setSection("EndFlag")
    iniFile.addKeyValue("EndFlag", "flag", "end")
    logFile.logInfo("*****测试结束********")
    fileOperate.copyFile("%s/%s" % (appRunPath, Config.testDirectory), commFunc.getExternalStorageAbsolutePath())
