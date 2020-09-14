import h5py
import numpy as np

titles = []
with open("./downloadlist.txt", "r") as dlfile:
    titles = dlfile.readlines()

titles = [title.strip() for title in titles]

for title in titles:
    with h5py.File("./out/compresseddata/" + title + ".hdf5", 'r') as rfile:
        ldr = rfile[("label")].value
        shape = rfile[("video")].shape
        print(f"{title} ldr: { ldr } shape: { shape }")