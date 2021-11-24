#!/usr/bin/env python
# -*- coding: utf-8 -*-

MV_OK                                        = 0x00000000  # < \~chinese 成功，無錯誤             \~english Successed, no error

# 通用錯誤碼定義:範圍0x80000000-0x800000FF
MV_E_HANDLE                                  = 0x80000000  # < \~chinese 錯誤或無效的句柄         \~english Error or invalid handle
MV_E_SUPPORT                                 = 0x80000001  # < \~chinese 不支援的功能             \~english Not supported function
MV_E_BUFOVER                                 = 0x80000002  # < \~chinese 緩存已滿                 \~english Buffer overflow
MV_E_CALLORDER                               = 0x80000003  # < \~chinese 函數調用順序錯誤         \~english Function calling order error
MV_E_PARAMETER                               = 0x80000004  # < \~chinese 錯誤的參數               \~english Incorrect parameter
MV_E_RESOURCE                                = 0x80000006  # < \~chinese 資源申請失敗             \~english Applying resource failed
MV_E_NODATA                                  = 0x80000007  # < \~chinese 無數據                   \~english No data
MV_E_PRECONDITION                            = 0x80000008  # < \~chinese 前置條件有誤，或運行環境已發生變化       \~english Precondition error, or running environment changed
MV_E_VERSION                                 = 0x80000009  # < \~chinese 版本不匹配               \~english Version mismatches
MV_E_NOENOUGH_BUF                            = 0x8000000A  # < \~chinese 傳入的記憶體空間不足       \~english Insufficient memory
MV_E_ABNORMAL_IMAGE                          = 0x8000000B  # < \~chinese 異常圖像，可能是丟包導緻圖像不完整       \~english Abnormal image, maybe incomplete image because of lost packet
MV_E_LOAD_LIBRARY                            = 0x8000000C  # < \~chinese 動態導入DLL失敗          \~english Load library failed
MV_E_NOOUTBUF                                = 0x8000000D  # < \~chinese 冇有可輸出的緩存         \~english No Avaliable Buffer
MV_E_UNKNOW                                  = 0x800000FF  # < \~chinese 未知的錯誤               \~english Unknown error

# GenICam係列錯誤:範圍0x80000100-0x800001FF
MV_E_GC_GENERIC                              = 0x80000100  # < \~chinese 通用錯誤                 \~english General error
MV_E_GC_ARGUMENT                             = 0x80000101  # < \~chinese 參數非法                 \~english Illegal parameters
MV_E_GC_RANGE                                = 0x80000102  # < \~chinese 值超出範圍               \~english The value is out of range
MV_E_GC_PROPERTY                             = 0x80000103  # < \~chinese 屬性                     \~english Property
MV_E_GC_RUNTIME                              = 0x80000104  # < \~chinese 運行環境有問題           \~english Running environment error
MV_E_GC_LOGICAL                              = 0x80000105  # < \~chinese 邏輯錯誤                 \~english Logical error
MV_E_GC_ACCESS                               = 0x80000106  # < \~chinese 節點訪問條件有誤         \~english Node accessing condition error
MV_E_GC_TIMEOUT                              = 0x80000107  # < \~chinese 超時                     \~english Timeout
MV_E_GC_DYNAMICCAST                          = 0x80000108  # < \~chinese 轉換異常                 \~english Transformation exception
MV_E_GC_UNKNOW                               = 0x800001FF  # < \~chinese GenICam未知錯誤          \~english GenICam unknown error

# GigE_STATUS對應的錯誤碼:範圍0x80000200-0x800002FF
MV_E_NOT_IMPLEMENTED                         = 0x80000200  # < \~chinese 命令不被設備支援         \~english The command is not supported by device
MV_E_INVALID_ADDRESS                         = 0x80000201  # < \~chinese 訪問的目標地址不存在     \~english The target address being accessed does not exist
MV_E_WRITE_PROTECT                           = 0x80000202  # < \~chinese 目標地址不可寫           \~english The target address is not writable
MV_E_ACCESS_DENIED                           = 0x80000203  # < \~chinese 設備無訪問權限           \~english No permission
MV_E_BUSY                                    = 0x80000204  # < \~chinese 設備忙，或網路斷開       \~english Device is busy, or network disconnected
MV_E_PACKET                                  = 0x80000205  # < \~chinese 網路包數據錯誤           \~english Network data packet error
MV_E_NETER                                   = 0x80000206  # < \~chinese 網路相關錯誤             \~english Network error
MV_E_IP_CONFLICT                             = 0x80000221  # < \~chinese 設備IP沖突               \~english Device IP conflict

# USB_STATUS對應的錯誤碼:範圍0x80000300-0x800003FF
MV_E_USB_READ                                = 0x80000300  # < \~chinese 讀usb出錯               \~english Reading USB error
MV_E_USB_WRITE                               = 0x80000301  # < \~chinese 寫usb出錯               \~english Writing USB error
MV_E_USB_DEVICE                              = 0x80000302  # < \~chinese 設備異常                \~english Device exception
MV_E_USB_GENICAM                             = 0x80000303  # < \~chinese GenICam相關錯誤         \~english GenICam error
MV_E_USB_BANDWIDTH                           = 0x80000304  # < \~chinese 帶寬不足  該錯誤碼新增   \~english Insufficient bandwidth, this error code is newly added
MV_E_USB_DRIVER                              = 0x80000305  # < \~chinese 驅動不匹配或者未裝驅動   \~english Driver mismatch or unmounted drive
MV_E_USB_UNKNOW                              = 0x800003FF  # < \~chinese USB未知的錯誤           \~english USB unknown error

# 升級時對應的錯誤碼:範圍0x80000400-0x800004FF
MV_E_UPG_FILE_MISMATCH                       = 0x80000400  # < \~chinese 升級固件不匹配           \~english Firmware mismatches
MV_E_UPG_LANGUSGE_MISMATCH                   = 0x80000401  # < \~chinese 升級固件語言不匹配       \~english Firmware language mismatches
MV_E_UPG_CONFLICT                            = 0x80000402  # < \~chinese 升級沖突（設備已經在升級了再次請求升級即返回此錯誤）   \~english Upgrading conflicted (repeated upgrading requests during device upgrade)
MV_E_UPG_INNER_ERR                           = 0x80000403  # < \~chinese 升級時設備內部出現錯誤   \~english Camera internal error during upgrade
MV_E_UPG_UNKNOW                              = 0x800004FF  # < \~chinese 升級時未知錯誤          \~english Unknown error during upgrade
