#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("mushroom.csv",engine='python')


# In[3]:


df.head()


# In[4]:


df.shape


# In[6]:


df.isnull().sum()


# In[8]:


sns.countplot(x='class', data=df, palette="mako_r")
plt.xlabel("claas")
plt.show()


# In[9]:


plt.style.use('dark_background')
plt.rcParams['figure.figsize']=8,8 
s = sns.countplot(x = "class", data = df)
for p in s.patches:
    s.annotate(format(p.get_height(), '.1f'), 
               (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha = 'center', va = 'center', 
                xytext = (0, 9), 
                textcoords = 'offset points')
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




