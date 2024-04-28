# """
# 封装log方法
#
# """
#
# import logging
# import os
# import time
# import sys
# from .Config import Config
# from jnius import autoclass
#
#
# class GetApkRunPath:
#     def __init__(self, getPath):
#         self.getDefaultPath = getPath
#
#
# LEVELS = {
#     'debug': logging.DEBUG,
#     'info': logging.INFO,
#     'warning': logging.WARNING,
#     'error': logging.ERROR,
#     'critical': logging.CRITICAL
# }
# # level = 'error'
# level = 'info'
# logger = logging.getLogger()
#
#
# def create_file(filename):
#     fd = open(filename, mode='w', encoding='utf-8')
#     fd.close()
#
#
# def set_handler(levels):
#     if levels == 'error':
#         logger.addHandler(MyLog.err_handler)
#     logger.addHandler(MyLog.handler)
#
#
# def remove_handler(levels):
#     if levels == 'error':
#         logger.removeHandler(MyLog.err_handler)
#     logger.removeHandler(MyLog.handler)
#
#
# def get_current_time():
#     return time.strftime(MyLog.date, time.localtime(time.time()))
#
#
# class MyLog:
#     # 返回上级目录
#     # ?
#     logger.setLevel(LEVELS.get(level, logging.NOTSET))
#
#     # 将自定义的过滤器添加到日志记录器中
#
#     # create_file(Config.actualResultFileName)
#     create_file(GetApkRunPath().)
#     date = '%Y-%m-%d %H:%M:%S'
#
#     handler = logging.FileHandler(Config.automationLog, encoding='utf-8')
#     err_handler = logging.FileHandler(Config.automationLog, encoding='utf-8')
#
#     @staticmethod
#     def debug(log_meg):
#         set_handler('debug')
#         logger.debug("[DEBUG " + get_current_time() + "]" + log_meg)
#         remove_handler('debug')
#         print("[DEBUG " + get_current_time() + "]" + log_meg, flush=True)
#
#     @staticmethod
#     def info(log_meg):
#         # 强制刷新标准输出流，确保及时输出
#         set_handler('info')
#         logger.info("[INFO " + get_current_time() + "]" + log_meg)
#         remove_handler('info')
#         print("[INFO " + get_current_time() + "]" + log_meg, flush=True)
#
#     @staticmethod
#     def warning(log_meg):
#         set_handler('warning')
#         logger.warning("[WARNING " + get_current_time() + "]" + log_meg)
#         remove_handler('warning')
#         print("[WARNING " + get_current_time() + "]" + log_meg, flush=True)
#
#     @staticmethod
#     def error(log_meg):
#         set_handler('error')
#         logger.error("[ERROR " + get_current_time() + "]" + log_meg)
#         remove_handler('error')
#         print("[ERROR " + get_current_time() + "]" + log_meg, flush=True)
#
#     @staticmethod
#     def critical(log_meg):
#         set_handler('critical')
#         logger.error("[CRITICAL " + get_current_time() + "]" + log_meg)
#         remove_handler('critical')
#         print("[CRITICAL " + get_current_time() + "]" + log_meg, flush=True)
#
#
# class OutPutIni:
#     # 返回上级目录
#     # path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     # log的目录，日志目录
#     filename = log_path + '/CatchLogs/output.txt'
#     # filename D:\GNP\GNP_StablilityTest/Log/log.log    D:\GNP\GNP_StablilityTest/Log/err.log
#     # path D:\GNP\GNP_StablilityTest/Log
#     path = filename[0:filename.rfind('/')]
#     # 判断是否为文件夹
#     if not os.path.isdir(path):
#         os.makedirs(path)
#     # 判读是否为文件
#     elif not os.path.isfile(filename):
#         fd = open(filename, mode='w', encoding='utf-8')
#         fd.close()
#     elif 'output.txt' in filename:
#         os.rename(filename, path + '/output' + time.strftime("%Y-%m-%d_%H_%M_%S") + '.txt')
#         fd = open(filename, mode='w', encoding='utf-8')
#         fd.close()
#
#     @staticmethod
#     def write_text(msg):
#         # ("[WARNING " + get_current_time() + "]" + log_meg)
#         date = '%Y-%m-%d %H:%M:%S'
#         filename = log_path + '/CatchLogs/output.txt'
#         f = open(filename, 'a+', encoding='utf-8')
#         f.write(msg + '\n')
#         f.close()
#
#
# if __name__ == "__main__":
#     MyLog.debug("This is debug message")
#     MyLog.info("This is info message")
#     MyLog.warning("This is warning message")
#     MyLog.error("This is error")
#     MyLog.critical("This is critical message")
#     # MyLog()
#
#     # output = OutPutText()
#     # output.write_text("这是什么\n")
#     # output.write_text("这是在调试11111")
