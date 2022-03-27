#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# # Read data set

# In[2]:


data=pd.read_csv('E:cars_data.csv')
data.head()


# # Null values

# In[3]:


data.isnull()


# In[4]:


data.isnull().sum()


# # bar graph
# 
# 
# 
# 

# In[49]:



data['Buyer Gender'].value_counts().plot(kind='bar',width =0.2,figsize=(5,5),color=['blue','green'],edgecolor='red');
plt.xlabel("Gender",labelpad=25)
plt.ylabel("Count of People",labelpad=25)
plt.title("Count of Male and Female Buyers",fontsize=15,y=1.02);
plt.ylim(4800,5100)


# # Topmost cars

# In[45]:


data1=data.sort_values(by=["Sale Price"],ascending=False)
print("Top 5 cars based on Sale Price are:")
data1.filter(['Model','Sale Price']).head()


# # Least Cars

# In[3]:



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('E:cars_data.csv')

data2=data.sort_values(by=["Resell Price"],ascending=False)
print("Least 5 cars based on Resell Price are:")
data2.filter(['Model','Resell Price']).tail()


# In[ ]:





# In[ ]:




