from inspect import Attribute
from math import fabs
from tkinter import W
import cv2,os
import numpy as np
class adb():
    def __init__(self,emulator):
        self.emulator= emulator
        
    def screenshot(self,name):
        os.system(f'adb -s {self.emulator} exec-out screencap -p > {name}')
    def click(self,x,y):
        os.system(f'adb -s {self.emulator} shell input tap {x} {y}')
    def find(self,target_pic_name='',template_pic_Name=False,threshold= 0.99):
        
        if template_pic_Name== False:
            self.screenshot(self.emulator+'.png')
            template_pic_Name=self.emulator+'.png'
        else:
            self.screenshot(template_pic_Name)
        icon_img= cv2.imread(target_pic_name,cv2.IMREAD_UNCHANGED)
        template_img= cv2.imread(template_pic_Name,cv2.IMREAD_UNCHANGED)        
        w=icon_img.shape[1]
        print(w)
        h=icon_img.shape[0]   
        result= cv2.matchTemplate(icon_img, template_img, cv2.TM_CCOEFF_NORMED) 
        print(result)
        loc= np.where(result>= threshold)
        print(loc)
        test_data=list(zip(*loc[::-1]))
        print(test_data)
        is_match= len(test_data) > 0
        print(is_match)
        point= []
        if is_match:
            point.append((test_data[0][0] +  w/2, test_data[0][1] + h/2))
        return is_match, point, test_data
d = adb('BAG00072893')
is_match,point,test_data=d.find(target_pic_name='icon.png')
x,y= test_data[0][0],test_data[0][1]
d.click(x,y)
print(x,y)
            

        
        