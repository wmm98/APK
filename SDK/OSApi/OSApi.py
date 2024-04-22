from .PublicApi import TelApi


class OSApi(TelApi):
    def __init__(self, osApi):
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

    def setWifiApConfiguration(self, apName,  password):
        # 暂时用不到, 详细参照接口源码
        return self.getSystemControl().setWifiApConfiguration(apName, password)

    def setScreenOffTimeoutConfiguration(self, ScreenOffTimeout):
        return self.getSystemControl().setScreenOffTimeoutConfiguration(ScreenOffTimeout)