#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install numpy')


# In[6]:


get_ipython().system('pip install pandas')


# In[5]:


get_ipython().system('pip install matplotlib')


# In[8]:


get_ipython().system('pip install seaborn')


# In[10]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[18]:


df = pd.read_csv(r'C:\Users\Mithu Bhaskar\Downloads\Diwali Sales Data.csv', encoding='unicode_escape')


# In[20]:


df.shape


# In[22]:


df.head(10)


# In[23]:


df.info()


# In[24]:


#drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[25]:


df.info()


# In[26]:


pd.isnull(df)


# In[27]:


#check for null values
pd.isnull(df).sum()


# In[28]:


df.shape


# In[30]:


#drop null values
df.dropna(inplace=True)


# In[31]:


df.shape


# In[32]:


#change data type
df['Amount']= df['Amount'].astype('int')


# In[33]:


df['Amount'].dtypes


# In[34]:


df.info()


# In[36]:


df.columns


# In[37]:


#rename column
df.rename(columns={'Marital_Status':'Saadi'})


# In[40]:


df.describe()


# In[41]:


#use describe for specific column
df[['Age','Orders','Amount']].describe()


# # Exploraatory Data Analysis

# Gender

# In[43]:


df.columns


# In[44]:


ax = sns.countplot(x='Gender', data=df)

for bars in ax.containers:
    ax.bar_label(bars)


# In[48]:


sales_gen = df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by ='Amount', ascending=False)

sns.barplot(x='Gender',y='Amount', data= sales_gen)


# From above graphs we can see that most of the buyers are females and even the purchasing power of females are greater than men

# Age

# 

# In[49]:


df.columns


# In[52]:


ax = sns.countplot(data = df, x= 'Age Group', hue='Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[53]:


# Total amount vs Age group
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x='Age Group', y='Amount', data=sales_age)


# From above bargraphs we can see that most of the buyers are of age group between 26-35 yrs female

# State

# In[54]:


df.columns


# In[55]:


sales_state = df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data =sales_state, x='State',y='Orders')


# From above graphs we can see that most of the orders and total sales/amount are from UP, Maharastra & Karnataka respectively

# In[56]:


df.columns


# Marital Status

# In[61]:


ax = sns.countplot(data=df, x='Marital_Status')
sns.set(rc={'figure.figsize':(5,5)})

for bars in ax.containers:
    ax.bar_label(bars)


# In[62]:


sales_state = df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)
sns.barplot(data=sales_state, x='Marital_Status',y='Amount', hue='Gender')


# *From above graphs we can see that most of the buyers are married(women) and they have high purchasing power

# *Occupation

# In[63]:


df.columns


# In[67]:


sns.set(rc={'figure.figsize':(20,5)})

ax = sns.countplot(data=df, x='Occupation')
for bars in ax.containers:
    ax.bar_label(bars)


# In[69]:


sales_state=df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(data=sales_state, x='Occupation', y='Amount')


# *from above graphs we can see that most of the buyers are working in IT , Healthcare and Aviation sector

# Product Category

# In[73]:


ax= sns.countplot(data=df, x='Product_Category')
sns.set(rc={'figure.figsize':(20,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[81]:


sales_state=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set('figure.figsize')

sns.barplot(data=sales_state, x='Product_Category', y='Amount')
                                                                                


# *From above graphs we can see that most of the sold products are from food, footwear & Electronics category*

# In[82]:


sales_state = df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x= 'Product_ID',y='Orders')


# In[ ]:




