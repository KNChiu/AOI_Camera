# -- coding: utf-8 --
import sys
import _tkinter
import tkinter.messagebox
# import tkinter as tk
import sys, os

from cv2 import error
# from tkinter import ttk
# sys.path.append("../MvImport")
# from MvImport import *
# from MvCameraControl_class import *

from MvImport.MvCameraControl_class import *
from CamOperation_class import *

# from CamOperation_class import *


#获取选取设备信息的索引，通过[]之间的字符去解析
def TxtWrapBy(start_str, end, all):
    start = all.find(start_str)
    if start >= 0:
        start += len(start_str)
        end = all.find(end, start)
        if end >= 0:
            return all[start:end].strip()

#将返回的错误码转换为十六进制显示
def ToHexStr(num):
    chaDic = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
    hexStr = ""
    if num < 0:
        num = num + 2**32
    while num >= 16:
        digit = num % 16
        hexStr = chaDic.get(digit, str(digit)) + hexStr
        num //= 16
    hexStr = chaDic.get(num, str(num)) + hexStr   
    return hexStr


class CameraAPI():
    def __init__(self):
        # global deviceList 
        self.deviceList = MV_CC_DEVICE_INFO_LIST()
        # global tlayerType
        self.tlayerType = MV_GIGE_DEVICE | MV_USB_DEVICE
        # global cam
        self.cam = MvCamera()
        # global nSelCamIndex
        self.nSelCamIndex = 0
        # global obj_cam_operation
        self.obj_cam_operation = 0
        # global b_is_run
        self.b_is_run = False

    #绑定下拉列表至设备信息索引
    # def xFunc(self, event):
    #     # global nSelCamIndex
    #     self.nSelCamIndex = TxtWrapBy("[","]",device_list.get())

    # ch:列出可用相機 | en:enum devices
    def enum_devices(self):
        while True:
            try:
                self.deviceList = MV_CC_DEVICE_INFO_LIST()
                self.tlayerType = MV_GIGE_DEVICE | MV_USB_DEVICE
                ret = self.cam.MV_CC_EnumDevices(self.tlayerType, self.deviceList)
                if ret != 0:
                    # tkinter.messagebox.showerror('show error','enum devices fail! ret = '+ ToHexStr(ret))
                    print('error :', str(ret))
                    time.sleep(0.5)
                    continue

                if self.deviceList.nDeviceNum == 0:
                    # tkinter.messagebox.showinfo('show info','find no device!')
                    print('error :', "there is no device!")
                    time.sleep(0.5)
                    continue

                print ("Find %d devices!" % self.deviceList.nDeviceNum)

                devList = []
                for i in range(0, self.deviceList.nDeviceNum):
                    mvcc_dev_info = cast(self.deviceList.pDeviceInfo[i], POINTER(MV_CC_DEVICE_INFO)).contents
                    if mvcc_dev_info.nTLayerType == MV_GIGE_DEVICE:
                        print ("\ngige device: [%d]" % i)
                        strModeName = ""
                        for per in mvcc_dev_info.SpecialInfo.stGigEInfo.chModelName:
                            strModeName = strModeName + chr(per)
                        print ("device model name: %s" % strModeName)

                        nip1 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0xff000000) >> 24)
                        nip2 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x00ff0000) >> 16)
                        nip3 = ((mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x0000ff00) >> 8)
                        nip4 = (mvcc_dev_info.SpecialInfo.stGigEInfo.nCurrentIp & 0x000000ff)
                        print ("current ip: %d.%d.%d.%d\n" % (nip1, nip2, nip3, nip4))
                        devList.append("Gige["+str(i)+"]:"+str(nip1)+"."+str(nip2)+"."+str(nip3)+"."+str(nip4))
                    elif mvcc_dev_info.nTLayerType == MV_USB_DEVICE:
                        print ("\nu3v device: [%d]" % i)
                        strModeName = ""
                        for per in mvcc_dev_info.SpecialInfo.stUsb3VInfo.chModelName:
                            if per == 0:
                                break
                            strModeName = strModeName + chr(per)
                        print ("device model name: %s" % strModeName)

                        strSerialNumber = ""
                        for per in mvcc_dev_info.SpecialInfo.stUsb3VInfo.chSerialNumber:
                            if per == 0:
                                break
                            strSerialNumber = strSerialNumber + chr(per)
                        print ("user serial number: %s" % strSerialNumber)
                        devList.append("USB["+str(i)+"]"+str(strSerialNumber))
                
                break

            except Exception as e:
                print("error :", e)
                time.sleep(0.5)
                continue


    # ch:開啟相機 | en:open device
    def open_device(self):
        while True:
            try:
                if True == self.b_is_run:
                    # tkinter.messagebox.showinfo('show info','Camera is Running!')
                    return

                self.obj_cam_operation = CameraOperation(self.cam,self.deviceList,self.nSelCamIndex)
                ret = self.obj_cam_operation.Open_device()
                
                if  0!= ret:
                    self.b_is_run = False
                    print('error :', str(ret))
                    time.sleep(0.5)
                    continue
                else:
                    self.b_is_run = True

            except Exception as e:
                print("error :", e)
                time.sleep(0.5)
                continue
                    

    # ch:開始串流 | en:Start grab image
    def start_grabbing(self):
        self.obj_cam_operation.Start_grabbing()

    # 取得影像的 numpy格式
    def get_img_nummpy(self):
        return self.obj_cam_operation.get_img_nummpy()

    # ch:停止串流 | en:Stop grab image
    def stop_grabbing(self):
        # global obj_cam_operation
        self.obj_cam_operation.Stop_grabbing()    

    # ch:關閉設備 | Close device   
    def close_device(self):
        # global b_is_run
        # global obj_cam_operation
        self.obj_cam_operation.Close_device()
        self.b_is_run = False 

    #ch:# 將影像存成BMP檔案 | en:save bmp image
    def bmp_save(self, save_path, save_name):
        # global obj_cam_operation
        self.obj_cam_operation.save_path = save_path
        self.obj_cam_operation.save_name = save_name
        self.obj_cam_operation.b_save_bmp = True

if __name__ == "__main__":
    CameraAPI = CameraAPI()
    CameraAPI.enum_devices()
    print("enum_devices")
    time.sleep(0.1)

    CameraAPI.open_device()
    print("open_device")
    time.sleep(0.5)

    CameraAPI.start_grabbing()
    print("start_grabbing")
    time.sleep(0.5)

    cv2.namedWindow("showIMG",0)
    cv2.resizeWindow("showIMG", 500, 500) 
    
    while True:
        numArray = CameraAPI.get_img_nummpy()
        if numArray is None:
            pass
        else:
            cv2.imshow("showIMG", numArray)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break
            elif key & 0xFF == ord('s'):
                CameraAPI.bmp_save(save_path = r"./CameraAPI/SaveBMP", save_name = "123")
                print("bmp_save")
                time.sleep(0.1)


    CameraAPI.stop_grabbing()
    print("stop_grabbing")
    time.sleep(0.1)

    CameraAPI.close_device()
    print("close_device")
    time.sleep(0.1)

    print("finish")
    