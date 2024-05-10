import os
import time
from jnius import autoclass
from SDK.CommonFunction.Config import Config
from SDK.OSApi.OSAPiShell import OSAPiShell

shell = OSAPiShell()


Environment = autoclass('android.os.Environment')


class BaseInterface:
    def __init__(self):
        pass

    def timeSleep(self, seconds):
        time.sleep(seconds)

    def getCurrentPath(self):
        return os.getcwd()

    def chDirPath(self, path):
        os.chdir(path)

    def chRootPath(self):
        os.path.expanduser('~')

    def getExternalStorageAbsolutePath(self):
        return Environment.getExternalStorageDirectory().getAbsolutePath()


