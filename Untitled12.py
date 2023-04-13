#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import numpy as np


# In[2]:


sayı = [11539,11721,11519,11811,12359,12775,13084,13360,13799,14313,14913,15486,15889,15998,16247,17199,17266,17190,17793,19274,20271]
yıl = [2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021,2022]


# In[3]:


plt.plot(yıl,sayı,color="yellow")
plt.title("Yıllara Göre Biçerdöver Sayı Grafiği") # Başlık Yazmak İçin
plt.xlabel("Yıllar") # X Ekseni Başlık 
plt.ylabel("Biçerdöver Sayısı") # Y Ekseni Başlık
plt.grid() # Kare Çizgisi Ekler


# In[ ]:




