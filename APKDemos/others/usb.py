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
import datetime

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
        # 测试前先捕捉log
        # myShell.Exec_command(["logcat > /sdcard/usb_logcat.txt &"], True, True)
        flag = 0
        usb_result = "/sdcard/usb_result.txt"
        write_data_txt = "usb_write_in.txt"
        fileOperate.echoInfo(usb_result, "")
        now = datetime.datetime.now()
        while True:
            flag += 1
            while True:
                result = myShell.Exec_command(["ls /mnt/media_rw"], True, True)
                usb_name = result.success_msg.strip()
                if len(result.success_msg) > 0:
                    cur_time = myShell.Exec_command(["date +%Y-%m-%d\ %H:%M:%S.%3N"], True, True).success_msg
                    fileOperate.appendInfo(usb_result, "%s: U盘插入%d次" % (cur_time, flag))
                    # 写入数据
                    fileOperate.echoInfo("/mnt/media_rw/%s/%s" % (usb_name, write_data_txt), "%d" % flag)
                    # 查询写入是否正确
                    usb_text = myShell.Exec_command(["cat /mnt/media_rw/%s/%s" % (usb_name, write_data_txt)], True,
                                                    True)
                    if "%d" % flag in usb_text.success_msg:
                        cur_success_write_time = myShell.Exec_command(["date +%Y-%m-%d\ %H:%M:%S.%3N"], True,
                                                                      True).success_msg
                        fileOperate.appendInfo(usb_result, "%s: 写入成功%d次" % (cur_success_write_time, flag))
                    else:
                        cur_fail_write_time = myShell.Exec_command(["date +%Y-%m-%d\ %H:%M:%S.%3N"], True,
                                                                   True).success_msg
                        fileOperate.appendInfo(usb_result, "%s: 写入失败%d次" % (cur_fail_write_time, flag))
                    break
                time.sleep(0.1)

            while True:
                result = myShell.Exec_command(["ls /mnt/media_rw"], True, True)
                if len(result.success_msg) == 0:
                    cur_time = myShell.Exec_command(["date +%Y-%m-%d\ %H:%M:%S.%3N"], True, True).success_msg
                    fileOperate.appendInfo(usb_result, "%s: U盘断开%d次" % (cur_time, flag))
                    break
                time.sleep(0.1)
            fileOperate.appendInfo(usb_result, "******压测%d次******" % flag)
    except Exception as e:
        print(e)
        logFile.logErr(str(e))

    # 测试最后复制log出来
    # iniFile.setSection("EndFlag")
    # iniFile.addKeyValue("EndFlag", "flag", "end")
    # logFile.logInfo("*****测试结束********")
    # fileOperate.copyFile("%s/%s" % (appRunPath, Config.testDirectory), commFunc.getExternalStorageAbsolutePath())
