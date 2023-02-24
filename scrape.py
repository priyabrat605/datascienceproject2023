#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import requests
from bs4 import BeautifulSoup as soup
import numpy as np
     


# In[46]:


headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}
requests.get('https://economictimes.indiatimes.com/',headers=headers).text


# In[49]:


webpage=requests.get('https://economictimes.indiatimes.com/')


# In[50]:


eco=soup(webpage.content,'lxml')
eco


# In[58]:


for link in eco.findAll('h2'):
    print("Headline: {}".format(link.text))


# In[60]:


for news in eco.findAll('article',{'class':'newsList flt w-100'}):
    print(news.text.strip())


# In[67]:


eco.find_all("span", {"class":"subheader_wrapper hide"})


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[29]:


soup=BeautifulSoup(webpage,'lxml')


# In[30]:


print(soup.prettify())


# In[40]:


soup.find_all('h1')[0].text


# In[42]:


for i in soup.find_all('h1'):
  print(i.text.strip())


# In[33]:


for i in soup.find_all('p'):
  print(i.text.strip())


# In[34]:


len(soup.find_all('p',class_='rating'))


# In[ ]:





# In[ ]:





# In[ ]:





# In[16]:


company=soup.find_all('div',class_='company-content-wrapper')


# In[17]:


len(company) 


# In[18]:


name=[]
rating=[]
reviews=[]
ctype=[]
hq=[]
how_old=[]
no_of_employee=[]

for i in company:

  name.append(i.find('h2').text.strip())
  rating.append(i.find('p',class_='rating').text.strip())
  reviews.append(i.find('a' , class_='review-count').text.strip())
  ctype.append(i.find_all('p',class_='infoEntity')[0].text.strip())
  hq.append(i.find_all('p',class_='infoEntity')[1].text.strip())
  how_old.append(i.find_all('p',class_='infoEntity')[2].text.strip())
  no_of_employee.append(i.find_all('p',class_='infoEntity')[3].text.strip())

df=pd.DataFrame({'name':name,
   'rating':rating,
   'reviews':reviews,
   'company_type':ctype,
   'Head_Quarters':hq,
   'Company_Age':how_old,
   'No_of_Employee':no_of_employee,
   })
  


# In[19]:


name


# In[20]:


rating


# In[ ]:





# In[22]:


final=pd.DataFrame()
for j in range(1,1001):
  webpage=requests.get('https://economictimes.indiatimes.com/'.format(j)).text
  soup=BeautifulSoup(webpage,'lxml')
  company=soup.find_all('div',class_='company-content-wrapper')
  name=[]
  rating=[]
  reviews=[]
  ctype=[]
  hq=[]
  how_old=[]
  no_of_employee=[]

  for i in company:

    try:
       name.append(i.find('h2').text.strip())
    except:
       name.append(np.nan)

    try:
       rating.append(i.find('p',class_='rating').text.strip())
    except:
       rating.append(np.nan)
   
    try:

      reviews.append(i.find('a' , class_='review-count').text.strip())
    except:
      reviews.append(np.nan)

    try:

      ctype.append(i.find_all('p',class_='infoEntity')[0].text.strip())
    except:
      ctype.append(np.nan)
    try:

      hq.append(i.find_all('p',class_='infoEntity')[1].text.strip())
    except:
      hq.append(np.nan)
    
    try:

      how_old.append(i.find_all('p',class_='infoEntity')[2].text.strip())
    except:
      how_old.append(np.nan)
    try:
      no_of_employee.append(i.find_all('p',class_='infoEntity')[3].text.strip())
    except:
      no_of_employee.append(np.nan)
    

  df=pd.DataFrame({'name':name,
    'rating':rating,
    'reviews':reviews,
    'company_type':ctype,
    'Head_Quarters':hq,
    'Company_Age':how_old,
    'No_of_Employee':no_of_employee,
    })
  
  final=final.append(df,ignore_index=True)


# In[26]:


df.


# In[24]:


df.shape


# In[25]:


final.shape


# In[ ]:




