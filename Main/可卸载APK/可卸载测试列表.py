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

    logFile.logInfo("*****可卸载APK测试开始********")
    try:
        # com.xzr.La.hotter com.bjw.ComAssistant
        # 获可防卸载的包
        shell.SendCommand("cat %s | grep uninstall_enable" % (commFunc.getIniFilePath()))
        expPackagesUninstallEnable = shell.successMsg
        logFile.logInfo("预期的可卸载列表为： %s" % expPackagesUninstallEnable)
        # 防卸载列表
        shell.SendCommand("cat %s | grep uninstall_disable" % (commFunc.getIniFilePath()))
        expPackagesUninstallDisable = shell.successMsg
        logFile.logInfo("预期的防卸载列表为：%s" % expPackagesUninstallDisable)

        # 获取防止卸载package列表
        UninstallablePackages = testApi.getAppUninstallable().strip()

        # 添加
        section = "Application"
        iniFile.setSection(section)
        # logFile.logInfo("%s ： %s" % (option, launcherName))

        if expPackagesUninstallEnable:
            logFile.logInfo("系统显示的防卸载列表为：%s" % UninstallablePackages)
            expPackagesUninstallEnableList = expPackagesUninstallEnable.split("=")[1].split(";")[:-1]
            for package in expPackagesUninstallEnableList:
                if package not in expPackagesUninstallDisable:
                    # 去卸载apk
                    result = testApi.unInstallApp(package)
                    if testApi.unInstallApp(package) == OSApiErrorCode.STATUS_SUCCESS:
                        logFile.logInfo("应用%s可卸载， 测试成功并且不在防卸载列表里" % package)
                        iniFile.addKeyValue(section, package, "pass")
                    else:
                        logFile.logErr("应用%s不可卸载， 测试失败, 返回码%s， 补充信息为： %s" % (package, str(result["mResult"]), result["mResultMessage"]))
                        iniFile.addKeyValue(section, package, "fail")
                else:
                    logFile.logErr("应用%s在防卸载列表里面， 请检查！！！" % package)
                    iniFile.addKeyValue(section, package, "fail")
        else:
            logFile.logErr("没有设置可卸载应用， 请检查！！！")
    except Exception as e:
        logFile.logErr(str(e))

    # 测试最后复制log出来
    iniFile.setSection("EndFlag")
    iniFile.addKeyValue("EndFlag", "flag", "end")
    logFile.logInfo("*****测试结束********")
    fileOperate.copyFile("%s/%s" % (appRunPath, Config.testDirectory), commFunc.getExternalStorageAbsolutePath())
