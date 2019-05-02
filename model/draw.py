import cv2
import numpy as np
from predict import *

drawing = False  # true if mouse is pressed
mode = True

# mouse callback function


def roi(location):
    xbar = []
    ybar = []
    for value in location:
        xbar.append(value[0])
        ybar.append(value[1])
    min_x = min(xbar)
    max_x = max(xbar)
    min_y = min(ybar)
    max_y = max(ybar)
    return min_x, max_y, max_x, min_y


location = []
number = 0
line_color = (255, 255, 255)


def paint_draw(event, former_x, former_y, flags, param):
    global current_former_x, current_former_y, drawing, mode, number
    if event == cv2.EVENT_LBUTTONDOWN:
        location.clear()
        drawing = True
        current_former_x, current_former_y = former_x, former_y
        cropping = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.line(image, (current_former_x, current_former_y),
                         (former_x, former_y), line_color, 20)
                current_former_x = former_x
                current_former_y = former_y
        location.append([current_former_x, current_former_y])

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.line(image, (current_former_x, current_former_y),
                     (former_x, former_y), line_color, 5)
            current_former_x = former_x
            current_former_y = former_y
        x1, y1, x2, y2 = roi(location)
        cropping = False
        cv2.rectangle(image, (x1-20, y1+20), (x2+20, y2-20), (0, 0, 255), 2)
        #cv2.imshow("image", image)
        crop_img = image[y2-18:y1+18, x1-18:x2+18]
        cv2.imshow("digit", crop_img)
        cv2.imwrite("E:\\digits\\digit.png", crop_img)
        argv = "E:\\digits\\digit.png"
        img_pre = preprocess(argv)
        result = clf.predict([img_pre])
        print(result)

    return former_x, former_y


image = cv2.imread("E:\\black_1.jpg")
cv2.namedWindow("OpenCV Paint Brush")
cv2.setMouseCallback('OpenCV Paint Brush', paint_draw)
while(1):
    cv2.imshow('OpenCV Paint Brush', image)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:  # Escape KEY
        cv2.imwrite("E:\\painted_image.jpg", image)
        break

cv2.destroyAllWindows()
