#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


dataset=pd.read_csv("post.csv")


# In[ ]:





# In[3]:


dataset


# In[6]:


dataset.head(10)


# In[7]:


y=dataset.iloc[:,-1]


# In[8]:


x


# In[9]:


y.shape


# In[10]:


x=dataset.iloc[:,1:7]


# In[11]:


x.shape


# In[12]:


from sklearn.model_selection import train_test_split


# In[18]:


X_train, X_test, y_train, y_test = train_test_split (x, y, test_size=1/4, random_state=42)


# In[19]:


X_train


# In[20]:


X_test


# In[14]:


#from sklearn.preprocessing import LabelEncoder
#labelencoder_x=LabelEncoder()
#x_new=labelencoder_x.fit_transform(state)
#x_new
#x.iloc[:,-2]=x_new


# In[21]:


y_test


# In[17]:





# In[ ]:





# In[19]:





# In[ ]:





# In[22]:


from sklearn.linear_model import LinearRegression


# In[23]:


model=LinearRegression()


# In[24]:


model.fit(X_train,y_train)


# In[29]:


import matplotlib.pyplot as plt


# In[30]:


plt.scatter(X_test,y_test)


# In[35]:


model.predict(X_test)


# In[34]:


y_test


# In[36]:


for x in y_test:
    if x==0:
        print("inform his close friends and relatives")
    elif x==1:
        print("inform all the friends and relatives ")
    elif x==2:
        print("quick action to be taken ")


# In[ ]:




