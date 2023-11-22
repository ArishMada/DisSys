#!/usr/bin/env python
# coding: utf-8

# In[56]:


import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import classification_report, accuracy_score
from sklearn import metrics


# In[57]:


df = pd.read_csv('inventory1.csv')




# In[58]:


df.drop('ProductName', axis=1, inplace=True)


# In[59]:


X = df.iloc[:, :-1]
y = df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=0)


# In[60]:


X_train


# In[61]:


y_train


# In[62]:


X_test


# In[63]:


y_test


# In[64]:


nbc = GaussianNB()


# In[65]:


nbc.fit(X_train,y_train)


# In[66]:


y_pred = nbc.predict(X_test)
mislabel = np.sum((y_test!=y_pred))
print("Total number of mislabelled data points from {} test samples is {}".format(len(y_test),mislabel))


# In[67]:


print("The classification report is as follows...\n")
print(y_pred)


# In[72]:


print("Accuracy: ",metrics.accuracy_score(y_test,y_pred))


# In[ ]:




