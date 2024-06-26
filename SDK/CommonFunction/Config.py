import os


class Config:
    testDirectory = "TestTeam"
    screenShotDirectory = "TestScreenShot"
    actualResultFileName = "TestResult.ini"
    automationLog = "AutomationTestLog.txt"
    expectResult = "ExpectResult"

    # 检查次数
    checkTimes = 3
    # 等待set 响应时间
    waitSetRespTime = 5
    waitGetResTime = 3

    projectPath = os.getcwd()
    # print("Config path:", projectPath)
    logFilePath = os.path.join(projectPath, testDirectory, automationLog)
    iniFilePath = os.path.join(projectPath, testDirectory, actualResultFileName)
    screenShotPath = os.path.join(projectPath, testDirectory, screenShotDirectory)

    # ini字段
    btn_open = "on"
    btn_off = "off"
    enable = "1"
    disable = "0"
    # 基础用例ini字段
    # section
    section_sys_default_settings = "SystemDefaultSettings"
    option_wifi = "wifi"
    option_eth0 = "eth0"
    option_gps = "location"
    option_mobile = "mobile"
    option_network_type = "network_type"
    option_bt = "bt"
    option_install_enable = "install_enable"
    option_stream_system = "stream_system"
    option_stream_music = "stream_music"
    option_stream_alarm = "stream_alarm"
    option_stream_voice_call = "stream_voice_call"
    option_brightness = "brightness"
    option_font_size = "size"
    option_screen_lock = "screen_lock"
    option_autosync = "autosync"
    option_autotimezone = "autotimezone"
    option_sleep_time = "sleep_time"
    # 音量section
    section_volume = "Volume"
    section_system_ui = "SystemUI"
    option_status_bar = "status_bar"
    option_navigation_bar = "navigation_bar"
    option_statusbar_drop = "statusbar_drop"

    section_language = "Language"
    option_language = "language"

    section_power = "Power"
    section_display = "Display"

    section_connection = "Connection"

    # 音量最大值，最小值
    min_volume = 0
    max_volume = 100

