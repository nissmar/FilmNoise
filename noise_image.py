from noise_patch_generator import NoisePatchGenerator
import numpy as np
from utilities import resize_image


class NoiseImage():
    def __init__(self, input_image, ksize=11):
        # normalize
        self.input_image = input_image.copy()
        if np.max(self.input_image) > 2:  # image not in [0,1] range
            self.input_image /= 255
        self.dimx = self.input_image.shape[0]
        self.dimy = self.input_image.shape[1]

        self.out = np.zeros((self.dimx*ksize, self.dimy*ksize))
        self.resized_out = None
        self.ksize = ksize
        self.PatchGen = NoisePatchGenerator(ksize)
        self.PatchGen.make_batch(10000)

    def process(self):
        for i in range(self.dimx):
            for j in range(self.dimy):
                patch = self.PatchGen.simulate(self.input_image[i, j])
                self.out[self.ksize*i:self.ksize*i+self.ksize,
                         self.ksize*j:self.ksize*j+self.ksize] = patch
        self.resized_out = resize_image(self.out, self.input_image.shape)

    def output_raw_noise(self):
        return self.resized_out

    def output_mix(self, l=0.5):
        return l*self.resized_out+(1-l)*self.input_image
