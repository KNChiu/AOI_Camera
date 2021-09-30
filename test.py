import time
import cv2
from AOI_Camera import CameraAPI

AOICameraAPI = CameraAPI()
# AOICameraAPI.fast_gradding()
havecamera = AOICameraAPI.enum_devices()        # 列出可用相機
time.sleep(0.1)
if havecamera:
    AOICameraAPI.open_device()         # 開啟相機
    time.sleep(0.5)

    AOICameraAPI.start_grabbing()      # 開始串流
    time.sleep(0.5)

    cv2.namedWindow("showIMG",0)
    cv2.resizeWindow("showIMG", 500, 500) 

    while True:
        numArray = AOICameraAPI.get_img_nummpy()
        if numArray is None:
            pass
        else:
            cv2.imshow("showIMG", numArray)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break
            elif key & 0xFF == ord('s'):
                AOICameraAPI.bmp_save(save_path = r"./SaveBMP", save_name = "123")
                print("bmp_save")
                time.sleep(0.1)


    AOICameraAPI.stop_grabbing()
    print("stop_grabbing")
    time.sleep(0.1)

    AOICameraAPI.close_device()
    print("close_device")
    time.sleep(0.1)

print("finish")

