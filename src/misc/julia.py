#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
~~~~~~~~~~~~~~~~~~~
A Julia Set Fractal 
~~~~~~~~~~~~~~~~~~~
"""

import numpy as np
import matplotlib.pyplot as plt
from numba import jit


MAXITERS = 500
RADIUS = 4
CONST = 0.7


@jit('float32(complex64)')
def escape(z):
    for i in range(MAXITERS):
        if z.real * z.real + z.imag * z.imag > RADIUS:
            break
        z = (z*z + CONST) / (z*z - CONST)
    return i


def main(xmin, xmax, ymin, ymax, width, height):
    y, x = np.ogrid[ymax: ymin: height*1j, xmin: xmax: width*1j]
    z = x + y*1j
    img = np.asarray(np.frompyfunc(escape, 1, 1)(z)).astype(np.float)
    img /= np.max(img)
    img = np.sin(img**2 * np.pi) # a simple way to smooth the coloring.
    fig = plt.figure(figsize=(width/100.0, height/100.0), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis('off')
    ax.imshow(img, cmap='hot')
    fig.savefig('julia.png')


if __name__ == '__main__':
    main(-2, 2, -1.6, 1.6, 800, 640)
