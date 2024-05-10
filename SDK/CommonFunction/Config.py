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
    waitSetRespTime = 2

    projectPath = os.getcwd()
    # print("Config path:", projectPath)
    logFilePath = os.path.join(projectPath, testDirectory, automationLog)
    iniFilePath = os.path.join(projectPath, testDirectory, actualResultFileName)
    screenShotPath = os.path.join(projectPath, testDirectory, screenShotDirectory)
