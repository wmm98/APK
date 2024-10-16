from jnius import autoclass
from SDK.OSApi.OSApi import OSApi
from SDK.OSApi.OSAPiShell import OSAPiShell
from SDK.OSApi.MyShell import My_Shell
from SDK.OSApi.OSApiConstants import OSApiConstants
from SDK.OSApi.OSApiErrorCode import OSApiErrorCode
from SDK.CommonFunction.IntegrateFunction import CommFunction
from SDK.CommonFunction.OperateFile import OperateFile
from SDK.CommonFunction.OperateFile import OutPutTestResult, OutPutIniResult
from SDK.CommonFunction.Config import Config
from SDK.CommonFunction.Page.BaseCaseFunction import BaseFunction
from kivy.app import App
import sys
from kivy.app import App
from jnius import autoclass
import os
import time

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
    baseFunc = BaseFunction()
    myShell = My_Shell()

    # 创建存放测试结果的目录， 创建存放测试数据的文件,初始化后在sdcard/TestTeam的路径下
    logFile.logInfo("root 设备")
    if commFunc.enableSetGet(testApi.setAppRootEnable(OSApiConstants.ABLE_TYPE_ENABLE), testApi.getAppRootEnable()):
        print("root成功")
        logFile.logInfo("root 成功")
    else:
        print("root失败")
        logFile.logErr("root 失败")

    logFile.logInfo("*********U盘识别测试试开始********")
    try:
        flag = 0
        fileOperate.echoInfo("/sdcard/usb.txt", "")
        print("***********************")
        while True:
            while True:
                result = myShell.Exec_command(["ls /storage"], True, True)
                fileOperate.appendInfo("/sdcard/usb.txt", "%s" % ",".join(result.success_msg))
                # print(shell.SendCommand("ls /storage"))
                print("result:", result.result)
                print("success message:", result.success_msg)
                if len(result.success_msg) > 2:
                    print("到这里来")
                    flag += 1
                    fileOperate.appendInfo("/sdcard/usb.txt", "识别成功%d次" % flag)
                    break
                    # fileOperate.echoInfo("/sdcard/usb.txt", "")
                time.sleep(0.3)

            while True:
                result = myShell.Exec_command(["ls /storage"], True, True)
                fileOperate.appendInfo("/sdcard/usb.txt", "%s" % ",".join(result.success_msg))
                # print(shell.SendCommand("ls /storage"))
                print("result:", result.result)
                print("success message:", result.success_msg)
                if len(result.success_msg) == 2:
                    print("到这里来")
                    flag += 1
                    fileOperate.appendInfo("/sdcard/usb.txt", "U盘断开状态")
                    break
                    # fileOperate.echoInfo("/sdcard/usb.txt", "")
                time.sleep(0.3)
    except Exception as e:
        print(e)
        logFile.logErr(e)

    # 测试最后复制log出来
    # iniFile.setSection("EndFlag")
    # iniFile.addKeyValue("EndFlag", "flag", "end")
    # logFile.logInfo("*****测试结束********")
    # fileOperate.copyFile("%s/%s" % (appRunPath, Config.testDirectory), commFunc.getExternalStorageAbsolutePath())
