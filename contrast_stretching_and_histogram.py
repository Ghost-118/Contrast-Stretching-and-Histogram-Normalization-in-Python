# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 13:04:34 2024

@author: jose ochoa
"""

import cv2
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 

sns.set_theme()

img = cv2.imread("img2_bajo_contraste.jpg", 0)

i_min = np.min(img)
i_max = np.max(img)

img = (img-i_min)/(i_max-i_min)

img = (img*255).astype(int) 

frecuencias = np.zeros(256, dtype=int) 

unique, counts = np.unique(img, return_counts=True)
frecuencias[unique] = counts 
x = np.arange(256)

cv2.imwrite("img2_E12.jpg", img) 

plt.figure(figsize=(16, 9)) 
plt.stem(x, frecuencias)
plt.tight_layout()
plt.savefig("img2_histograma_E12.jpg")
plt.show()

#Ejercicio 12