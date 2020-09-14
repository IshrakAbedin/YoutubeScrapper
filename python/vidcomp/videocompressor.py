import h5py
from skvideo import io as vio

def compressvideo(filepath : str, output: str, ylabelval: float, xkey: str, ykey: str):
    # Reading
    vid = vio.vread(filepath)  
    # Writing
    with h5py.File(output, 'w') as wfile:
        wfile.create_dataset(xkey, data=vid)
        wfile.create_dataset(ykey, data=ylabelval)