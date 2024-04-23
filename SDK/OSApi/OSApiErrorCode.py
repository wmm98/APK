from jnius import autoclass


class OSApiErrorCode:
    ErrorCode = autoclass('com.android.common.osapi.OSApiErrorCode')
    ApiErrorCode = ErrorCode

    OK = ApiErrorCode.OK
    ERR_SYS_TIMEOUT = ApiErrorCode.ERR_SYS_TIMEOUT
    ERR_SYS_INVALID = ApiErrorCode.ERR_SYS_INVALID
    ERR_SYS_NO_DEV = ApiErrorCode.ERR_SYS_NO_DEV
    ERR_SYS_NO_INIT = ApiErrorCode.ERR_SYS_NO_INIT
    ERR_SYS_ALREADY_INIT = ApiErrorCode.ERR_SYS_ALREADY_INIT
    ERR_SYS_OVER_FLOW = ApiErrorCode.ERR_SYS_OVER_FLOW
    ERR_SYS_NOT_SUPPORT = ApiErrorCode.ERR_SYS_NOT_SUPPORT
    ERR_SYS_UNEXPECT = ApiErrorCode.ERR_SYS_UNEXPECT
    ERR_SYS_NO_PERMISSION = ApiErrorCode.ERR_SYS_NO_PERMISSION
    ERR_SYS_DATA_TRANSMIT = ApiErrorCode.ERR_SYS_DATA_TRANSMIT

    # /** 操作成功 */
# public final static int OK = 0;
#
# /**********************************系统共用错误**************************/
# /**操作超时*/
# public final static int ERR_SYS_TIMEOUT = -1;
# /**参数非法*/
# public final static int ERR_SYS_INVALID = -2;
# /** 设备未找到 */
# public final static int ERR_SYS_NO_DEV  = -3;
# /**设备或资源未初始化*/
# public final static int ERR_SYS_NO_INIT = -4;
# /**设备或资源已经初始化*/
# public final static int ERR_SYS_ALREADY_INIT = -5;
# /**缓存不足*/
# public final static int ERR_SYS_OVER_FLOW = -6;
# /**暂不支持*/
# public final static int ERR_SYS_NOT_SUPPORT = -7;
# /**未知错误 */
# public final static int ERR_SYS_UNEXPECT = -8;
# /**无权限访问*/
# public final static int ERR_SYS_NO_PERMISSION = -9;
# /** 通信失败 **/
# public final static int ERR_SYS_DATA_TRANSMIT = -10;


if __name__ == '__main__':
    print(OSApiErrorCode().ERR_SYS_ALREADY_INIT)