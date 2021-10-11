#!/usr/bin/env python
# -*- coding: utf-8 -*-

# \~chinese 設備類型定義    \~english Device Type Definition
MV_UNKNOW_DEVICE                             = 0x00000000  # < \~chinese 未知設備類型，保留意義       \~english Unknown Device Type, Reserved
MV_GIGE_DEVICE                               = 0x00000001  # < \~chinese GigE設備                     \~english GigE Device
MV_1394_DEVICE                               = 0x00000002  # < \~chinese 1394-a/b 設備                \~english 1394-a/b Device
MV_USB_DEVICE                                = 0x00000004  # < \~chinese USB 設備                     \~english USB Device
MV_CAMERALINK_DEVICE                         = 0x00000008  # < \~chinese CameraLink設備               \~english CameraLink Device

INFO_MAX_BUFFER_SIZE                         = 64          # < \~chinese 最大的數據信息大小           \~english Maximum data information size

MV_MAX_TLS_NUM                               = 8           # < \~chinese 最多支援的傳輸層實例個數     \~english The maximum number of supported transport layer instances
MV_MAX_DEVICE_NUM                            = 256         # < \~chinese 最大支援的設備個數           \~english The maximum number of supported devices

MV_MAX_GENTL_IF_NUM                          = 256         # < \~chinese 最大支援的GenTL數量          \~english The maximum number of GenTL supported
MV_MAX_GENTL_DEV_NUM                         = 256         # < \~chinese 最大支援的GenTL設備數量      \~english The maximum number of GenTL devices supported

# \~chinese 設備的訪問模式    \~english Device Access Mode
# \~chinese 獨佔權限，其他APP隻允許讀CCP寄存器                        \~english Exclusive authority, other APP is only allowed to read the CCP register
MV_ACCESS_Exclusive                          = 1
# \~chinese 可以從5模式下搶佔權限，然後以獨佔權限打開                 \~english You can seize the authority from the 5 mode, and then open with exclusive authority
MV_ACCESS_ExclusiveWithSwitch                = 2
# \~chinese 控製權限，其他APP允許讀所有寄存器                         \~english Control authority, allows other APP reading all registers
MV_ACCESS_Control                            = 3
# \~chinese 可以從5的模式下搶佔權限，然後以控製權限打開               \~english You can seize the authority from the 5 mode, and then open with control authority
MV_ACCESS_ControlWithSwitch                  = 4
# \~chinese 以可被搶佔的控製權限打開                                  \~english Open with seized control authority
MV_ACCESS_ControlSwitchEnable                = 5
# \~chinese 可以從5的模式下搶佔權限，然後以可被搶佔的控製權限打開     \~english You can seize the authority from the 5 mode, and then open with seized control authority
MV_ACCESS_ControlSwitchEnableWithKey         = 6
# \~chinese 讀模式打開設備，適用於控製權限下                          \~english Open with read mode and is available under control authority
MV_ACCESS_Monitor                            = 7

MV_MATCH_TYPE_NET_DETECT                     = 0x00000001  # < \~chinese 網路流量和丟包信息              \~english Network traffic and packet loss information
MV_MATCH_TYPE_USB_DETECT                     = 0x00000002  # < \~chinese host接收到來自U3V設備的字節總數 \~english The total number of bytes host received from U3V device

# \~chinese GigEVision IP配置    \~english GigEVision IP Configuration
MV_IP_CFG_STATIC                             = 0x05000000  # < \~chinese 靜態         \~english Static
MV_IP_CFG_DHCP                               = 0x06000000  # < \~chinese DHCP         \~english DHCP
MV_IP_CFG_LLA                                = 0x04000000  # < \~chinese LLA          \~english LLA

# \~chinese GigEVision網路傳輸模式    \~english GigEVision Net Transfer Mode
MV_NET_TRANS_DRIVER                          = 0x00000001  # < \~chinese 驅動         \~english Driver
MV_NET_TRANS_SOCKET                          = 0x00000002  # < \~chinese Socket       \~english Socket

# \~chinese CameraLink波特率    \~english CameraLink Baud Rates (CLUINT32)
MV_CAML_BAUDRATE_9600                        = 0x00000001  # < \~chinese 9600         \~english 9600
MV_CAML_BAUDRATE_19200                       = 0x00000002  # < \~chinese 19200        \~english 19200
MV_CAML_BAUDRATE_38400                       = 0x00000004  # < \~chinese 38400        \~english 38400
MV_CAML_BAUDRATE_57600                       = 0x00000008  # < \~chinese 57600        \~english 57600
MV_CAML_BAUDRATE_115200                      = 0x00000010  # < \~chinese 115200       \~english 115200
MV_CAML_BAUDRATE_230400                      = 0x00000020  # < \~chinese 230400       \~english 230400
MV_CAML_BAUDRATE_460800                      = 0x00000040  # < \~chinese 460800       \~english 460800
MV_CAML_BAUDRATE_921600                      = 0x00000080  # < \~chinese 921600       \~english 921600
MV_CAML_BAUDRATE_AUTOMAX                     = 0x40000000  # < \~chinese 最大值       \~english Auto Max

# \~chinese 異常消息類型    \~english Exception message type
MV_EXCEPTION_DEV_DISCONNECT                  = 0x00008001  # < \~chinese 設備斷開連接              \~english The device is disconnected
MV_EXCEPTION_VERSION_CHECK                   = 0x00008002  # < \~chinese SDK與驅動版本不匹配       \~english SDK does not match the driver version

MAX_EVENT_NAME_SIZE                          = 128         # < \~chinese 設備Event事件名稱最大長度 \~english Max length of event name
MV_MAX_XML_SYMBOLIC_NUM                      = 64          # \~chinese 最大XML符號數               \~english Max XML Symbolic Number
