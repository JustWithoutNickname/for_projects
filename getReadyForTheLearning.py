#до этого уже созданы папки куда распихивать обработанные картины

from mrcnn.config import Config
from mrcnn import model as modellib
import numpy as np
import colorsys
import imutils
import random
import cv2
import os

import random


def region_selection0(image, numberOfPhoto):
    print(0)
    part1 = random.randint(7, 9)
    part2 = random.randint(7, 9)
    startY = image.shape[0] // part1
    startX = image.shape[1] // part2
    endY = startY + (image.shape[0] - startY) // 3
    endX = startX + (image.shape[1] - startX) // 3
    for i in range(2):
        cropped = image[startY: endY, startX: endX]
        print(cropped.shape)
        cv2.imwrite("D:\\results\\picture" + str(numberOfPhoto) + "\\" + str(i + 1) + ".jpg", cropped)
        if (i == 1):
            break
        startX = endX + (image.shape[1] - endX) // 5
        startY += 2 * (image.shape[0] - startY) // 5
        endX += (image.shape[1] - startX)
        endY += (image.shape[0] - startY)


def region_selection1(image,startX, startY, endX, endY, numberOfPhoto):
    print(1)
    if ((startX >= (image.shape[1] - endX)) and (startY <= image.shape[0] - endY)):
        startY = endY + (image.shape[0] - endY) // 9
        endY =  startY + (image.shape[0] - startY) // 2
        endX = startX - startX // 8
        startX = startX // 10
    elif ((startX >= (image.shape[1] - endX))  and (startY >= image.shape[0] - endY)):
        endY = startY - startY // 8
        startY = startY // 10
        endX = startX - startX // 8
        startX = startX // 10
    elif ((startX <= (image.shape[1] - endX))  and (startY >= image.shape[0] - endY)):
        endY = startY - startY // 8
        startY = startY // 10
        startX = endX + (image.shape[1] - endX) // 9
        endX = startX +  (image.shape[1] - startX) * 2 // 3
    elif ((startX <= (image.shape[1] - endX))  and (startY <= image.shape[0] - endY)):
        startY = endY + (image.shape[0] - endY) // 9
        endY = startY + (image.shape[0] - startY) // 2
        startX = endX + (image.shape[1] - endX) // 9
        endX = startX + (image.shape[1] - startX) // 2
    cropped = image[startY : endY , startX : endX]
    cv2.imwrite("D:\\results\\picture" + str(numberOfPhoto) + "\\2.jpg", cropped)

for i in range(100):
    args = {"labels": "C:\\Users\\User\\PycharmProjects\\PythonStading\\coco_labels.txt",
            "weights": "C:\\Users\\User\\PycharmProjects\\PythonStading\\mask_rcnn_coco.h5",
            "image": "D:\\imagesForProject\\" + str(i) + ".jpg"}

    CLASS_NAMES = open(args["labels"]).read().strip().split("\n")

    # generate random (but visually distinct) colors for each class label
    # (thanks to Matterport Mask R-CNN for the method!)
    hsv = [(j / len(CLASS_NAMES), 1, 1.0) for j in range(len(CLASS_NAMES))]
    COLORS = list(map(lambda c: colorsys.hsv_to_rgb(*c), hsv))
    random.seed(42)
    random.shuffle(COLORS)
    image = cv2.imread(args["image"])
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = imutils.resize(image, width=512)

    class SimpleConfig(Config):
        # give the configuration a recognizable name
        NAME = "coco_inference"

        # set the number of GPUs to use along with the number of images
        # per GPU
        GPU_COUNT = 1
        IMAGES_PER_GPU = 1

        # number of classes (we would normally add +1 for the background
        # but the background class is *already* included in the class
        # names)
        NUM_CLASSES = len(CLASS_NAMES)

        # cv2.imwrite("D:\\results\\picture" + str(i) + "\\0.jpg", image)


    config = SimpleConfig()
    # initialize the Mask R-CNN model for inference and then load the
    # weights
    print("[INFO] loading Mask R-CNN model...")
    model = modellib.MaskRCNN(mode="inference", config=config, model_dir=os.getcwd())
    model.load_weights(args["weights"], by_name=True)
    # perform a forward pass of the network to obtain the results
    print("[INFO] making predictions with Mask R-CNN...")
    r = model.detect([image], verbose=1)[0]

    for j in range(0, r["rois"].shape[0]):
        # extract the class ID and mask for the current detection, then
        # grab the color to visualize the mask (in BGR format)
        classID = r["class_ids"][j]
        mask = r["masks"][:, :, j]
        color = COLORS[classID][::-1]

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # loop over the predicted scores and class labels


    for j in range(0, len(r["scores"])):
        (startY, startX, endY, endX) = r["rois"][j]
        cropped = image[startY - startY // 5: endY + (image.shape[0] - endY) // 5,
                  startX - startX // 5: endX + (image.shape[1] - endX) // 5]
        #cv2.imshow("vhjfas", cropped)
        cv2.imwrite("D:\\results\\picture" + str(i) + "\\" + str(j + 1) + ".jpg", cropped)

    if (len(r["scores"]) == 0):
        region_selection0(image, i)
    elif (len(r["scores"]) == 1):
        (stY, stX, eY, eX) = r["rois"][0]
        region_selection1(image, stX, stY, eX, eY, i)
    # show the output image
    #cv2.imshow("vyvod", image)
    #cv2.waitKey()