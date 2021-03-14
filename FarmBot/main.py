import cv2 as cv
import numpy as np
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

fullLime_img = cv.imread('full_lime.png', cv.IMREAD_UNCHANGED)
limestone_img = cv.imread('limestone_img.png', cv.IMREAD_UNCHANGED)
limestone2_img = cv.imread('limestone2_img.png', cv.IMREAD_UNCHANGED)
limestone3_img = cv.imread('limestone3_img.png', cv.IMREAD_UNCHANGED)
LmultiLime_img = cv.imread('Lmulti_lime.png', cv.IMREAD_UNCHANGED)
multiLime_img = cv.imread('multi_lime.png', cv.IMREAD_UNCHANGED)
DarkLime_img = cv.imread('limestoneDark_img.png', cv.IMREAD_UNCHANGED)
DarkLime2_img = cv.imread('limestoneDark2_img.png', cv.IMREAD_UNCHANGED)
#Reading the Limestone Images
lightResult = cv.matchTemplate(fullLime_img, limestone_img, cv.TM_CCOEFF_NORMED)
darkResult = cv.matchTemplate(multiLime_img, DarkLime_img, cv.TM_CCOEFF_NORMED)
darkResult2 = cv.matchTemplate(multiLime_img, DarkLime2_img, cv.TM_CCOEFF_NORMED)
mlightResult = cv.matchTemplate(LmultiLime_img, limestone2_img, cv.TM_CCOEFF_NORMED)
mlightResult2 = cv.matchTemplate(LmultiLime_img, limestone3_img, cv.TM_CCOEFF_NORMED)
#cv.imshow('Result', result)
#cv.waitKey()
#Grabbing Min and Max Location Values for images
Lmin_val, Lmax_val, Lmin_loc, Lmax_loc = cv.minMaxLoc(lightResult)
Dmin_val, Dmax_val, Dmin_loc, Dmax_loc = cv.minMaxLoc(darkResult)
D2min_val, D2max_val, D2min_loc, D2max_loc = cv.minMaxLoc(darkResult2)
MLmin_val, MLmax_val, MLmin_loc, MLmax_loc = cv.minMaxLoc(mlightResult)
ML2min_val, ML2max_val, ML2min_loc, ML2max_loc = cv.minMaxLoc(mlightResult2)

print('Best match top LEFT position: %s' % str(Lmax_loc))
print('Best match Confidence: %s' % Lmax_val)

threshhold = 0.8
Lightlocations = np.where(lightResult >= threshhold)
Lightlocations = list(zip(*Lightlocations[::-1]))
Darklocations = np.where(darkResult >= threshhold)
#Darklocations += np.where(darkResult2 >= threshhold)
Darklocations = list(zip(*Darklocations[::-1]))
print(Lightlocations)

if Lightlocations:
    print('Stone Found')
    #Grab Dimensions of the Image
    stone_w = limestone_img.shape[1]
    stone_h = limestone_img.shape[0]
    line_color = (0,255,0)
    line_type = cv.LINE_4

    if Darklocations:
        print('Dark Stone Found')
        Dstone_w = DarkLime_img.shape[1]
        Dstone_h = DarkLime_img.shape[0]

    for loc in Lightlocations:
        top_left = loc
        #Find Box Positions
        bottom_right = (top_left[0] + stone_w, top_left[1] + stone_h)
        #Drawing the boxes
        cv.rectangle(fullLime_img, top_left, bottom_right,
                    line_color, line_type)
        for dloc in Darklocations:
            top_left = dloc
            bottom_right = (top_left[0] + Dstone_w, top_left[1] + Dstone_h)
            cv.rectangle(multiLime_img, top_left, bottom_right,
                        line_color, line_type)

    cv.imshow('Result', fullLime_img)
    cv.imshow('Dark Result', multiLime_img)
    cv.waitKey()
    #cv.imwrite('stone_result.png', fullLime_img)
else:
    print('Stone NOT found')