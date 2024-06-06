from jnius import autoclass
from SDK.OSApi.OSApi import OSApi
from SDK.OSApi.OSAPiShell import OSAPiShell
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

    # 创建存放测试结果的目录， 创建存放测试数据的文件,初始化后在sdcard/TestTeam的路径下
    logFile.logInfo("root 设备")
    if commFunc.enableSetGet(testApi.setAppRootEnable(OSApiConstants.ABLE_TYPE_ENABLE), testApi.getAppRootEnable()):
        logFile.logInfo("root 成功")
    else:
        logFile.logErr("root 失败")

    logFile.logInfo("****音量设置与功能测试开始********")
    section = Config.section_volume
    iniFile.setSection(section)
    set_volume = 0
    try:
        option = Config.option_stream_music
        if not commFunc.enableSet(testApi.setSystemStreamVolumeConfigure(OSApiConstants.STREAM_TYPE_MUSIC, set_volume)):
            logFile.logErr("无法修改媒体音量值")
        logFile.logInfo("媒体音量修改成功")
        commFunc.waitSetResponse()
        mediaCurrentVolumeValue = testApi.getSystemStreamVolumeConfigure(OSApiConstants.STREAM_TYPE_MUSIC)
        logFile.logInfo("当前的媒体音量为：%d" % mediaCurrentVolumeValue)
        if mediaCurrentVolumeValue >= 0:
            iniFile.addKeyValue(section, option, str(mediaCurrentVolumeValue))
        else:
            iniFile.addKeyValue(section, option, baseFunc.dealOSErrCode(mediaCurrentVolumeValue))
    except Exception as e:
        logFile.logErr(str(e))

    try:
        option = Config.option_stream_voice_call
        if not commFunc.enableSet(testApi.setSystemStreamVolumeConfigure(OSApiConstants.STREAM_TYPE_VOICE_CALL, set_volume)):
            logFile.logErr("无法修改通话音量值")
        logFile.logInfo("通话音量修改成功")
        commFunc.waitSetResponse()
        voiceCallCurrentVolumeValue = testApi.getSystemStreamVolumeConfigure(OSApiConstants.STREAM_TYPE_VOICE_CALL)
        logFile.logInfo("当前的通话音量为：%d" % voiceCallCurrentVolumeValue)
        if voiceCallCurrentVolumeValue >= 0:
            iniFile.addKeyValue(section, option, str(voiceCallCurrentVolumeValue))
        else:
            iniFile.addKeyValue(section, option, baseFunc.dealOSErrCode(voiceCallCurrentVolumeValue))
    except Exception as e:
        logFile.logErr(str(e))

    try:
        option = Config.option_stream_alarm
        if not commFunc.enableSet(testApi.setSystemStreamVolumeConfigure(OSApiConstants.STREAM_TYPE_ALARM, set_volume)):
            logFile.logErr("无法修改闹钟音量值")
        logFile.logInfo("闹钟音量修改成功")
        commFunc.waitSetResponse()
        alarmCallCurrentVolumeValue = testApi.getSystemStreamVolumeConfigure(OSApiConstants.STREAM_TYPE_ALARM)
        logFile.logInfo("当前alarm音量为： %d" % alarmCallCurrentVolumeValue)
        if alarmCallCurrentVolumeValue >= 0:
            iniFile.addKeyValue(section, option, str(alarmCallCurrentVolumeValue))
        else:
            iniFile.addKeyValue(section, option, baseFunc.dealOSErrCode(alarmCallCurrentVolumeValue))
    except Exception as e:
        logFile.logErr(str(e))

    try:
        option = Config.option_stream_system
        if not commFunc.enableSet(testApi.setSystemStreamVolumeConfigure(OSApiConstants.STREAM_TYPE_SYSTEM, set_volume)):
            logFile.logErr("无法修改系统音量值")
        logFile.logInfo("系统音量修改成功")
        commFunc.waitSetResponse()
        systemCallCurrentVolumeValue = testApi.getSystemStreamVolumeConfigure(OSApiConstants.STREAM_TYPE_SYSTEM)
        logFile.logInfo("当前system音量为： %d" % systemCallCurrentVolumeValue)
        if systemCallCurrentVolumeValue >= 0:
            iniFile.addKeyValue(section, option, str(systemCallCurrentVolumeValue))
        else:
            iniFile.addKeyValue(section, option, baseFunc.dealOSErrCode(systemCallCurrentVolumeValue))
    except Exception as e:
        logFile.logErr(str(e))

    # 测试最后复制log出来
    iniFile.setSection("EndFlag")
    iniFile.addKeyValue("EndFlag", "flag", "end")
    logFile.logInfo("*****测试结束********")
    fileOperate.copyFile("%s/%s" % (appRunPath, Config.testDirectory), commFunc.getExternalStorageAbsolutePath())
