#!/usr/bin/env python
# coding: utf-8

# In[1]:


# FURTHER DATA EXPLORATION
import pandas as pd
import numpy as np


# In[2]:


Births = pd.read_csv("C:/Users/Ayieko/Documents/MACHINE LEARNING TUTORIALS/soon/NCHS_-_U.S._and_State_Trends_on_Teen_Births.csv")
print(Births)


# In[3]:


Births.head(10)


# In[ ]:





# In[17]:


# let's apply the pivot syntax
Births.pivot_table('State Rate', index='State', columns='Year')


# In[16]:


Births.groupby(['State', 'State Rate'])['U.S. Birth Rate'].aggregate('mean').unstack()
### we passed the pivots tables by hand
# we selected state rate by state, applied the mean aggregate, combined the resulting groups


# In[15]:


Births.groupby(['State Births', 'State Rate'])['U.S. Birth Rate'].aggregate('mean').unstack()
### we passed the pivots tables by hand
##### we selected states births, birth rate against U.S. birth rate
######## we calculated the aggregate mean


# In[8]:


## we can apply the pivot table to understand the data
## random manipulation using the pivot table
Births.groupby('State Rate')[['Unit']].mean()


# In[ ]:





# In[ ]:





# In[ ]:




