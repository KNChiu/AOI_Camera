import time
import cv2
from AOI_Camera import CameraAPI

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
    cnt = 0
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
                nameList = ['Tr_1_G', 'Tr_2_G', 'Tr_1_NG', 'Tr_2_NG']
                CameraAPI.bmp_save(save_path = r"SaveBMP", save_name = nameList[cnt])
                cnt += 1
                print("bmp_save")
                time.sleep(0.1)


    CameraAPI.stop_grabbing()
    print("stop_grabbing")
    time.sleep(0.1)

    CameraAPI.close_device()
    print("close_device")
    time.sleep(0.1)

    print("finish")