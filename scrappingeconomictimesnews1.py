#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np
     


# In[20]:


url='https://economictimes.indiatimes.com/tech/newsletters/ettech-unwrapped/edtech-ma-talks-gain-momentum-amid-a-prolonged-funding-crunch/articleshow/98221912.cms'


# In[21]:


page=requests.get(url)


# In[22]:


page.content


# In[26]:


eco=BeautifulSoup(page.content,'html.parser')


# In[27]:


eco


# In[ ]:





# In[28]:


news_summary1=eco.find(attrs={'class':'mainText'}).text


# In[29]:


print(news_summary1)


# In[30]:


news_headings=eco.find(attrs={'class':'mainHeadText'}).text


# In[31]:


print(news_headings)


# In[32]:


data=[[url,news_headings,news_summary1]]


# In[33]:


df=pd.DataFrame(data,columns=['url','news_headings','news_summary1'])


# In[34]:


df


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




