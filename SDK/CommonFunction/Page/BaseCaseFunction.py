from SDK.CommonFunction.IntegrateFunction import CommFunction
from SDK.OSApi.OSAPiShell import OSAPiShell
from jnius import autoclass

shell = OSAPiShell()

runTime = autoclass('java.lang.Runtime')


class BaseFunction(CommFunction):
    def __init__(self):
        pass

    def getCpuCoresNum(self):
        cores = runTime.getRuntime().availableProcessors()
        return cores

    def currentCpuFrequency(self, cpu_no):
        cmd = "cat /sys/devices/system/cpu/cpu%d/cpufreq/cpuinfo_cur_freq" % cpu_no
        shell.SendCommand(cmd)
        return shell.successMsg

    def maxCpuFrequency(self, cpu_no):
        cmd = "cat /sys/devices/system/cpu/cpu%d/cpufreq/cpuinfo_max_freq" % cpu_no
        shell.SendCommand(cmd)
        return shell.successMsg

    def minCpuFrequency(self, cpu_no):
        cmd = "cat /sys/devices/system/cpu/cpu%d/cpufreq/cpuinfo_min_freq" % cpu_no
        shell.SendCommand(cmd)
        return shell.successMsg

    def currentUser(self):
        cmd = "getprop ro.build.type"
        shell.SendCommand(cmd)
        return shell.successMsg
