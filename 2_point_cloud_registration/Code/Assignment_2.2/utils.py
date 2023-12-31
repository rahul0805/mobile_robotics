import numpy as np

def readData(filename):

    """
    reads the ground truth file
    returns a 2D array with each
    row as GT pose(arranged row major form)
    array size should be 1101*12
    """
    data = np.loadtxt(filename)
    return data


def readPointCloud(filename):
    """
    reads bin file and returns
    as m*4 np array
    all points are in meters
    you can filter out points beyond(in x y plane)
    50m for ease of computation
    and above or below 10m
    """
    pcl = np.fromfile(filename, dtype=np.float32,count=-1)
    pcl = pcl.reshape([-1,4])
    return pcl
