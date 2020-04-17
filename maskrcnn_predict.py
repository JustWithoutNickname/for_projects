# USAGE
# python maskrcnn_predict.py --weights mask_rcnn_coco.h5 --labels coco_labels.txt --image images/30th_birthday.jpg

# import the necessary packages
from mrcnn.config import Config
from mrcnn import model as modellib
from mrcnn import visualize
import numpy as np
import colorsys
import argparse
import imutils
import random
import cv2
import os
import sklearn
import random


def region_selection0(image):
    part1 = random.randint(7, 9)
    part2 = random.randint(7, 9)
    startY = image.shape[0] // part1
    startX = image.shape[1] // part2
    #part1 = random.randint(3, 6)
    #part2 = random.randint(3, 6)
    endY = startY + (image.shape[0] - startY) // 3
    endX = startX + (image.shape[1] - startX) // 3
    for i in range(2):
        cropped = image[startY: endY, startX: endX]
        print(cropped.shape)
        cv2.imwrite("C:\\Users\\User\\PycharmProjects\\PythonStading\\results_of_predictions\\outpyt" + str(i) + ".jpg",
                    cropped)
        if (i == 1):
            break
        startX = endX + (image.shape[1] - endX) // 5
        startY += 2 * (image.shape[0] - startY) // 5
        endX += (image.shape[1] - startX)
        endY += (image.shape[0] - startY)


def region_selection1(image,startX, startY, endX, endY):
    print(startX <= (image.shape[1] - endX))
    print(startY >= image.shape[0] - endY, '\n')
    print(startX >= (image.shape[1] - endX))
    print(startY <= image.shape[0] - endY, '\n')
    print(startX >= (image.shape[1] - endX))
    print(startY >= image.shape[0] - endY, '\n')
    print(startX <= (image.shape[1] - endX))
    print(startY <= image.shape[0] - endY)
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
    cv2.imwrite("C:\\Users\\User\\PycharmProjects\\PythonStading\\results_of_predictions\\outpyt1.jpg",
                cropped)
# construct the argument parse and parse the arguments
"""ap = argparse.ArgumentParser()
ap.add_argument("-w", "--weights", required=True,
	help="path to Mask R-CNN model weights pre-trained on COCO")
ap.add_argument("-l", "--labels", required=True,
	help="path to class labels file")
ap.add_argument("-i", "--image", required=True,
	help="path to input image to apply Mask R-CNN to")
args = vars(ap.parse_args())"""
args = {"labels": "C:\\Users\\User\\PycharmProjects\PythonStading\coco_labels.txt",
        "weights": "C:\\Users\\User\\PycharmProjects\PythonStading\mask_rcnn_coco.h5",
        "image": "C:\\Users\\User\\PycharmProjects\PythonStading\\abstractOne.jpg",
        "output": "C:\\Users\\User\\PycharmProjects\PythonStading\outpyt.jpg"}
# load the class label names from disk, one label per line
CLASS_NAMES = open(args["labels"]).read().strip().split("\n")

# generate random (but visually distinct) colors for each class label
# (thanks to Matterport Mask R-CNN for the method!)
hsv = [(i / len(CLASS_NAMES), 1, 1.0) for i in range(len(CLASS_NAMES))]
COLORS = list(map(lambda c: colorsys.hsv_to_rgb(*c), hsv))
random.seed(42)
random.shuffle(COLORS)


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


# initialize the inference configuration
config = SimpleConfig()

# initialize the Mask R-CNN model for inference and then load the
# weights
print("[INFO] loading Mask R-CNN model...")
model = modellib.MaskRCNN(mode="inference", config=config,
                          model_dir=os.getcwd())
model.load_weights(args["weights"], by_name=True)

# load the input image, convert it from BGR to RGB channel
# ordering, and resize the image
image = cv2.imread(args["image"])
image.imwrite("C:\\Users\\User\\PycharmProjects\\PythonStading\\results_of_predictions\\output0.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image = imutils.resize(image, width=512)

# perform a forward pass of the network to obtain the results
print("[INFO] making predictions with Mask R-CNN...")
r = model.detect([image], verbose=1)[0]

# loop over of the detected object's bounding boxes and masks
for i in range(0, r["rois"].shape[0]):
    # extract the class ID and mask for the current detection, then
    # grab the color to visualize the mask (in BGR format)
    classID = r["class_ids"][i]
    mask = r["masks"][:, :, i]
    color = COLORS[classID][::-1]

# visualize the pixel-wise mask of the object
# image = visualize.apply_mask(image, mask, color, alpha=0.5)

# convert the image back to BGR so we can use OpenCV's drawing
# functions
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

# loop over the predicted scores and class labels
(stY, stX, eY, eX) = r["rois"][0]
for i in range(0, len(r["scores"])):
    # extract the bounding box information, class ID, label, predicted
    # probability, and visualization color
    # Y - height, X - length
    (startY, startX, endY, endX) = r["rois"][i]
    cropped = image[startY - startY // 5: endY + (image.shape[0] - endY) // 5,
              startX - startX // 5: endX + (image.shape[1] - endX) // 5]
    # print("stY", startY, "stX", startX, "endX", endX, "endY", endY)
    cv2.imwrite("C:\\Users\\User\\PycharmProjects\\PythonStading\\results_of_predictions\\outpyt" + str(i + 1) + ".jpg",
                cropped)
    classID = r["class_ids"][i]
    label = CLASS_NAMES[classID]
    score = r["scores"][i]
    color = [int(c) for c in np.array(COLORS[classID]) * 255]

    # draw the bounding box, class label, and score of the object
    cv2.rectangle(image, (startX, startY), (endX, endY), color, 2)
    text = "{}: {:.3f}".format(label, score)
    y = startY - 10 if startY - 10 > 10 else startY + 10
    cv2.putText(image, text, (startX, y), cv2.FONT_HERSHEY_SIMPLEX,
                0.6, color, 2)

if (len(r["scores"]) == 0):
    region_selection0(image)
elif (len(r["scores"]) == 1):
    region_selection1(image, stX, stY, eX, eY)
# show the output image
cv2.imshow("vyvod", image)
cv2.waitKey()
