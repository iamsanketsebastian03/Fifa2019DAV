#!/usr/bin/env python
# coding: utf-8

# In[30]:


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = 'dark')
import random
from collections import Counter as counter


# In[2]:


fifa_df = pd.read_csv("Downloads/data.csv")


# In[3]:


fifa_df.info()


# In[4]:


fifa_df.head()


# In[5]:


fifa_df.columns


# In[6]:


useful_features = ['Name',
                   'Age',
                   'Photo', 
                   'Nationality', 
                   'Flag',
                   'Overall',
                   'Potential', 
                   'Club', 
                   'Club Logo', 
                   'Value',
                   'Wage',
                   'Preferred Foot',
                   'International Reputation',
                   'Weak Foot',
                   'Skill Moves',
                   'Work Rate',
                   'Body Type',
                   'Position',
                   'Joined', 
                   'Contract Valid Until',
                   'Height',
                   'Weight',
                   'Crossing', 
                   'Finishing',
                   'HeadingAccuracy',
                   'ShortPassing', 
                   'Volleys', 
                   'Dribbling',
                   'Curve',
                   'FKAccuracy',
                   'LongPassing',
                   'BallControl',
                   'Acceleration',
                   'SprintSpeed',
                   'Agility',
                   'Reactions', 
                   'Balance',
                   'ShotPower', 
                   'Jumping',
                   'Stamina', 
                   'Strength',
                   'LongShots',
                   'Aggression',
                   'Interceptions',
                   'Positioning', 
                   'Vision', 
                   'Penalties',
                   'Composure',
                   'Marking',
                   'StandingTackle', 
                   'SlidingTackle',
                   'GKDiving',
                   'GKHandling',
                   'GKKicking',
                   'GKPositioning',
                   'GKReflexes']


# In[7]:


df = pd.DataFrame(fifa_df , columns = useful_features)


# In[8]:


# find the age distribution

plt.figure(1, figsize=(18, 7))
sns.countplot( x= 'Age', data=df, palette='Accent')
plt.title('Age distribution of all players')


#                                  It seems most of the age is distributed form 19 ~ 30

# In[13]:


#We can examine the relationship between age and overall with scatter plot.

df.plot(kind="scatter", x="Age", y="Overall", color="green", alpha="0.1", figsize=(10,10))
plt.xlabel("Age")
plt.ylabel("Overall")
plt.title("Age-Overall Scatter Plot")


# From Age-Overall Scatter Plot, we can evidence that points:
# 
# At age 20, players overall rankings nearly 60-62.
# At age 25, players overall rankings mainly at 69-72.
# Generally players overall rankings increasing due to age until 29. After this age players overall rankings are reducing.

# In[17]:


# handle all the players

def preprocess_value(x):
    x = str(x).replace('€', '')
    if('M' in str(x)):
        x = str(x).replace('M', '')
        x = float(x) * 1000000
    elif('K' in str(x)):
        x = str(x).replace('K', '')
        x = float(x) * 1000
    return float(x)

df['Value'] = df['Value'].apply(preprocess_value)


# In[18]:


# find the most expensive players

df.sort_values(by='Value', ascending=False)[['Name','Nationality', 'Club', 'Position', 'Overall', 'Value']].head(5)


# In[19]:


# which club has the highest total value 

club_values =df.groupby('Club')['Value'].sum()
club_values.sort_values(ascending=False).head(5)


# In[35]:


# different positions acquired by the players 

plt.figure(figsize = (12, 8))
sns.set(style = 'dark',color_codes = True)
ax = sns.countplot('Position', data = df, palette = 'inferno_r')
ax.set_xlabel(xlabel = 'Different Positions in Football', fontsize = 16)
ax.set_ylabel(ylabel = 'Count of Players', fontsize = 16)
ax.set_title(label = 'Comparison of Positions and Players', fontsize = 20)
plt.show()


# In[31]:


plt.figure(1 , figsize = (15 , 7))
countries = []
c = counter(df['Nationality']).most_common()[:11]
for n in range(11):
    countries.append(c[n][0])

sns.countplot(x  = 'Nationality' ,
              data = df[df['Nationality'].isin(countries)] ,
              order  = df[df['Nationality'].isin(countries)]['Nationality'].value_counts().index , 
             palette = 'rocket') 
plt.xticks(rotation = 90)
plt.title('Maximum number footballers belong to which country' )
plt.show()


#                                       England has maximum numbers of players.

# In[37]:


# To show Different Work rate of the players participating in the FIFA 2019

plt.figure(figsize = (15, 8))
sns.countplot(x = 'Work Rate', data = df, palette = 'hls')
plt.title('Different work rates of the Players Participating in the FIFA 2019', fontsize = 20)
plt.xlabel('Work rates associated with the players', fontsize = 16)
plt.ylabel('count of Players', fontsize = 16)
plt.show()


# In[39]:


# best players per each position with their age, club, and nationality based on their overall scores

df.iloc[df.groupby(df['Position'])['Overall'].idxmax()][['Position', 'Name', 'Age', 'Club', 'Nationality']]


# In[ ]:




