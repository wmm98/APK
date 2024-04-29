from .PublicApi import TelApi
from jnius import autoclass

arrayList = autoclass('java.util.ArrayList')


class OSApi(TelApi):
    def __init__(self, osApi):
        # pass
        TelApi.__init__(self, osApi)

    def setAppRootEnable(self, enable):
        return self.getSystemControl().setAppRootEnable(enable)

    def getAppRootEnable(self):
        return self.getSystemControl().getAppRootEnable()

    def setWifiEnable(self, enable):
        return self.getSystemControl().setWifiEnable(enable)

    def getWifiEnable(self):
        return self.getSystemControl().getWifiEnable()

    def setBluetoothEnable(self, enable):
        return self.getSystemControl().setBluetoothEnable(enable)

    def getBluetoothEnable(self):
        return self.getSystemControl().getBluetoothEnable()

    def setLocationEnable(self, enable):
        return self.getSystemControl().setLocationEnable(enable)

    def getLocationEnable(self):
        return self.getSystemControl().getLocationEnable()

    def setEthernetEnable(self, enable):
        return self.getSystemControl().setEthernetEnable(enable)

    def getEthernetEnable(self):
        return self.getSystemControl().getEthernetEnable()

    def setMobileDataEnable(self, enable):
        return self.getSystemControl().setMobileDataEnable(enable)

    def getMobileDataEnable(self):
        return self.getSystemControl().getMobileDataEnable()

    def setWifiApEnable(self, enable):
        return self.getSystemControl().setWifiApEnable(enable)

    def getWifiApEnable(self):
        return self.getSystemControl().getWifiApEnable()

    def setLockScreenEnable(self, enable):
        return self.getSystemControl().setLockScreenEnable(self, enable)

    def getLockScreenEnable(self):
        return self.getSystemControl().getLockScreenEnable()

    def setAutoTimeEnable(self, enable):
        return self.getSystemControl().setAutoTimeEnable(enable)

    def getAutoTimeEnable(self):
        return self.getSystemControl().getAutoTimeEnable()

    def setAutoTimeZoneEnable(self, enable):
        return self.getSystemControl().setAutoTimeZoneEnable(enable)

    def getAutoTimeZoneEnable(self):
        return self.getSystemControl().getAutoTimeZoneEnable()

    def setScreenRecordEnable(self, enable):
        return self.getSystemControl().setScreenRecordEnable(enable)

    def getScreenRecordEnable(self):
        return self.getSystemControl().getScreenRecordEnable()

    def setKeyEnable(self, keyType, enable):
        # 设置按键开关接口,详细参数参照API文档
        """

        :param keyType:
                        key_type_menu 目录键
                        key_type_back 返回键
                        key_type_recent 最近运行键
                        key_type_home Home键
                        key_type_volume_up 音量上键
                        key_type_volume_down 音量下键
                        key_type_function 功能键
        :param enable:
        :return:
        """
        return self.getSystemControl().setKeyEnable(keyType, enable)

    def getKeyEnable(self, keyType):
        return self.getSystemControl().getKeyEnable(keyType)

    def setSettings(self, SettingsType, name, value):
        # SettingsType 指得是 settings list system 中得system 表. name, value 代表要设置的键值对
        return self.getSystemControl().setSettings(SettingsType, name, value)

    def getSettings(self, SettingsType, name):
        # 返回Settings value
        return self.getSystemControl().getSettings(SettingsType, name)

    def setSystemStreamVolumeConfigure(self, StreamType, level):
        """
        :param StreamType:
                           AudioManager.STREAM_VOICE_CALL 通话音量
                           AudioManager.STREAM_SYSTEM 系统音量
                           STREAM_TYPE_MUSIC AudioManager.STREAM_MUSIC 多媒体音量
                           STREAM_TYPE_ALARM AudioManager.STREAM_ALARM 闹钟音量
        :param level: (eg:0~100)
        :return:

        Usage:
             meta_cls = autoclass("android.media.AudioManager")
             meta = meta_cls(context)
             setSystemStreamVolumeConfigure(meta.AudioManager.STREAM_VOICE_CALL, 10)
        """
        return self.getSystemControl().setSystemStreamVolumeConfigure(self, StreamType, level)

    def getSystemStreamVolumeConfigure(self, StreamType):
        return self.getSystemControl().getSystemStreamVolumeConfigure(StreamType)

    def setWifiConfiguration(self, OsWifiConfiguration):
        # 暂时用不到， OsWifiConfiguration为实例化的类，详细参照接口源码
        return self.getSystemControl().setWifiConfiguration(OsWifiConfiguration)

    def setWifiApConfiguration(self, apName, password):
        # 暂时用不到, 详细参照接口源码
        return self.getSystemControl().setWifiApConfiguration(apName, password)

    def setScreenOffTimeoutConfiguration(self, ScreenOffTimeout):
        return self.getSystemControl().setScreenOffTimeoutConfiguration(ScreenOffTimeout)

    def getScreenOffTimeoutConfiguration(self):
        return self.getSystemControl().getScreenOffTimeoutConfiguration()

    def setLanguageConfiguration(self, language):
        """
        :param language: zh_CN en_US
        :return:
        """
        return self.getSystemControl().setLanguageConfiguration(language)

    def getLanguageConfiguration(self):
        return self.getSystemControl().getLanguageConfiguration()

    def setTimeZoneConfiguration(self, timeZone):
        """
        :param timeZone: Asia/Shanghai
        :return:
        """
        return self.getSystemControl().setTimeZoneConfiguration(timeZone)

    def getTimeZoneConfiguration(self):
        return self.getSystemControl().getTimeZoneConfiguration()

    def setExternalModelConfiguration(self, name):
        return self.getSystemControl().setExternalModelConfiguration(name)

    def getExternalModelConfiguration(self):
        return self.getSystemControl().getExternalModelConfiguration()

    def setManufacturerConfiguration(self, name):
        return self.getSystemControl().setManufacturerConfiguration(name)

    def getManufacturerConfiguration(self):
        return self.getSystemControl().getManufacturerConfiguration()

    def shutdown(self):
        return self.getSystemControl().shutdown()

    def reboot(self):
        return self.getSystemControl().reboot()

    def wipeData(self):
        return self.getSystemControl().wipeData()

    def wakeup(self):
        return self.getSystemControl().wakeup()

    def sleep(self):
        return self.getSystemControl().sleep()

    def setNfcEnable(self, enable):
        return self.getSystemControl().setNfcEnable(enable)

    def getNfcEnable(self):
        return self.getSystemControl().getNfcEnable()

    def doScreenCapture(self, displayId, path):
        return self.getSystemControl().doScreenCapture(displayId, path)

    def setAirplaneModeEnable(self, enable):
        return self.setAirplaneModeEnable(enable)

    def getAirplaneModeEnable(self):
        return self.getSystemControl().getAirplaneModeEnable()

    def setGoogleServiceEnable(self, enable):
        return self.getApplicationControl().setGoogleServiceEnable(enable)

    def getGoogleServiceEnable(self):
        return self.getApplicationControl().getGoogleServiceEnable()

    def setAppEnable(self, packageName, enable):
        return self.getApplicationControl().setAppEnable(packageName, enable)

    def setDeviceOwner(self, admin):
        return self.getApplicationControl().setDeviceOwner(admin)

    def setKioskEnable(self, packageName, enable):
        return self.getApplicationControl().setKioskEnable(packageName, enable)

    def getKioskEnable(self, packageName):
        return self.getApplicationControl().getKioskEnable(packageName)

    def startAppKeepAlive(self, componentName):
        return self.getApplicationControl().startAppKeepAlive(componentName)

    def stopAppKeepAlive(self):
        return self.getApplicationControl().stopAppKeepAlive()

    def setLauncher(self, launcher):
        return self.getApplicationControl().setLauncher(launcher)

    def getLauncher(self):
        """
        :return:launcher package name
        """
        return self.getSystemControl().getLauncher()

    def installApk(self, apkFilePath):
        return self.getApplicationControl().installApk(apkFilePath)

    def unInstallApp(self, packageName):
        return self.getApplicationControl().unInstallApp(packageName)

    def setAppInstallBlackList(self, packageName):
        return self.getSystemControl().setAppInstallBlackList(packageName)

    def getAppInstallBlackList(self):
        """

        :return: return String
        """
        return self.getSystemControl().getAppInstallBlackList()

    def setAppUninstallable(self, packageName):
        # 设置应用防卸载列表
        return self.getApplicationControl().setAppUninstallable(packageName)

    def getAppUninstallable(self):
        return self.getApplicationControl().getAppUninstallable()

    def setSystemAppDisable(self, packageName):
        return self.getApplicationControl().setSystemAppDisable(packageName)

    def getSystemAppsDisable(self):
        return self.getApplicationControl().getSystemAppsDisable()

    def setDeviceAdminEnable(self, admin, enable):
        return self.getApplicationControl().setDeviceAdminEnable(admin, enable)

    def getDeviceAdminEnable(self, admin):
        return self.getApplicationControl().getDeviceAdminEnable(admin)

    def setAppUpperPermission(self, t_type, packageName, enable):
        """
        :param t_type:
        :param packageName:
        :param enable:
        type 可以在ApiConstants 查询
        OP_SYSTEM_ALERT_WINDOW 24 显示再其他应用上层
        OP_WRITE_SETTINGS 23 修改系统设置
        OP_REQUEST_INSTALL_PACKAGES 66 安装未知应用
        :return:
        """
        return self.getApplicationControl().setAppUpperPermission(t_type, packageName, enable)

    def setBootLogo(self, path):
        return self.getDisplayControl().setBootLogo(path)

    def setBootAnimation(self, path):
        return self.getApplicationControl().setBootAnimation(path)

    def setWallPaper(self, path):
        return self.getApplicationControl().setWallPaper(path)

    def setBrightness(self, level):
        # 0~255
        return self.getApplicationControl().setBrightness(level)

    def getBrightness(self):
        return self.getDisplayControl().getBrightness()

    def setFontSize(self, size):
        """

        :param size: size：字体大小{eg:0,1,2,3}
        :return:
        """
        return self.getDisplayControl().setFontSize(size)

    def getFontSize(self):
        return self.getDisplayControl().getFontSize()

    def setQsTiles(self, tiles):
        """

        :param titles: 快捷选项{eg: wifi,bt}
        :return:
        """
        return self.getDisplayControl().setQsTiles(tiles)

    def getQsTiles(self):
        return self.getDisplayControl().getQsTiles()

    def setBatteryPercentEnable(self, enable):
        return self.getDisplayControl().setBatteryPercentEnable()

    def getBatteryPercentEnable(self):
        return self.getDisplayControl().getBatteryPercentEnable()

    def setStatusbarEnable(self, enable):
        # 设置状态栏显示
        return self.getDisplayControl().setStatusbarEnable(enable)

    def getStatusbarEnable(self):
        # 获取状态栏显示
        return self.getDisplayControl().getStatusbarEnable()

    def setStatusbarDropEnable(self, enable):
        # 设置状态栏下拉状态
        return self.getDisplayControl().setStatusbarDropEnable(enable)

    def getStatusbarDrop(self):
        # 获取状态栏下拉状态
        return self.getDisplayControl().getStatusbarDrop()

    def setNavigationBarEnable(self, enable):
        return self.getDisplayControl().setNavigationBarEnable(enable)

    def getNavigationBarEnable(self):
        return self.getDisplayControl().getNavigationBarEnable()

    def getDeviceModel(self):
        # 获取设备的型号信息
        return self.getDisplayControl().getDeviceModel()

    def getProductModel(self):
        # 获取产品型号
        return self.getDisplayControl().getProductModel()

    def getSerialNumber(self):
        return self.getDisplayControl().getSerialNumber()

    def getBuildNumber(self):
        return self.getDisplayControl().getBuildNumber()

    def getBaseband(self):
        return self.getDisplayControl().getBaseband()

    def getIMEI(self, slot):
        # : 卡道（eg：0，1）
        return self.getDisplayControl().getIMEI(slot)

    def getMEID(self, slot):
        # : 卡道（eg：0，1）
        return self.getDisplayControl().getMEID(slot)

    def getBootloader(self):
        # 获取设备SP的bootloader信息
        return self.getDisplayControl().getBootloader()

    def getSecurityOS(self):
        # 获取设备SP的OS信息
        return self.getDisplayControl().getSecurityOS()

    def getBootWizard(self):
        # 获取开机向导版本
        return self.getDisplayControl().getBootWizard()

    def getCurrentNetWorkType(self):
        """

        :return: {eg:"unknown","ethernet","wifi","2G","3G","4G"]
        """
        return self.getDisplayControl().getCurrentNetWorkType()

    def getSimSignalStrength(self, slot):
        # 获取信号强度等级（只包含SIM卡）
        return self.getDisplayControl().getSimSignalStrength(slot)

    def getSimRSRP(self, slot):
        # 获取信号接收功率（只包含SIM卡）
        return self.getDisplayControl().getSimRSRP(slot)

    def getSimRSSINR(self, slot):
        # 获取信号与干扰噪声比（只包含SIM卡）
        return self.getDisplayControl().getSimRSSINR(slot)

    def getSimPCI(self):
        # getSimPCI
        return self.getDisplayControl().getSimPCI()

    def getSimSignalCoverageLevel(self):
        # 获取无线信号覆盖等级（只包含SIM卡）
        return self.getDisplayControl().getSimSignalCoverageLevel()

    def getSimCellLocationInfo(self):
        # 获取小区位置信息（只包含SIM卡）
        return self.getDisplayControl().getSimCellLocationInfo()

    def getEthernetMac(self):
        return self.getDisplayControl().getEthernetMac()

    def getWifiMac(self):
        return self.getDisplayControl().getWifiMac()

    def getBluetoothMac(self):
        return self.getDisplayControl().getBluetoothMac()

    def getBatteryStatus(self):
        # 获取电池状态
        return self.getDisplayControl().getBatteryStatus()

    def getBatteryLevel(self):
        # 获取电池当前电量
        return self.getDisplayControl().getBatteryLevel()

    def getMemorySize(self):
        """

        :return: int
        """
        return self.getDisplayControl().getMemorySize()

    def getStorageSize(self):
        """

        :return: int
        """
        return self.getDisplayControl().getStorageSize()

    def getMemoryUsage(self):
        """

        :return: float
        """
        return self.getDisplayControl().getMemoryUsage()

    def getStorageUsage(self):
        # 获取存储使用率
        return self.getDisplayControl().getStorageUsage()

    def getTotalCpuUsage(self):
        # 获取总CPU使用率
        return self.getDisplayControl().getTotalCpuUsage()

    def getCpuTemperature(self):
        """

        :return: float
        """
        return self.getDisplayControl().getCpuTemperature()

    def getUsbDevices(self):
        """

        :return: # 获取接入的USB设备
        """
        return self.getDisplayControl().getUsbDevices()

    def getScreenInfo(self, screenId):
        return self.getDisplayControl().getScreenInfo(screenId)

    def setIpAddressBlackList(self, blackList):
        # 重启后黑名设置的失效
        # 创建一个空的 Java ArrayList 对象
        java_list = arrayList()
        # Python 列表
        # 将 Python 列表中的元素添加到 Java ArrayList 中
        for item in blackList:
            java_list.add(item)
        return self.getNetworkControl().setIpAddressBlackList(java_list)

    def getIpAddressBlackList(self):
        return list(self.getDisplayControl().getIpAddressBlackList())

    def clearIpAddressBlackList(self):
        return self.getNetworkControl().clearIpAddressBlackList()

    def setIpAddressWhiteList(self, whiteList):
        # 重启后黑名设置的失效
        # 创建一个空的 Java ArrayList 对象
        java_list = arrayList()
        # Python 列表
        # 将 Python 列表中的元素添加到 Java ArrayList 中
        for item in whiteList:
            java_list.add(item)
        return self.getNetworkControl().setIpAddressWhiteList(java_list)

    def getIpAddressWhiteList(self):
        return list(self.getDisplayControl().getIpAddressWhiteList())

    def clearIpAddressWhiteList(self):
        return self.getNetworkControl().clearIpAddressWhiteList()

    def queryTotalDataTraffic(self, networkType, startTime, endTime):
        """

        :param networkType: DATA_TRAFFIC_TYPE_MOBILE, DATA_TRAFFIC_TYPE_WIFI
        :param startTime: 精确到毫秒
        :param endTime:
        :return:
        """
        return self.getNetworkControl().queryTotalDataTraffic(networkType, startTime, endTime)

    def queryAllAppDataTraffic(self, networkType, startTime, endTime):
        dict_res = self.getNetworkControl().queryAllAppDataTraffic(networkType, startTime, endTime)
        python_dict = {}
        for entry in dict_res.entrySet():
            python_dict[str(entry.getKey())] = entry.getValue()
        return python_dict

    def copyFile(self, srcPath, destPath):
        return self.getMiscControl().copyFile(srcPath, destPath)

    def setBootStartupApp(self, packageName):
        # 开机启动应用的包名
        return self.getMiscControl().setBootStartupApp(packageName)

    def setLockScreenPassword(self, password):
        return self.getMiscControl().setLockScreenPassword(password)

    def clearLockScreenPassword(self):
        return self.getMiscControl().clearLockScreenPassword()

    def dataTransmissionCheck(self):
        return self.getMiscControl().dataTransmissionCheck()

    def startLogCollect(self, minute):
        return self.getMiscControl().startLogCollect(minute)

    def stopLogCollect(self):
        return self.getMiscControl().stopLogCollect()

    def getAttestationKey(self):
        # 认证密钥编号
        return self.getMiscControl().getAttestationKey()

    def setAttestationKey(self, fileName):
        return self.getMiscControl().setAttestationKey(fileName)

    def getServerVersion(self):
        # osapi服务端版本
        return self.getCommonControl().getServerVersion()

    def getClientVersion(self):
        # osapi客户端版本（sdk版本）
        return self.getCommonControl().getClientVersion()
