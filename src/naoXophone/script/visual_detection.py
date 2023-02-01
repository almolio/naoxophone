import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import glob
import time

def extract_shapes(mask, er, dil, kernel):
    erosion = cv2.erode(mask,kernel,iterations = er)
    dilation = cv2.dilate(erosion,kernel,iterations = dil)
    return dilation

##########################################################
############ callibration with base frame ################
##########################################################
def callibration(image, top_bound, bottom_bound):

    ############ define base image without background ########
    ##########################################################

    #image           = video[base_frame,:,:,:] 
    base_image      = np.copy(image)
    base_image[0:top_bound, :,:]                 = \
        np.ones((top_bound, image.shape[1], image.shape[2]))*200 # 200 makes the ranges grey
    base_image[bottom_bound:image.shape[0], :,:] = \
        np.ones((image.shape[0]-bottom_bound, image.shape[1], image.shape[2]))*200

    ############ mask red ####################################
    ##########################################################
    image_hsv   = cv2.cvtColor(base_image, cv2.COLOR_BGR2HSV)
    
    lower_red = np.array([0,50,150])
    upper_red = np.array([10,235,190])


    mask_red  = cv2.inRange(image_hsv, lower_red, upper_red)

    kernel_rec = cv2.getStructuringElement(cv2.MORPH_RECT,(4,4))
    dil_red    = extract_shapes(mask_red, 1, 4, kernel_rec)

    ############ define ranges from red to red ###############
    ##########################################################
    y_min = 120
    y_max = 150

    red_bottom_left     = [np.max(np.where(dil_red!=0)[0]), np.min(np.where(dil_red!=0)[1])]
    red_bottom_right    = [np.max(np.where(dil_red!=0)[0]),np.max(np.where(dil_red!=0)[1]) ]
    diff_bottom         = (red_bottom_right[1] - red_bottom_left[1])/8    
    ranges_bottom       = np.zeros((2, 9))
    ranges_bottom[0, 0] = red_bottom_left[1]
    ranges_bottom[1,:]  = np.ones((1,9))*170
    for i in range(1, 9):
        ranges_bottom[0, i] = ranges_bottom[0,i-1]+diff_bottom

    ranges_top          = np.zeros((2, 9))
    ranges_top[0,0]     = ranges_bottom[0, 1]
    ranges_top[0,8]     = ranges_bottom[0, 7]
    diff_top            = (ranges_top[0,8] - ranges_top[0,0])/8   
    ranges_top[1,:]     = np.ones((1,9))*90 
    for i in range(1, 8):
        ranges_top[0, i] = ranges_top[0,i-1]+diff_top

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


    plt.figure()
    plt.imshow(image_rgb)
    for i in range(0, 9):
        plt.plot([ranges_bottom[0,i], ranges_top[0,i]], [ranges_bottom[1,i], ranges_top[1,i]] , linewidth = 2)
    plt.hlines(y_min, 50, 320, colors='white', linewidth = 2)
    plt.hlines(y_max, 50, 320, colors='white', linewidth = 2)
    plt.show()

    return dil_red, ranges_bottom, ranges_top


def find_played_tones(base_image, top_bound, bottom_bound, ranges_bottom, ranges_top):
    base_image[0:top_bound, :,:]                 = \
        np.ones((top_bound, base_image.shape[1], base_image.shape[2]))*200 # 200 makes the ranges grey
    base_image[bottom_bound:base_image.shape[0], :,:] = \
        np.ones((base_image.shape[0]-bottom_bound, base_image.shape[1], base_image.shape[2]))*200

    ############ rgb image to plot ###########################
    ##########################################################
    image_rgb = cv2.cvtColor(base_image, cv2.COLOR_BGR2RGB)

    ############ mask black ##################################
    ##########################################################
    image_hsv   = cv2.cvtColor(base_image, cv2.COLOR_BGR2HSV)
    lower_black = np.array([0,0,0])
    upper_black = np.array([150,100,100])
    mask_black  = cv2.inRange(image_hsv, lower_black, upper_black)
    kernel_cir  = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(6,6))
    dil_black   = extract_shapes(mask_black, 1, 3, kernel_cir)

    ############ find tones ##################################
    ##########################################################
    tones = ['red', 'orange', 'yellow', 'green', 'blue', 'white', 'lila', 'red', 'none']
    y_min = 110
    y_max = 140
    unique, counts = np.unique(np.where(dil_black[y_min:y_max] != 0)[1], return_counts=True)
    played = 8
    if len(counts) >=1:
        ind = np.where(counts == np.max(counts))[0]
        if len(ind) > 1:
            ind = ind[0]
        for i in range(0, 8):
            if  ranges_bottom[0, i] < unique[ind] < ranges_bottom[0, i+1]:
                played = i
                print(tones[i])


    # fig = plt.figure()
    #plt.imshow(image_rgb)
    # if True not in np.isnan(dil_black/np.max(np.abs(dil_black))):
    # plt.imshow(dil_black)#, alpha=(dil_black/np.max(np.abs(dil_black))))
    # for i in range(0, 9):
    #     plt.plot([ranges_bottom[0,i], ranges_top[0,i]], [ranges_bottom[1,i], ranges_top[1,i]] , linewidth = 2)
    # plt.hlines(y_min, 50, 320, colors='white', linewidth = 2)
    # plt.hlines(y_max, 50, 320, colors='white', linewidth = 2)
    # if len(counts) >=1:
    #     plt.title('Tone {}'.format(tones[played]))

    # path = '/home/hrsb/MSNE_HRS/catkin_ws/src/naoXophone'
    # plt.tight_layout()
    # fig.savefig(os.path.join(path, 'images', 'fig_{}.png'.format(time.time())))


    return played


##########################################################
############ identify tones and timing ###################
##########################################################

def clean_up(played_tones):
    # print(played_tones)
    for i in range(0,played_tones.shape[0]-1):
        if played_tones[i] == played_tones[i+1]:
            played_tones[i] = 8
    times_in_frames = np.where(played_tones != 8)[0]
    tones_in_frames = played_tones[times_in_frames]
    # print(times_in_frames.shape, tones_in_frames.shape)

    # for i in range(0,times_in_frames.shape[0]-2):
    #     # if times of two tones are less than 5 frames
    #     if times_in_frames[i] <= times_in_frames[i+1]+2\
    #         and tones_in_frames[i] == tones_in_frames[i+1]:
    #         tones_in_frames[i] = 100
    #         times_in_frames[i] = 100

    tones_in_frames = np.delete(tones_in_frames, np.where(tones_in_frames == 100)[0])
    times_in_frames = np.delete(times_in_frames, np.where(times_in_frames == 100)[0])

    # To Do: need to sample times in frames to times in robot
    times_in_frames  = times_in_frames - np.ones(times_in_frames.shape[0])*times_in_frames[0]
    # times_in_second = times_in_second/10
    tones_in_int  = tones_in_frames

    return times_in_frames, tones_in_int
