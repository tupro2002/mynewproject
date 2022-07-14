import cv2


# 'cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR','cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED'
method = cv2.TM_CCOEFF_NORMED

# Đọc file ảnh
small_image = cv2.imread('iconFB.png')
large_image = cv2.imread('anhcap.png')

result = cv2.matchTemplate(small_image, large_image, method)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(min_val, max_val, min_loc, max_loc )