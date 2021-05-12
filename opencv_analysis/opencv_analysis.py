import cv2
import numpy as np


def edge_detect(file, minval, maxval):
    # 读取图片
    w1 = cv2.imread(file)

    # 边缘检测
    gaus = cv2.GaussianBlur(w1, (3, 3), 0, 0)
    gray = cv2.cvtColor(gaus, cv2.COLOR_BGR2GRAY)
    edge_output = cv2.Canny(gray, minval, maxval)

    # 查找并绘制轮廓
    # ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(edge_output, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    w1 = cv2.drawContours(w1, contours, 1, (0, 0, 255), 4)

    # 提取前景
    mask = np.zeros(w1.shape, np.uint8)
    mask = cv2.drawContours(mask, contours, 1, (255, 255, 255), -1)
    loc = cv2.bitwise_and(w1, mask)

    image_out = cv2.imwrite(r"appimage\wound_image\manual_result\manual_result.png", w1)
