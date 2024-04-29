from SDK.OSApi.OSAPiShell import OSAPiShell
import os
import time
import configparser
from SDK.CommonFunction.Config import Config

shell = OSAPiShell()


class OperateFile:
    def __init__(self):
        pass

    def shellCreateFile(self, fileName):
        shell.SendCommand("touch %s" % fileName)

    def echoInfo(self, fileName, info):
        # adb shell echo "Your message" > /path/to/your/file
        shell.SendCommand("echo %s > %s" % (info, fileName))

    def appendInfo(self, fileName, info):
        # adb shell echo "Your message" >> /path/to/your/file
        shell.SendCommand("echo info: %s >> %s" % (info, fileName))

    def appendErr(self, fileName, err):
        shell.SendCommand("echo err: %s >> %s" % (err, fileName))

    def removeFile(self, fileName):
        shell.SendCommand("rm %s" % fileName)

    def clearFileInfo(self, fileName):
        shell.SendCommand("echo "" > %s" % fileName)

    def createDirectory(self, direName):
        shell.SendCommand("mkdir %s" % direName)

    def deleteDirectory(self, direName):
        shell.SendCommand("rm -rf %s" % direName)

    def copyFile(self, source, destination):
        shell.SendCommand("cp -rf %s %s" % (source, destination))

    def osCreateDirectory(self, DireName):
        os.mkdir(DireName)


def get_current_time():
    dateStr = '%Y-%m-%d %H:%M:%S'
    return time.strftime(dateStr, time.localtime(time.time()))


class OutPutTestResult:
    def __init__(self, defaultPath):
        self.defaultPath = defaultPath
        self.testResultLogPath = ""

    def createFile(self, filename):
        filePath = os.path.join(self.defaultPath, Config.testDirectory, filename)
        self.testResultLogPath = filePath
        fd = open(filePath, "w")
        fd.close()

    def logInfo(self, msg):
        fd = open(self.testResultLogPath, "a+")
        fd.write("[INFO " + get_current_time() + "]" + msg + "\n")
        fd.close()

    def logErr(self, msg):
        fd = open(self.testResultLogPath, "a")
        fd.write("[ERROR " + get_current_time() + "]" + msg + "\n")
        fd.close()


class OutPutIniResult:
    config = configparser.ConfigParser()

    def __init__(self, defaultPath):
        self.defaultPath = defaultPath
        self.testResultIniPath = ""

    def createIniFile(self, fileName):
        self.testResultIniPath = os.path.join(self.defaultPath, Config.testDirectory, fileName)
        fd = open(self.testResultIniPath, "w")
        fd.close()

    def setSection(self, sectionName):
        self.config.add_section(sectionName)

    def addKeyValue(self, sectionName, key, value):
        self.config.set(sectionName, key, value)
        with open(self.testResultIniPath, 'w') as configfile:
            self.config.write(configfile)


