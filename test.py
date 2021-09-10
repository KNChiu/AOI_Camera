import time
import cv2
from AOI_Camera import CameraAPI

if __name__ == "__main__":
    # CameraAPI = CameraAPI()

    # CameraAPI.enum_devices()        # 列出可用相機
    # print("enum_devices")
    # time.sleep(0.1)

    # CameraAPI.open_device()         # 開啟相機
    # print("open_device")        
    # time.sleep(0.5)

    # CameraAPI.start_grabbing()      # 開始串流
    # print("start_grabbing")
    # time.sleep(0.5)

    # 建立一個顯示畫面
    # cv2.namedWindow("showIMG",0)
    # cv2.resizeWindow("showIMG", 500, 500) 

    while True:
        AOICameraAPI = CameraAPI()

        AOICameraAPI.enum_devices()        # 列出可用相機
        print("enum_devices")
        time.sleep(0.1)

        AOICameraAPI.open_device()         # 開啟相機
        print("open_device")        
        time.sleep(0.5)

        AOICameraAPI.start_grabbing()      # 開始串流
        print("start_grabbing")
        time.sleep(0.5)

        AOICameraAPI.enum_devices()        # 列出可用相機
        print("enum_devices")
        time.sleep(0.1)


        AOICameraAPI.open_device()         # 開啟相機
        print("open_device")        
        time.sleep(0.5)

        AOICameraAPI.start_grabbing()      # 開始串流
        print("start_grabbing")
        time.sleep(0.5)
        isConnect = True

        while True:
            numArray = AOICameraAPI.get_img_nummpy()   # 取得影像的
            # print(numArray)
            time.sleep(0.5)
            

            if numArray is None:
                print("None")
                if isConnect == False:
                    break
                else:
                    time.sleep(3)
                    isConnect = False
                    continue
            else:
                isConnect = True
                print("not None")

    # cnt = 0
    # while True:
        # if numArray is None:
        #     pass
        # else:
        #     cv2.imshow("showIMG", numArray)
        #     key = cv2.waitKey(1)
        #     if key & 0xFF == ord('q'):
                
        #         break
        #     elif key & 0xFF == ord('s'):
        #         nameList = ['Tr_1_G', 'Tr_2_G', 'Tr_1_NG', 'Tr_2_NG']
        #         CameraAPI.bmp_save(save_path = r"SaveBMP", save_name = nameList[cnt])   # 將影像存成BMP檔案
        #         cnt += 1
        #         print("bmp_save")
        #         time.sleep(0.1)

    cv2.destroyAllWindows()             # 釋放

    CameraAPI.stop_grabbing()           # 停止串流
    print("stop_grabbing")
    time.sleep(0.1)

    CameraAPI.close_device()            # 關閉設備
    print("close_device")
    time.sleep(0.1)

    print("finish")