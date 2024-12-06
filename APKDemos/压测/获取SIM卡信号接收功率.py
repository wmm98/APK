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
    # logFile.logInfo("root 设备")
    # if commFunc.enableSetGet(testApi.setAppRootEnable(OSApiConstants.ABLE_TYPE_ENABLE), testApi.getAppRootEnable()):
    #     pass
    #     logFile.logInfo("root 成功")
    # else:
    #     logFile.logErr("root 失败")

    testApi.setAppRootEnable(OSApiConstants.ABLE_TYPE_ENABLE), testApi.getAppRootEnable()

    """
    0 dBm 至 -10 dBm: 极强的信号，通常表示设备非常接近无线接入点（如路由器）。在这个范围内，信号强度非常高，通信质量非常好，通常会达到最大传输速率。
    -10 dBm 至 -30 dBm: 非常强的信号，通信质量非常好，传输速率非常高。
    -30 dBm 至 -50 dBm: 强信号，通信质量良好，传输速率高。
    -50 dBm 至 -60 dBm: 较强信号，通信质量良好，通常可以达到较高的传输速率。
    -60 dBm 至 -70 dBm: 中等信号，通信质量一般，可能会有一些轻微的干扰或传输速率下降。
    -70 dBm 至 -80 dBm: 信号较弱，可能会出现一些通信不稳定或传输速率下降。
    -80 dBm 至 -90 dBm: 信号非常弱，通信可能会不稳定，数据传输速度极低。
    -90 dBm 以下: 信号极其弱，可能无法建立稳定连接或数据传输速度极低。
    """

    sim_0 = testApi.getSimRSRP(0)
    sim_1 = testApi.getSimRSRP(1)

    logFile.logInfo("卡槽1的SIM卡信号接收功率为：%s dBm" % str(sim_0))
    logFile.logInfo("卡槽2的SIM卡信号接收功率为：%s dBm" % str(sim_1))

    # 测试最后复制log出来
    iniFile.setSection("EndFlag")
    iniFile.addKeyValue("EndFlag", "flag", "end")
    # logFile.logInfo("*****测试结束********")
    fileOperate.copyFile("%s/%s" % (appRunPath, Config.testDirectory), commFunc.getExternalStorageAbsolutePath())
