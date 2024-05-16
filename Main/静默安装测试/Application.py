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
from android.permissions import request_permissions, Permission
import os
import stat
import android

# from androguard.core.bytecodes.apk import APK
# from androguard.misc import APK
# from androguard.core.bytecodes.apk import APK

# sdk_version = android.os.Build.VERSION.SDK_INT
# if sdk_version >= 29:
#     print("sdk version大于29")
    # 申请权限
permissions = [Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE]
request_permissions(permissions)

from jnius import autoclass

# 导入需要的类
PythonActivity = autoclass('org.kivy.android.PythonActivity')
PackageManager = autoclass('android.content.pm.PackageManager')

# 获取当前应用程序的 Context
context = PythonActivity.mActivity.getApplicationContext()

# 获取 PackageManager
package_manager = context.getPackageManager()

# 获取当前应用程序的包名
package_name = context.getPackageName()

# 获取当前应用程序的 ApplicationInfo
app_info = package_manager.getApplicationInfo(package_name, PackageManager.GET_META_DATA)

# 获取当前应用程序的 AndroidManifest.xml 文件路径
manifest_path = app_info.sourceDir

# 打开 AndroidManifest.xml 文件
with open(manifest_path, 'r') as file:
    manifest_content = file.read()

# 将 android:requestLegacyExternalStorage="true" 添加到 <application> 标签中
manifest_content = manifest_content.replace('<application', '<application android:requestLegacyExternalStorage="true"')

# 保存修改后的 AndroidManifest.xml 文件
with open(manifest_path, 'w') as file:
    file.write(manifest_content)

print("AndroidManifest.xml 文件已成功修改。")


if __name__ == '__main__':

    Environment = autoclass('android.os.Environment')
    print("为 true，采用的是非分区存储方法： ", Environment.isExternalStorageLegacy())

    # request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Context = PythonActivity.mActivity
    packageName = Context.getApplicationContext().getPackageName()
    Api = autoclass('com.android.common.osapi.OSApi')
    testApi = OSApi(Api(Context))
    fileOperate = OperateFile()
    commFunc = CommFunction()
    shell = OSAPiShell()
    # 初始化测试结果文件相关

    # Manifest = autoclass("android.Manifest")
    # PackageManager = autoclass("android.content.pm.PackageManager")
    # ContextCompat = autoclass("androidx.core.content.ContextCompat")
    # if ContextCompat.checkSelfPermission(Context.getApplicationContext(), ):
    #     print("没有外部存储权限")

    ContextCompat = autoclass('androidx.core.content.ContextCompat')
    Manifest = autoclass('android.Manifest$permission')

    # 获取外部存储权限
    permissionWrite = ContextCompat.checkSelfPermission(Context.getApplicationContext(),
                                                        Manifest.WRITE_EXTERNAL_STORAGE)
    print("permissionWrite权限： ", permissionWrite)

    permissionRead = ContextCompat.checkSelfPermission(Context.getApplicationContext(),
                                                       Manifest.READ_EXTERNAL_STORAGE)
    print("Read_EXTERNAL_STORAGE： ", permissionWrite)

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

    logFile.logInfo("*****静默安装测试开始********")
    os.chdir("/sdcard/%s/%s" % (Config.expectResult, "tps900_config"))
    shell.SendCommand("ls")
    print(shell.successMsg)
    fileOperate.copyFile("tps900_config.ini", "/data/data/org.test.myapp/files/app")
    os.chdir("/data/data/org.test.myapp/files/app")
    externalStoragePath = commFunc.getExternalStorageAbsolutePath()
    expectResult = Config.expectResult
    configDireName = "tps900_config"
    os.chdir(os.path.join(externalStoragePath, expectResult, configDireName))
    print(os.getcwd())
    shell.SendCommand("ls | grep ini")
    print(shell.successMsg)
    File = autoclass('java.io.File')
    FileInputStream = autoclass('java.io.FileInputStream')
    InputStreamReader = autoclass('java.io.InputStreamReader')
    BufferedReader = autoclass('java.io.BufferedReader')
    file = File("tps900_config.ini")

    # try:
    # 创建FileInputStream对象
    file_input_stream = FileInputStream(file)

    # 创建InputStreamReader对象
    input_stream_reader = InputStreamReader(file_input_stream)

    # 创建BufferedReader对象
    buffered_reader = BufferedReader(input_stream_reader)

    # 读取文件内容
    line = buffered_reader.readLine()
    while line:
        line = buffered_reader.readLine()
        print(line)

    # 关闭流
    buffered_reader.close()
    input_stream_reader.close()
    file_input_stream.close()

    # print(os.listdir())
    # with open("tps900_config.ini", "r") as f:
    #     print(f.readline())

    # try:
    #     externalStoragePath = commFunc.getExternalStorageAbsolutePath()
    #     expectResult = Config.expectResult
    #     section = "Application"
    #     option = "quiet_install"
    #     iniFile.setSection(section)
    #     logFile.logInfo("静默安装测试")
    #     # 获取配置包包名
    #     shell.SendCommand("ls %s" % os.path.join(externalStoragePath, expectResult))
    #     configDireName = shell.successMsg.strip()
    #     print(configDireName)
    #     # 获取ini文件名字
    #     shell.SendCommand("ls %s | grep ini" % os.path.join(externalStoragePath, expectResult, configDireName))
    #     iniFileName = shell.successMsg.strip()
    #     # 获取静默安装的apk
    #     shell.SendCommand("cat %s | grep quiet_install" % (
    #         os.path.join(externalStoragePath, expectResult, configDireName, iniFileName)))
    #     origApks = shell.successMsg
    #     # 获取apk列表
    #     apks = origApks.split("=")[1].split(";")[:-1]
    #     print(apks)
    #     print("111111111111111111111111111111111111111")
    #     os.chdir(os.path.join(externalStoragePath, expectResult, configDireName))
    #     shell.SendCommand("ls")
    #     print(shell.successMsg)
    #     print("2222222222222222222222222")
    #     print(os.listdir())

        # # 替换为你的未安装 APK 文件路径
        # # apk_file_path = "/sdcard/ExpectResult/tps900_config/resources/apk/ComAssistant.apk"
        # # apk_file_path = os.path.join("resources/apk/ComAssistant.apk")
        # fileOperate.copyFile("resources/apk/ComAssistant.apk", appRunPath)
        # print("当前的路径：", os.getcwd())
        # # shell.SendCommand("ls")
        # # print(shell.successMsg)
        # # print(os.listdir())
        # # print(apk_file_path)
        # os.chdir(appRunPath)
        # shell.SendCommand("ls")
        # print(shell.successMsg)
        #
        # print(shell.SendCommand("aapt dump badging %s" % "ComAssistant.apk"))
        # print(shell.successMsg)
        # # apk = APK("ComAssistant.apk")
        # # print(apk)
        #
        # # 获取包名（Package Name）
        # # package_name = apk.get_package()
        #
        # print("2222222222222222222222222222222222222222222222")
        # # print("包名为： ", package_name)
        # print("333333333333333333333333333333333333333333333333")
        # if package_name:
        #     print("APK 文件的包名:", package_name)
        # else:
        #     print("无法获取 APK 文件的包名。")

        #
        # # sdExpectPath = os.path.join(commFunc.getExternalStorageAbsolutePath(), expectResult)
        # # print(os.listdir(os.path.join(expectResult, expectResult)))
        # # print(os.listdir(os.path.join(commFunc.getExternalStorageAbsolutePath(), expectResult)))
        # # print(os.listdir(appRunPath))
        # # launcherName = str(testApi.getLauncher())
        # # print("launcherName", launcherName)
        # # iniFile.addKeyValue(section, option, launcherName)
        # logFile.logInfo("%s ： %s" % (option, launcherName))
    # except Exception as e:
    #     logFile.logErr(str(e))

    # 测试最后复制log出来
    iniFile.setSection("EndFlag")
    iniFile.addKeyValue("EndFlag", "flag", "end")
    logFile.logInfo("*****测试结束********")
    fileOperate.copyFile("%s/%s" % (appRunPath, Config.testDirectory), commFunc.getExternalStorageAbsolutePath())
