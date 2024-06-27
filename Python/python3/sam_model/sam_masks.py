# -*- coding: utf-8 -*-
# @Time    : 2024/6/24 23:08
# @Author  : Monarch
# @File    : sam_masks.py
# @Software: PyCharm

import os
import torch
import time
import cv2
import matplotlib.pyplot as plt
from segment_anything import sam_model_registry, SamAutomaticMaskGenerator
import numpy as np

start = time.time()
path = r'D:\Work\SamUGis'
os.chdir(path)

image_file = r'F1-2018.JPG'
img = cv2.imread(image_file)
image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

sam_checkpoint = "asset/sam_vit_b_01ec64.pth"
model_type = "vit_b"
device = "cuda"

sam = sam_model_registry[model_type](checkpoint=sam_checkpoint)
sam.to(device=device)
mask_generator = SamAutomaticMaskGenerator(sam, points_per_batch=8)
masks = mask_generator.generate(image)
w = masks[0]["segmentation"].shape[0]
h = masks[0]["segmentation"].shape[1]
mask_data = np.zeros((w, h))
labels = np.zeros((w, h))
for index, ann in enumerate(masks):
    m = ann["segmentation"]
    mask_data[m] = index + 1
labels[1:w-1, 1:h-1] = (mask_data[1:w-1, 2:h] != mask_data[1:w-1, :h-2]) | (mask_data[2:w, 1:h-1] != mask_data[:w-2, 1:h-1])
img[labels == 1] = 0
cv2.imwrite('F1-2018-seg-32.png', img)

print('耗时:', time.time()-start)


