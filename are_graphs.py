#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd


# In[154]:


my_dict={'nbr_stars':[12,12,12,12,12],
        'to_BH':[55,55,55,55,55],
        'life_span':[8,8,8,8,8],
        'spawn_rate':[0.024,0.024,0.024,0.024,0.024],
        'nbr_BH1':[5,3,4,6,3],
        'temps(milliard d\'anees)':[1,2,3,4,5],
        'nbr_BH2':[4,6,6,4,2]}


# In[155]:


df=pd.DataFrame(data=my_dict)


# In[156]:


df.plot.line(figsize=(10,5),title='Nombre des trous noirs',x='temps(milliard d\'anees)',y=['nbr_BH1','nbr_BH2'],use_index='True')


# In[157]:


my_dict2={'nbr_BH2':[4,6,6,4,2],
          'nbr_BH3':[3,2,3,3,3],
         'temps(milliard d\'anees)':[1,2,3,4,5]}


# In[158]:


df=pd.DataFrame(data=my_dict2)
df.plot.line(figsize=(10,5),title='Nombre des trous noirs',x='temps(milliard d\'anees)',y=['nbr_BH2','nbr_BH3'],use_index='True')


# In[159]:


my_dict3={'nbr_BH3':[3,2,3,3,3],
         'nbr_BH4':[2,3,5,0,2],
         'temps(milliard d\'anees)':[1,2,3,4,5]}


# In[160]:


df=pd.DataFrame(data=my_dict3)
df.plot.line(figsize=(10,5),title='Nombre des trous noirs',x='temps(milliard d\'anees)',y=['nbr_BH3','nbr_BH4'],use_index='True')


# In[161]:


my_dict4={'nbr_BH4':[2,3,5,0,2],
          'nbr_BH5':[3,0,2,2,0],
         'temps(milliard d\'anees)':[1,2,3,4,5]}


# In[162]:


df=pd.DataFrame(data=my_dict4)
df.plot.line(figsize=(10,5),title='Nombre des trous noirs',x='temps(milliard d\'anees)',y=['nbr_BH4','nbr_BH5'],use_index='True')


# In[163]:


my_dict5={'nbr_BH5':[3,0,2,2,0],
          'nbr_BH6':[3,4,2,4,4],
         'temps(milliard d\'anees)':[1,2,3,4,5]}


# In[164]:


df=pd.DataFrame(data=my_dict5)
df.plot.line(figsize=(10,5),title='Nombre des trous noirs',x='temps(milliard d\'anees)',y=['nbr_BH5','nbr_BH6'],use_index='True')


# In[ ]:





# In[ ]:




