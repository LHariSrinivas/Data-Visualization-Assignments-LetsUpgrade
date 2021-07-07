#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib as mpl
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from numpy.random import randn,randint,uniform,sample
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.DataFrame(randn(10,4),columns=['a','b','c','d'])


# In[4]:


df.head()


# In[5]:


df.plot(kind='bar',title='Bar Chart',figsize=(10,10),grid=True,legend = True)


# In[ ]:




