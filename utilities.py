from PIL import Image
import numpy as np


def load_image(str, bw=True):
    im = np.array(Image.open(str)).astype('float')
    if bw:
        im = im.mean(axis=2)  # convert to bw
    return im


def resize_image(img, size):
    '''img in [0,1]'''
    out = Image.fromarray((255*img).astype("uint8"))
    return np.array(out.resize((size[1], size[0])))/255.0
