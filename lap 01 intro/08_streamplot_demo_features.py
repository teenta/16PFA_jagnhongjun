# -*- coding: utf8 -*-
""""
Demo of the `streamplot` function

A streamplot, or streamline plot, is used to display 20 vector fields. This
example shows a few features of the stream plot function:

     * Varying the color a long a streamline.
     * Varying the density of streamlines.
     * Varying the line width a long a stream line.
"""

# "images_contours_and_fieds example code: streamplot_demo_features.py" images_contours_and_fieds example code:
# streamplot_demo_features.py - Matplotib 1.5.1 documentation. [Online]. Available:
# http://matplotlib.org/examples/images_contours_and_fields/streamplot_demo_features.html. [Accessed: 21-Aug-2016].


import numpy as np
# 그래프 관련 기능을 담고 있는 matplotlip.pyplot 모듈을 plt 라는 이름으로 불러 옴
# 관련 기능은 plt. 으로 시작함
import matplotlib.pyplot as plt
Y, X = np.mgrid[-3:3:100J, -3:3:100J]
U = -1 - X **2 + Y
V = 1 + X - Y ** 2
speed = np.sqrt(U * U +V * V)

plt.streamplot(X, Y, U, V, color=U, linewidth=2, cmap=plt.cm.autumn)
plt.colorbar()

f, (ax1, ax2) = plt.subplots(ncols=2)
ax1.streamplot(X, Y, U, V, density=[0.5, 1])

lw = 5 * speed / speed.max()
ax2.streamplot(X, Y, U, V, density=0.6, color='k', linewidth=lw)

plt.show()
