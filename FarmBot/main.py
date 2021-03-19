import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
cvUNCHANGED = cv.IMREAD_UNCHANGED

def findClickPositions(stone_img_path, full_img_path, threshold=0.6, debug_mode=None):
    
    fullLime_img = cv.imread('full_lime.png', cvUNCHANGED)
    limestone_img = cv.imread('limestone_img.png', cvUNCHANGED)
    limestone2_img = cv.imread('limestone2_img.png', cvUNCHANGED)
    limestone3_img = cv.imread('limestone3_img.png', cvUNCHANGED)
    multiLimeLight_img = cv.imread('multi_limeLight.png', cvUNCHANGED)
    multiLimeDark_img = cv.imread('multi_limeDark.png', cvUNCHANGED)
    DarkLime_img = cv.imread('limestoneDark_img.png', cvUNCHANGED)
    DarkLime2_img = cv.imread('limestoneDark2_img.png', cvUNCHANGED)
    #Reading the Limestone Images
    lightResult = cv.matchTemplate(fullLime_img, limestone_img, cv.TM_CCOEFF_NORMED)
    darkResult = cv.matchTemplate(multiLimeDark_img, DarkLime_img, cv.TM_CCOEFF_NORMED)
    darkResult2 = cv.matchTemplate(multiLimeDark_img, DarkLime2_img, cv.TM_CCOEFF_NORMED)
    mlightResult = cv.matchTemplate(multiLimeLight_img, limestone2_img, cv.TM_CCOEFF_NORMED)
    mlightResult2 = cv.matchTemplate(multiLimeLight_img, limestone3_img, cv.TM_CCOEFF_NORMED)

    threshhold = 0.8
    Lightlocations = np.where(lightResult >= threshhold)
    Lightlocations = list(zip(*Lightlocations[::-1]))

    Darklocations = np.where(darkResult >= threshhold)
    Darklocations = list(zip(*Darklocations[::-1]))

    Darklocations2 = np.where(darkResult2 >= threshhold)
    DarkLocations2 = list(zip(*Darklocations2[::-1]))

    Lightlocations2 = np.where(mlightResult >= threshhold)
    Lightlocations2 = list(zip(*Lightlocations2[::-1]))

    Lightlocations3 = np.where(mlightResult2 >= threshhold)
    Lightlocations3 = list(zip(*Lightlocations3[::-1]))
    #Darklocations += np.where(darkResult2 >= threshhold)
    print(Lightlocations)


    if Lightlocations:
        print('Stone Found')
        #Grab Dimensions of the Image
        Lstone_w = limestone_img.shape[1]
        Lstone_h = limestone_img.shape[0]

        if Darklocations:
            print('Multi Dark Stone Found')
            Dstone_w = DarkLime_img.shape[1]
            Dstone_h = DarkLime_img.shape[0]
        if Darklocations2:
            print('Multi Dark Stone Found')
            D2stone_w = DarkLime2_img.shape[1]
            D2stone_h = DarkLime2_img.shape[0]
        if Lightlocations2:
            print('Multi Light Stone Found')
            L2stone_w = limestone2_img.shape[1]
            L2stone_h = limestone2_img.shape[0]
        if Lightlocations3:
            print('Multi Light Stone Found')
            L3stone_w = limestone3_img.shape[1]
            L3stone_h = limestone3_img.shape[0]

    rectangles = []
    for loc in Lightlocations:
        rect = [int(loc[0]), int(loc[1]), Lstone_w, Lstone_h]
        rectangles.append(rect)
        rectangles.append(rect)

    rectangles, weight = cv.groupRectangles(rectangles, groupThreshold=1, eps=0.5)

    points = []
    if len(rectangles):
        line_color = (0,255,0)
        line_type = cv.LINE_4
        marker_color = (255, 0, 255)
        marker_type = cv.MARKER_CROSS

        for (x, y, w, h) in rectangles:
            center_x = x + int(w/2)
            center_y = y + int(h/2)
            points.append((center_x, center_y))

            if debug_mode == 'rectangles':
                top_left = (x, y)
                bottom_right = (x + w, y + h)
                cv.drawMarker(limestone2_img, (center_x, center_y),
                              color=line_type, thickness=2)
            elif debug_mode == 'points':
                cv.drawMarker(limestone2_img, (center_x, center_y),
                              color=marker_color, markerType=marker_type,
                              markerSize=40, thickness=2)
        if debug_mode:
            cv.imshow('Matches', limestone2_img)
            cv.waitKey()
        
    return points

points = findClickPositions('travertineLight_img.png','multi_limeLight.png', debug_mode='points')
print(points)
points = findClickPositions('limestone2_img.png', 'multi_limeLight.png',
                            threshold=0.70, debug_mode='rectangles')
print(points)
print('Done.')
    