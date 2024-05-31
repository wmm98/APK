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

    logFile.logInfo("****系统默认设置测试开始********")
    try:
        iniFile.setSection(Config.section_sys_default_settings)
        logFile.logInfo("检查wifi状态")
        wifi_enable = testApi.getWifiEnable()
        if wifi_enable == OSApiConstants.ABLE_TYPE_ENABLE:
            iniFile.addKeyValue(Config.section_sys_default_settings, Config.option_wifi, Config.btn_open)
            logFile.logInfo("%s当前的状态：%s" % (Config.option_wifi, Config.btn_open))
        elif wifi_enable == OSApiConstants.ABLE_TYPE_DISABLE:
            iniFile.addKeyValue(Config.section_sys_default_settings, Config.option_wifi, Config.btn_off)
            logFile.logInfo("%s当前的状态：%s" % (Config.option_wifi, Config.btn_off))
        else:
            value = commFunc.dealOSErrCode(wifi_enable)
            logFile.logErr("%s当前的状态：%s" % (Config.option_wifi, value))
    except Exception as e:
        logFile.logErr(str(e))

    try:
        logFile.logInfo("检查以太网状态")
        eth_enable = testApi.getEthernetEnable()
        if eth_enable == OSApiConstants.ABLE_TYPE_ENABLE:
            iniFile.addKeyValue(Config.section_sys_default_settings, Config.option_eth0, Config.btn_open)
            logFile.logInfo("%s当前的状态：%s" % (Config.option_eth0, Config.btn_open))
        elif eth_enable == OSApiConstants.ABLE_TYPE_DISABLE:
            iniFile.addKeyValue(Config.section_sys_default_settings, Config.option_eth0, Config.btn_off)
            logFile.logInfo("%s当前的状态：%s" % (Config.option_eth0, Config.btn_off))
        else:
            value = commFunc.dealOSErrCode(eth_enable)
            logFile.logErr("%s当前的状态：%s" % (Config.option_eth0, value))
    except Exception as e:
        logFile.logErr(str(e))

    try:
        logFile.logInfo("检查蓝牙状态")
        bt_enable = testApi.getBluetoothEnable()
        if bt_enable == OSApiConstants.ABLE_TYPE_ENABLE:
            iniFile.addKeyValue(Config.section_sys_default_settings, Config.option_bt, Config.btn_open)
            logFile.logInfo("%s当前的状态：%s" % (Config.option_bt, Config.btn_open))
        elif bt_enable == OSApiConstants.ABLE_TYPE_DISABLE:
            iniFile.addKeyValue(Config.section_sys_default_settings, Config.option_eth0, Config.btn_off)
            logFile.logInfo("%s当前的状态：%s" % (Config.option_bt, Config.btn_off))
        else:
            value = commFunc.dealOSErrCode(bt_enable)
            logFile.logErr("%s当前的状态：%s" % (Config.option_bt, value))
    except Exception as e:
        logFile.logErr(str(e))

    try:
        logFile.logInfo("检查GPS状态")
        gps_enable = testApi.getLocationEnable()
        option = Config.option_gps
        if gps_enable == OSApiConstants.ABLE_TYPE_ENABLE:
            iniFile.addKeyValue(Config.section_sys_default_settings, option, Config.btn_open)
            logFile.logInfo("%s当前的状态：%s" % (option, Config.btn_open))
        elif gps_enable == OSApiConstants.ABLE_TYPE_DISABLE:
            iniFile.addKeyValue(Config.section_sys_default_settings, option, Config.btn_off)
            logFile.logInfo("%s当前的状态：%s" % (option, Config.btn_off))
        else:
            value = commFunc.dealOSErrCode(gps_enable)
            logFile.logErr("%s当前的状态：%s" % (option, value))
    except Exception as e:
        logFile.logErr(str(e))

    try:
        logFile.logInfo("检查移动数据开关状态")
        mobile_enable = testApi.getMobileDataEnable()
        option = Config.option_mobile
        if mobile_enable == OSApiConstants.ABLE_TYPE_ENABLE:
            iniFile.addKeyValue(Config.section_sys_default_settings, option, Config.btn_open)
            logFile.logInfo("%s当前的状态：%s" % (option, Config.btn_open))
        elif mobile_enable == OSApiConstants.ABLE_TYPE_DISABLE:
            iniFile.addKeyValue(Config.section_sys_default_settings, option, Config.btn_off)
            logFile.logInfo("%s当前的状态：%s" % (option, Config.btn_off))
        else:
            value = commFunc.dealOSErrCode(mobile_enable)
            logFile.logErr("%s当前的状态：%s" % (option, value))
    except Exception as e:
        logFile.logErr(str(e))

    try:
        logFile.logInfo("检查锁屏状态")
        lock_screen_enable = testApi.getLockScreenEnable()
        option = Config.option_screen_lock
        if lock_screen_enable == OSApiConstants.ABLE_TYPE_ENABLE:
            iniFile.addKeyValue(Config.section_sys_default_settings, option, Config.btn_open)
            logFile.logInfo("%s当前的状态：%s" % (option, Config.btn_open))
        elif lock_screen_enable == OSApiConstants.ABLE_TYPE_DISABLE:
            iniFile.addKeyValue(Config.section_sys_default_settings, option, Config.btn_off)
            logFile.logInfo("%s当前的状态：%s" % (option, Config.btn_off))
        else:
            value = commFunc.dealOSErrCode(lock_screen_enable)
            logFile.logErr("%s当前的状态：%s" % (option, value))
    except Exception as e:
        logFile.logErr(str(e))

    try:
        logFile.logInfo("检查时间同步按钮状态")
        time_sync_enable = testApi.getAutoTimeEnable()
        option = Config.option_autosync
        if time_sync_enable == OSApiConstants.ABLE_TYPE_ENABLE:
            iniFile.addKeyValue(Config.section_sys_default_settings, option, Config.btn_open)
            logFile.logInfo("%s当前的状态：%s" % (option, Config.btn_open))
        elif time_sync_enable == OSApiConstants.ABLE_TYPE_DISABLE:
            iniFile.addKeyValue(Config.section_sys_default_settings, option, Config.btn_off)
            logFile.logInfo("%s当前的状态：%s" % (option, Config.btn_off))
        else:
            value = commFunc.dealOSErrCode(time_sync_enable)
            logFile.logErr("%s当前的状态：%s" % (option, value))
    except Exception as e:
        logFile.logErr(str(e))

    try:
        logFile.logInfo("检查时区同步按钮状态")
        time_sync_zone_enable = testApi.getAutoTimeZoneEnable()
        option = Config.option_autotimezone
        if time_sync_zone_enable == OSApiConstants.ABLE_TYPE_ENABLE:
            iniFile.addKeyValue(Config.section_sys_default_settings, option, Config.btn_open)
            logFile.logInfo("%s当前的状态：%s" % (option, Config.btn_open))
        elif time_sync_zone_enable == OSApiConstants.ABLE_TYPE_DISABLE:
            iniFile.addKeyValue(Config.section_sys_default_settings, option, Config.btn_off)
            logFile.logInfo("%s当前的状态：%s" % (option, Config.btn_off))
        else:
            value = commFunc.dealOSErrCode(time_sync_zone_enable)
            logFile.logErr("%s当前的状态：%s" % (option, value))
    except Exception as e:
        logFile.logErr(str(e))

    try:
        logFile.logInfo("检查时默认的亮度")
        brightness = testApi.getBrightness()
        option = Config.option_brightness
        if brightness >= 0:
            iniFile.addKeyValue(Config.section_sys_default_settings, option, str(brightness))
            logFile.logInfo("%s当前的亮度：%s" % (option, str(brightness)))
        else:
            value = commFunc.dealOSErrCode(brightness)
            logFile.logErr("%s当前的亮度：%s" % (option, value))
    except Exception as e:
        logFile.logErr(str(e))

    try:
        logFile.logInfo("检查默认的休眠时间")
        screen_off_time_out = testApi.getScreenOffTimeoutConfiguration()
        option = Config.option_sleep_time
        if screen_off_time_out >= 0:
            iniFile.addKeyValue(Config.section_sys_default_settings, option, str(screen_off_time_out))
            logFile.logInfo("%s当前的休眠时间：%s" % (option, str(screen_off_time_out)))
        else:
            value = commFunc.dealOSErrCode(screen_off_time_out)
            logFile.logErr("%s当前的休眠时间：%s" % (option, value))
    except Exception as e:
        logFile.logErr(str(e))

    try:
        logFile.logInfo("检查当前的系统音量")
        system_volume = testApi.getSystemStreamVolumeConfigure(OSApiConstants.STREAM_TYPE_SYSTEM)
        option = Config.option_stream_system
        if system_volume >= 0:
            iniFile.addKeyValue(Config.section_sys_default_settings, option, str(system_volume))
            logFile.logInfo("%s当前的音量大小：%s" % (option, str(system_volume)))
        else:
            value = commFunc.dealOSErrCode(system_volume)
            logFile.logErr("%s获取的错误信息：%s" % (option, value))
    except Exception as e:
        logFile.logErr(str(e))

    try:
        logFile.logInfo("检查当前的闹钟音量")
        alarm_volume = testApi.getSystemStreamVolumeConfigure(OSApiConstants.STREAM_TYPE_ALARM)
        option = Config.option_stream_alarm
        if alarm_volume >= 0:
            iniFile.addKeyValue(Config.section_sys_default_settings, option, str(alarm_volume))
            logFile.logInfo("%s当前的音量大小：%s" % (option, str(alarm_volume)))
        else:
            value = commFunc.dealOSErrCode(alarm_volume)
            logFile.logErr("%s获取的错误信息：%s" % (option, value))
    except Exception as e:
        logFile.logErr(str(e))

    try:
        logFile.logInfo("检查当前的媒体音量")
        music_volume = testApi.getSystemStreamVolumeConfigure(OSApiConstants.STREAM_TYPE_MUSIC)
        option = Config.option_stream_music
        if music_volume >= 0:
            iniFile.addKeyValue(Config.section_sys_default_settings, option, str(music_volume))
            logFile.logInfo("%s当前的音量大小：%s" % (option, str(music_volume)))
        else:
            value = commFunc.dealOSErrCode(music_volume)
            logFile.logErr("%s获取的错误信息：%s" % (option, value))
    except Exception as e:
        logFile.logErr(str(e))

    try:
        logFile.logInfo("检查当前的通话音量")
        voice_call_volume = testApi.getSystemStreamVolumeConfigure(OSApiConstants.STREAM_TYPE_VOICE_CALL)
        option = Config.option_stream_voice_call
        if voice_call_volume >= 0:
            iniFile.addKeyValue(Config.section_sys_default_settings, option, str(voice_call_volume))
            logFile.logInfo("%s当前的音量大小：%s" % (option, str(voice_call_volume)))
        else:
            value = commFunc.dealOSErrCode(voice_call_volume)
            logFile.logErr("%s获取的错误信息：%s" % (option, value))
    except Exception as e:
        logFile.logErr(str(e))

    # 测试最后复制log出来
    iniFile.setSection("EndFlag")
    iniFile.addKeyValue("EndFlag", "flag", "end")
    logFile.logInfo("*****测试结束********")
    fileOperate.copyFile("%s/%s" % (appRunPath, Config.testDirectory), commFunc.getExternalStorageAbsolutePath())
