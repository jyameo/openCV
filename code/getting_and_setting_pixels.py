from argparse import ArgumentParser as ap
import cv2

parser = ap()
parser.add_argument("-i","--image", required = True, help = "Path to image required")
args = vars(parser.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Original", image)

(b, g, r) = image[0,0]
print("Pixel at (0,0) => Red: {}, Green: {}, Blue: {}".format(r,g,b))

corner = image[0:100, 0:100]
cv2.imshow("Corner", corner)

image[0:100, 0:100] = (0, 255, 0)

(b, g, r) = image[0,0]
print("Pixel at (0,0) => Red: {}, Green: {}, Blue: {}".format(r,g,b))

cv2.imshow("Updated", image)
cv2.waitKey(0)