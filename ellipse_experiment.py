"""
Trying to figure out how to extract a rotated ellipse from a grid.

This was key:
http://math.stackexchange.com/questions/426150/what-is-the-general-equation-of-the-ellipse-that-is-not-in-the-origin-and-rotate

"""

from __future__ import division

import numpy as np
import matplotlib.pyplot as plt

grid = np.ones((100,100))
x_indices, y_indices = np.indices(grid.shape)

b_maj = 40
b_min = 20

x_cen = 50
y_cen = 40

ellipse_selection = ((x_indices-x_cen)/b_maj)**2 + ((y_indices-y_cen)/b_min)**2 <= 1

theta = np.radians(11)

rotated_ellipse_selection = (
    (((x_indices-x_cen)*np.cos(theta) + (y_indices-y_cen)*np.sin(theta))/b_maj)**2 + 
    (((x_indices-x_cen)*np.sin(theta) + (y_indices-y_cen)*np.cos(theta))/b_min)**2) <= 1


fig = plt.figure()
plt.imshow(grid)

e_grid = np.copy(grid)
e_grid[ellipse_selection] = 0

plt.imshow(e_grid)

r_grid = np.copy(grid)
r_grid[rotated_ellipse_selection] = 2

plt.imshow(r_grid, origin='lower')

plt.show()
