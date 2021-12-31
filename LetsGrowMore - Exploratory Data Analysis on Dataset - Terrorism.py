#!/usr/bin/env python
# coding: utf-8

# ## Task Name: Exploratory Data Analysis on Dataset - Terrorism || December 2021
# ## Perform by : PULIVARTHI VENKATA BHARATH KUMAR
# ## Importing Libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("D:\GROWMORE\globalterrorismdb_0718dist.csv",encoding='latin1')
print(data)


# In[2]:


data.head()


# In[3]:


data.tail()


# In[4]:


data.shape


# In[5]:


data.describe()


# In[6]:


data.corr()


# In[7]:


data.columns.values


# In[8]:


data.nunique()


# In[9]:


data.dtypes


# In[10]:


#check nulls
data.isnull()


# In[11]:


data.isnull().sum()


# In[12]:


data['nkill']=data['nkill'].fillna(0)
data['nwound']=data['nwound'].fillna(0)


# In[13]:


data['Casualities'] = data['nkill'] + data['nwound']


# In[14]:


data.isnull().sum()


# In[15]:


data.head()


# In[16]:


year = data['iyear'].unique()
years_count = data['iyear'].value_counts(dropna = False).sort_index()
plt.figure(figsize = (15,10))
sns.barplot(x = year, y = years_count, palette = 'tab10')
plt.xticks(rotation = 50)
plt.xlabel('Attacking Year',fontsize=20)
plt.ylabel('Number of Attacks Each Year',Fontsize=20)
plt.title('Attacks In Years',fontsize=22)
plt.show()


# ####  Here, The graph shows the number of Attacks in each year from 1970 to 1992 and here we observed that the number of global terrorism attacks are continuously increasing from 1988 . The Graph shows 1991 is the most unlucky year because the most number of attacks took place in the year 1991.

# In[17]:


Data = data[['iyear','nkill']].groupby(['iyear']).sum()
fig, ax4 = plt.subplots(figsize=(20,10))
Data.plot(kind='bar',alpha=0.7,ax=ax4, color="green")
plt.xticks(rotation = 50)
plt.title("People Died Due To Attack",fontsize=25)
plt.ylabel("Number of killed peope",fontsize=20)
plt.xlabel('Year',fontsize=20)
top_side = ax4.spines["top"]
top_side.set_visible(False)
right_side = ax4.spines["right"]
right_side.set_visible(False)


# The graph shows the number of people killed from the year 1970 to 1992. As number of attacks increases, the people killed in attacks is also increases. The number of killed people is atmost in 1984

# In[18]:


data['gname'].value_counts().to_frame().drop('Unknown').head(10).plot(kind='bar',color='yellow',figsize=(20,10))
plt.title("Top 10 terrorist group attack",fontsize=25)
plt.xlabel("terrorist group name",fontsize=20)
plt.ylabel("Attack number",fontsize=20)
plt.show()


# Here the graph shows the top 10 terrorist group attacks and Taliban is the most active terrorist group followed by the others.

# In[19]:


data['country_txt'].value_counts().to_frame().sort_values('country_txt',axis=0,ascending=False).head(10).plot(kind='bar',color='blue',figsize=(20,10))
plt.title("Top 10 Attacked Countries",fontsize=25)
plt.xticks(rotation = 50)
plt.xlabel("Country Name",fontsize=20)
plt.ylabel("Attack number",fontsize=20)
plt.show()


# In[20]:


data['attacktype1_txt'].value_counts().plot(kind='bar',figsize=(20,10),color='orange')
plt.xticks(rotation = 50)
plt.xlabel("Attack Type",fontsize=20)
plt.ylabel("Number of attack",fontsize=20)
plt.title("Name of attacktype",fontsize=25)
plt.show()


# #### The Graph shows that which type of attack is mostly used. Here we observed that the Bombing/Explosion type attack were used most of time.

# In[21]:


plt.subplots(figsize=(20,10))
sns.countplot(data["targtype1_txt"],order=data['targtype1_txt'].value_counts().index,palette="gist_heat",edgecolor=sns.color_palette("Set2"));
plt.xticks(rotation=90)
plt.xlabel("Attacktype",fontsize=20)
plt.ylabel("count",fontsize=20)
plt.title("Type of attack",fontsize=25)
plt.show()


# Here we observed that Private Citizen and Property Attacks were more as compared to other attack types.

# In[22]:


kill = data.loc[:,'nkill']
print('Number of people killed by terror attack:', int(sum(kill.dropna())))


# In[23]:


df = data.pivot_table(columns='attacktype1_txt', values='nkill', aggfunc='sum')
df


# In[24]:


df1 = data.pivot_table(columns='country', values='nkill', aggfunc='sum')
df1


# In[25]:


#top 10 countries with most number of attacks
attack = data.country.value_counts()[:10]
attack


# In[26]:


#top 10 terrorist groups with most number of attacks
data.gname.value_counts()[1:11]


# ### Summary
# Highest number of attacks took place in 2014.
# 
# Leading to highest death rate in that year.
# 
# Taliban has done the hightest number of attacks out of all terrorist groups.
# 
# The highest number of attacks took place in Iraq.
# 
# The most frequent attack types were bombing/explosion.
# 
# These attacks affected provate citizens and propertiest the most

# In[ ]:




