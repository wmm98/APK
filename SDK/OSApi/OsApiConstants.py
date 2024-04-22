from jnius import autoclass


class OsApiConstants:
    AbleType = autoclass('com.android.common.osapi.common.OsApiConstants$AbleType')
    KeyType = autoclass('com.android.common.osapi.common.OsApiConstants$KeyType')
    SettingsType = autoclass('com.android.common.osapi.common.OsApiConstants$SettingsType')
    StreamType = autoclass('com.android.common.osapi.common.OsApiConstants$StreamType')
    ScreenOffTimeout = autoclass('com.android.common.osapi.common.OsApiConstants$ScreenOffTimeout')
    BatteryStatus = autoclass('com.android.common.osapi.common.OsApiConstants$BatteryStatus')
    DataTrafficType = autoclass('com.android.common.osapi.common.OsApiConstants$DataTrafficType')
    AppOpPermissions = autoclass('com.android.common.osapi.common.OsApiConstants$AppOpPermissions')

    TelAbleType = AbleType()
    TelKeyType = KeyType()
    TelSettingsType = SettingsType()
    TelStreamType = StreamType()
    TelScreenOffTimeout = ScreenOffTimeout()
    TelBatteryStatus = BatteryStatus()
    TelDataTrafficType = DataTrafficType()
    TelAppOpPermissions = AppOpPermissions()
    # 使能/失使能
    ABLE_TYPE_DISABLE = TelAbleType.ABLE_TYPE_DISABLE
    ABLE_TYPE_ENABLE = TelAbleType.ABLE_TYPE_ENABLE
    # key type/按键类型常量
    KEY_TYPE_MENU = TelKeyType.KEY_TYPE_MENU
    KEY_TYPE_BACK = TelKeyType.KEY_TYPE_BACK
    KEY_TYPE_RECENT = TelKeyType.KEY_TYPE_RECENT
    KEY_TYPE_HOME = TelKeyType.KEY_TYPE_HOME
    KEY_TYPE_VOLUME_UP = TelKeyType.KEY_TYPE_VOLUME_UP
    KEY_TYPE_VOLUME_DOWN = TelKeyType.KEY_TYPE_VOLUME_DOWN
    # function key/功能键
    KEY_TYPE_FUNCTION = TelKeyType.KEY_TYPE_FUNCTION
    KEY_TYPE_POWER = TelKeyType.KEY_TYPE_POWER

    # {@link android.provider.Settings#Global 全局系统设置}，包含始终以相同方式应用于所有定义用户的首选项
    SETTINGS_TYPE_GLOBAL = TelSettingsType.SETTINGS_TYPE_GLOBAL
    # {@link android.provider.Settings#Secure 安全系统设置}，包含应用程序可以读取但不允许写入的系统首选项
    SETTINGS_TYPE_SECURE = TelSettingsType.SETTINGS_TYPE_SECURE
    # {@link android.provider.Settings#System 系统设置}，包含其他系统首选项
    SETTINGS_TYPE_SYSTEM = TelSettingsType.SETTINGS_TYPE_SYSTEM

    # 音量
    STREAM_TYPE_VOICE_CALL = TelStreamType.STREAM_TYPE_VOICE_CALL
    STREAM_TYPE_SYSTEM = TelStreamType.STREAM_TYPE_SYSTEM
    STREAM_TYPE_MUSIC = TelStreamType.STREAM_TYPE_MUSIC
    STREAM_TYPE_ALARM = TelStreamType.STREAM_TYPE_ALARM

    # 屏幕超时
    TIMEOUT_15_SECONDS = TelScreenOffTimeout.TIMEOUT_15_SECONDS
    TIMEOUT_30_SECONDS = TelScreenOffTimeout.TIMEOUT_30_SECONDS
    TIMEOUT_1_MINUTE = TelScreenOffTimeout.TIMEOUT_1_MINUTE
    TIMEOUT_2_MINUTES = TelScreenOffTimeout.TIMEOUT_2_MINUTES
    TIMEOUT_5_MINUTES = TelScreenOffTimeout.TIMEOUT_5_MINUTES
    TIMEOUT_10_MINUTES = TelScreenOffTimeout.TIMEOUT_10_MINUTES
    TIMEOUT_30_MINUTES = TelScreenOffTimeout.TIMEOUT_30_MINUTES
    TIMEOUT_NEVER = TelScreenOffTimeout.TIMEOUT_NEVER

    # 电池状态常量
    BATTERY_STATUS_DISCHARGING = TelBatteryStatus.BATTERY_STATUS_DISCHARGING
    BATTERY_STATUS_CHARGING = TelBatteryStatus.BATTERY_STATUS_CHARGING

    # 网络流量类型
    DATA_TRAFFIC_TYPE_MOBILE = TelDataTrafficType.DATA_TRAFFIC_TYPE_MOBILE
    DATA_TRAFFIC_TYPE_WIFI = TelDataTrafficType.DATA_TRAFFIC_TYPE_WIFI

    # app Op Permissions/应用高级权限
    OP_SYSTEM_ALERT_WINDOW = TelAppOpPermissions.OP_SYSTEM_ALERT_WINDOW
    OP_WRITE_SETTINGS = TelAppOpPermissions.OP_WRITE_SETTINGS
    OP_REQUEST_INSTALL_PACKAGES = TelAppOpPermissions.OP_REQUEST_INSTALL_PACKAGES


if __name__ == '__main__':
    print(OsApiConstants().TIMEOUT_2_MINUTES)
    print(type(OsApiConstants().TIMEOUT_2_MINUTES))
