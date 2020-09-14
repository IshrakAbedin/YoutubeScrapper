import numpy as np
import h5py
from skvideo import io as vio

READ_DIR = r"./out/processedvideos/"
WRITE_DIR = r"./out/compresseddata/"
file = "Aquaman"

# Reading
vid = vio.vread(READ_DIR + file + ".mp4")  
print(vid.shape)
ldr = 2.5314

# Writing
with h5py.File(WRITE_DIR + file + ".hdf5", 'w') as wfile:
    dset = wfile.create_dataset("video", data=vid)
    dset = wfile.create_dataset("label", data=ldr)

# Read Back
with h5py.File(WRITE_DIR + file + ".hdf5", 'r') as rfile:
    print("=====label=====\n", rfile[("label")].value)
    print("=====video=====\n", np.max(rfile[("video")]))