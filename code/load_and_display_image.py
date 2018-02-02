import argparse
import cv2
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", required = True, help = "Path to the image")

args = vars(parser.parse_args())

image =  cv2.imread(args["image"])

print("Shape: {}".format(image.shape))
print("Width: {} pixels".format(image.shape[1]))
print("Height: {} pixels".format(image.shape[0]))
print("Channels: {} pixels".format(image.shape[2]))

cv2.imshow("Image0", image[:,:,0])
cv2.imshow("Image1", image[:,:,1])
cv2.imshow("Image2", image[:,:,2])
cv2.waitKey(0)
