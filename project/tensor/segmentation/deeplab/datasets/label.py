import tensorflow as tf
from PIL import Image
from tqdm import tqdm
import numpy as np
import sys

import os, shutil

arg1 = sys.argv[1]

# palette (color map) describes the (R, G, B): Label pair
palette = {
    (0,0,0):0,
    (255,0,218):1,
    (255,0,0):2,
    (114,0,255):3,
    (0,5,255):4
}

def convert_from_color_segmentation(arr_3d):
    arr_2d = np.zeros((arr_3d.shape[0], arr_3d.shape[1]), dtype=np.uint8)

    for c, i in palette.items():
        m = np.all(arr_3d == np.array(c).reshape(1, 1, 3), axis=2)
        arr_2d[m] = i
    return arr_2d


label_dir = arg1+'dataset/SegmentationClass/'
new_label_dir = arg1+'dataset/SegmentationClassRaw/'

if os.path.isdir(new_label_dir):
    print("Folder alread exists. Delete the folder and re-run the code!!!")
    shutil.rmtree(new_label_dir)
	
print("creating folder: ", new_label_dir)
os.mkdir(new_label_dir)


label_files = os.listdir(label_dir)

for l_f in tqdm(label_files):
    arr = np.array(Image.open(label_dir + l_f))
    arr = arr[:,:,0:3]
    arr_2d = convert_from_color_segmentation(arr)
    Image.fromarray(arr_2d).save(new_label_dir + l_f)