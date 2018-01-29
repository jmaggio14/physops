import numpy as np
import physops



def one(x_grid,y_grid):
    wavefront = np.ones(x_grid.shape)
    return wavefront

def cyl(x_grid,y_grid,diameter):
    radii = np.sqrt(x_grid**2 + y_grid**2)

    wavefront = np.zeros(x_grid.shape)
    wavefront[np.where(radii < diameter/2)] = 1
    return wavefront

# 
# def rect(x_grid,y_grid,width,height):
#     tmp = np.zeros(x_grid.shape)
