from ppadb.client import Client as AdbClient
import time
import cv2,os
import subprocess
import numpy as np


def getDevice():
    # Default is "127.0.0.1" and 5037
    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()
    if (len(devices) < 0):
        print("0 device")
        return 0

    return devices[0]
device = getDevice()
def __init__(self,emulator):
    self.emulator= emulator
def get_screen():
     os.system(f'adb -s {self.emulator} exec-out screencap -p > {name}.png')
get_screen()

#def screenShot():
   # sc=device.screencap("2.mp4", "/sdcard/2.mp4")
   # return sc
def  findel():
    # 'cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED'
    method = cv2.TM_CCOEFF_NORMED

    # Đọc file ảnh
    small_image = cv2.imread('iconFB.png')
    sc=device.screencap('sc.png','D:\autotool\sc.png')
   
    large_image = cv2.imread(sc)

    result = cv2.matchTemplate(small_image, large_image, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    return min_val, max_val, min_loc, max_loc 
    print(min_val, max_val, min_loc, max_loc)

print(device)
findel()


