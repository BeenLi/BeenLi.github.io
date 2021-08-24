#! D:\\app\\miniconda\\python.exe
import sys
import cv2
print(sys.path)
print("Hello, world")
path = "C:\\Users\\wanli\\Pictures\\kobe.jpg"
kobe = cv2.imread(path)
kobe_short = cv2.resize(kobe, (kobe.shape[1]//2, kobe.shape[0]),
        interpolation=cv2.INTER_AREA)
cv2.imshow("kobe_short", kobe_short)
cv2.waitKey(0)
cv2.destoryAllWindows()

