#!/usr/bin/env python
# coding: utf-8

# In[19]:


import matplotlib.pyplot as plt
import numpy as np


# In[22]:


derece = [20,19,14,19,17,11,14,13,16,17,17,14,13,11,11,16,11,15,9,7,12,13,13,13,17,17,18,20,16,6,8]
gün = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

plt.plot(gün,derece,color="red")
plt.title("Kayseri Mart 2023 Hava Sıcaklık Grafiği") # Başlık Yazmak İçin
plt.xlabel("Günler") # X Ekseni Başlık 
plt.ylabel("Sıcaklık Dercesi") # Y Ekseni Başlık
plt.grid() # Kare Çizgisi Ekler


# In[ ]:




