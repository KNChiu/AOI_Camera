import time
import cv2
from AOI_Camera import CameraAPI


if __name__ == "__main__":
    cnt = 0
    gradding = True

    while gradding:
        AOICameraAPI = CameraAPI()
        # AOICameraAPI.fast_gradding()

        AOICameraAPI.enum_devices()
        print("enum_devices")
        time.sleep(0.1)

        AOICameraAPI.open_device()
        print("open_device")
        time.sleep(0.5)

        AOICameraAPI.start_grabbing()
        print("start_grabbing")
        time.sleep(0.5)

        isConnect = True
        cv2.namedWindow("showIMG",0)
        cv2.resizeWindow("showIMG", 500, 500) 

        while gradding:
            numArray = AOICameraAPI.get_img_nummpy()   # 取得影像的
            # print(numArray)
            time.sleep(0.5)
            
            if numArray is None:
                print("Camera disconnected")
                if isConnect == False:
                    break
                else:
                    time.sleep(3)
                    isConnect = False
                    continue
            else:
                isConnect = True

                cv2.imshow("showIMG", numArray)
                key = cv2.waitKey(1)
                if key & 0xFF == ord('q'):
                    gradding = False
                    break
                elif key & 0xFF == ord('s'):
                    nameList = ['Tr_1_G', 'Tr_2_G', 'Tr_1_NG', 'Tr_2_NG']
                    AOICameraAPI.bmp_save(save_path = r"SaveBMP", save_name = nameList[cnt])   # 將影像存成BMP檔案
                    cnt += 1
                    print("bmp_save")
                    time.sleep(0.1)
    else:
        cv2.destroyAllWindows()             # 釋放

        AOICameraAPI.stop_grabbing()           # 停止串流
        time.sleep(0.1)

        AOICameraAPI.close_device()            # 關閉設備
        time.sleep(0.1)
    print(gradding)
    print("finish")