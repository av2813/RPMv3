from skimage import data, feature, exposure
from PIL import Image
import numpy as np
import argparse
import cv2
import math
from shapely import geometry
from matplotlib import pyplot as plt
from scipy import spatial
import itertools
import matplotlib.cm as cm
import matplotlib.colors as cl
global mx, my

#def spinflipdetect(before, after)
before = r"C:\Users\Dell XPS 9530\Documents\PhD\Samples\KS002\Monopole\524 mA-y\ks002-2x4-h-524ma-y-bigt.png" #Path to MFM image
after = r"C:\Users\Dell XPS 9530\Documents\PhD\Samples\KS002\Monopole\542 mA-y\ks002-2x4-h-542ma-y-bigt.png" #Path to lattice image

before = cv2.imread(before)
before_grey = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
cv2.imshow("click",before_grey)
cv2.waitKey(-1)

after = cv2.imread(after)
after_grey = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)
cv2.imshow("",after_grey)
cv2.waitKey(-1)

difference=cv2.subtract(before_grey,after_grey)
cv2.imshow("",difference)
cv2.waitKey(-1)
