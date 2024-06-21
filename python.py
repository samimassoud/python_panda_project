#!/usr/bin/env python
# coding: utf-8

# In[2]:


pwd


# In[3]:


pip install panda


# In[6]:


import pandas as pd


# In[7]:


df = pd.read_csv("chicago.csv")


# In[8]:


df.head()


# In[10]:


total_trip_duration = df['Trip Duration'].sum()
total_trip_duration


# In[12]:


average_trip_duration = df['Trip Duration'].mean()
average_trip_duration


# In[16]:


first_start_station = df['Start Station'].head(1)
first_start_station


# In[18]:


has_female_users = df['Gender'] == 'Female'
has_female_users


# In[21]:


has_female_users = 'Female' in df['Gender'].values
has_female_users 


# In[23]:


start_stations_list = df['Start Station'].tolist()
start_stations_list


# In[25]:


trip_durations = df['Trip Duration']


# In[27]:


summary_stats = (trip_durations.mean(), trip_durations.sum(), len(trip_durations))
summary_stats


# In[29]:


user_type_counts = df['Gender'].value_counts().to_dict()
user_type_counts


# In[30]:


unique_stations = set(df['Start Station'])
unique_stations


# In[31]:


total_duration = total_trip_duration 
average_duration = average_trip_duration
total_duration
average_duration


# In[32]:


long_trips = df[df['Trip Duration'] > 1000]
long_trips


# In[34]:


male_trips = df[(df['Gender'] == 'Male') & (df['Birth Year'] > 1990)]
male_trips


# In[36]:


df['Adjusted Duration'] = df['Trip Duration']
df['Adjusted Duration'] += 60
df['Adjusted Duration']


# In[37]:


df


# In[39]:


# Output results
print("Total Trip Duration:", total_trip_duration)


# In[41]:


print("Start Stations List:", start_stations_list[:5]) # Print first


# In[42]:


print("Summary Stats:", summary_stats)


# In[44]:


print("User Type Counts:", user_type_counts)
print("Unique Start Stations:", list(unique_stations)[:5]) # Print
print("Total Duration:", total_duration)
print("Average Duration:", average_duration)
print("Number of Long Trips:", len(long_trips))
print("Number of Male Trips by Users Born After 1990:",len(male_trips))
print("Sample Adjusted Durations:", df['Adjusted Duration'].head())


# In[45]:


df.to_csv('chicago_analysis_results.csv', index=False)


# In[ ]:




