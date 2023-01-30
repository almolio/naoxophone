import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import glob

"""
TO DO:
Change path to video.
"""
path = "/Users/aliyaablitip/Desktop/HRS/"

def extract_shapes(mask, er, dil, kernel):
    erosion = cv2.erode(mask,kernel,iterations = er)
    dilation = cv2.dilate(erosion,kernel,iterations = dil)
    return dilation

############ load video and save as numpy arr ############
##########################################################
cap = cv2.VideoCapture(os.path.join(path, 'rec_lamp.mp4'))
frames = []
ret = True
while ret:
    ret, img = cap.read() 
    if ret:
        frames.append(img)
video = np.stack(frames, axis=0) # dimensions (T, H, W, C)

############ define base image without background ########
##########################################################

for frame in range(0, video.shape[0]):
    
    """
    In the robot, we have to adjust the ranges for the base image or
    have a neutral background without black and red. This should be 
    doable for the demo. 
    """

    top_bound       = 100
    bottom_bound    = 200
    image           = video[frame,:,:,:] 
    base_image      = np.copy(image)
    base_image[0:top_bound, :,:]                 = \
        np.ones((top_bound, image.shape[1], image.shape[2]))*200 # 200 makes the ranges grey
    base_image[bottom_bound:image.shape[0], :,:] = \
        np.ones((image.shape[0]-bottom_bound, image.shape[1], image.shape[2]))*200

    ############ rgb image to plot ###########################
    ##########################################################
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    ############ mask red and black ##########################
    ##########################################################
    image_hsv   = cv2.cvtColor(base_image, cv2.COLOR_BGR2HSV)

    lower_red = np.array([170,50,50])
    upper_red = np.array([180,255,255])
    mask_red        = cv2.inRange(image_hsv, lower_red, upper_red)

    lower_black =np.array([110,0,0])
    upper_black =np.array([200,100,100])
    mask_black      = cv2.inRange(image_hsv, lower_black, upper_black)

    kernel_rec = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
    kernel_cir = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(7,7))

    dil_red     = extract_shapes(mask_red, 1, 4, kernel_rec)
    dil_black   = extract_shapes(mask_black, 1, 3, kernel_cir)


    ############ define ranges from red to red ###############
    ##########################################################
    red_bottom_left     = [np.max(np.where(dil_red!=0)[0]), np.min(np.where(dil_red!=0)[1])]
    red_bottom_right    = [np.max(np.where(dil_red!=0)[0]),np.max(np.where(dil_red!=0)[1]) ]
    diff_bottom         = (red_bottom_right[1] - red_bottom_left[1])/8    
    ranges_bottom       = np.zeros((2, 9))
    ranges_bottom[0, 0] = red_bottom_left[1]
    ranges_bottom[1,:]  = np.ones((1,9))*200
    for i in range(1, 9):
        ranges_bottom[0, i] = ranges_bottom[0,i-1]+diff_bottom

    ranges_top          = np.zeros((2, 9))
    ranges_top[0,0]     = ranges_bottom[0, 1]
    ranges_top[0,8]     = ranges_bottom[0, 7]
    diff_top            = (ranges_top[0,8] - ranges_top[0,0])/8   
    ranges_top[1,:]     = np.ones((1,9))*120 
    for i in range(1, 8):
        ranges_top[0, i] = ranges_top[0,i-1]+diff_top

    ############ find tones ##################################
    ##########################################################
    tones = ['red', 'orange', 'yellow', 'green', 'blue', 'white', 'lila', 'red', 'none']
    y_min = 140
    y_max = 160
    unique, counts = np.unique(np.where(dil_black[y_min:y_max] != 0)[1], return_counts=True)
    if len(counts) >=10:
        ind = np.where(counts == np.max(counts))[0]
        if len(ind) > 1:
            ind = ind[0]
        # print(ind, unique[ind])
        i = 9
        for i in range(0, 8):
            if  ranges_bottom[0, i] < unique[ind] < ranges_bottom[0, i+1]:
                played = i


    ############  save figure ################################
    ##########################################################

    if os.path.isdir(os.path.join(path, 'images')) == False:
        os.mkdir(os.path.join(path, 'images'))

    fig = plt.figure()
    plt.imshow(image_rgb)

    if True not in np.isnan(dil_red/np.max(np.abs(dil_red))):
        plt.imshow(dil_red*0, alpha=(dil_red/np.max(np.abs(dil_red))))
    if True not in np.isnan(dil_black/np.max(np.abs(dil_black))):
        plt.imshow(dil_black, alpha=(dil_black/np.max(np.abs(dil_black))))

    for i in range(0, 9):
        plt.plot([ranges_bottom[0,i], ranges_top[0,i]], [ranges_bottom[1,i], ranges_top[1,i]] , linewidth = 2)
    plt.hlines(y_min, 50, 320, colors='white', linewidth = 2)
    plt.hlines(y_max, 50, 320, colors='white', linewidth = 2)
    if len(counts) >=10:
        plt.title('Tone {}'.format(tones[played]))

    fig.savefig(os.path.join(path, 'images', 'fig_{}.png'.format(frame)))
    plt.tight_layout()
    # plt.show()
    plt.close()

 
############  save video ################################
##########################################################
img_array = []
def get_key(fp):
    filename = fp.split('_')[1]
    int_part = filename.split('.')[0]
    return int(int_part)

for filename in sorted(glob.glob(os.path.join(path, 'images/*.png')), key=get_key):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)
 
 
out = cv2.VideoWriter('project.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 30, size)
 
for i in range(len(img_array)):
    out.write(img_array[i])
out.release()
