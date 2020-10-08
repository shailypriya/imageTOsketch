def dodge(front,back):
    result=front*255/(255-back) 
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')

import numpy as np
def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])

img ="C:\\Users\\Shaily Priya\\Desktop\\projects\\sketchify-master\\263697.20.jpg"

import imageio
s = imageio.imread(img)
g=grayscale(s)
i = 255-g
import scipy.ndimage
b = scipy.ndimage.filters.gaussian_filter(i,sigma=10)
r= dodge(b,g)

import matplotlib.pyplot as plt
plt.imshow(r, cmap="gray")

plt.imsave('img2.png', r, cmap='gray', vmin=0, vmax=255)