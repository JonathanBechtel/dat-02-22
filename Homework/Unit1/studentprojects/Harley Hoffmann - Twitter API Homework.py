#!/usr/bin/env python
# coding: utf-8

# In[59]:


#importing requests package and tokens
import requests
from requests_oauthlib import OAuth1
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YWh5zjx5AqkzQucesPJd1Ffx8', 'DMVLJ5GkzqcWVo4LncuuMbPN79KotuTAp3W88ApmnLKtAOLFD5',
                  '74691997-AzJ7dR2NJRujEMTXEpnHs7vFXsCUUNSkeWozJJEec', 'XJEjNAtj5FjnpUi26e3LPERj5yE1j4oFPA7lpT8M2Ybvb')


# In[60]:


import pandas as pd


# In[61]:


req = requests.get(url, auth=auth)


# In[26]:


##### Function 1


# In[142]:


def find_user(screen_name, keys):
#create a dictionary to output values with entered keys and make json blob easier to work with
    returned_dict = {}
    user_objects = requests.get(f'https://api.twitter.com/1.1/users/lookup.json?screen_name={screen_name}', auth=auth)        
    user_objects_json = user_objects.json()
    for character in screen_name:
#check to remove @ if included
        if character == '@':
            screen_name.replace('@','')
#check to see if keys list value is empty or not
    if not keys:
        return user_objects_json
    else:
#if keys list is not empty then add the value of that key to the dictionary
        for key in keys:
            returned_dict[key] = user_objects_json[0][key]
        return returned_dict


# In[143]:


find_user('GA',['name','screen_name','followers_count','friends_count'])


# In[144]:





# In[ ]:


##### Function 2


# In[132]:


def find_hashtag(hashtag, count=None, search_type=None):
    hashtag_search = requests.get(f'https://api.twitter.com/1.1/search/tweets.json?q=%23{hashtag}&count={count}&result_type={search_type}', auth=auth)
    hashtag_search_json = hashtag_search.json()
    for character in hashtag:
#actually checking to remove hashtag because we've added %23 to the url above so we already have the hashtag
        if character == '#':
            hashtag.replace('#','')
#return the json for each of the parameters listed in the definition statement
    return hashtag_search_json

    


# In[140]:


find_hashtag('DataScience', 20, 'mixed')


# In[10]:





# In[104]:





# In[ ]:


##### Function 3


# In[171]:


def get_followers(screen_name, keys, to_df: bool):
    list_of_followers = []
    user_followers = requests.get(f'https://api.twitter.com/1.1/followers/list.json?screen_name={screen_name}', auth=auth)
    user_followers_json = user_followers.json()
    for character in screen_name:
#check to remove @ if included
        if character == '@':
                screen_name == screen_name.replace('@','')
#grabbing all the user objects in the list, separately, and then grabbing each key that match the inputs
#this is similar to question 1 but just a list of many users, so we have to do a double for loop
    for user in user_followers_json['users']:
# create a new single user since each user in nested in users and match the keys from the keys input
        single_user = {}
        for key in keys:
            single_user[key] = user[key]
# Now add the single user to the list of followers and continue looping through each user in users
        list_of_followers.append(single_user)
#if df is true, then put the result in a dataframe
    if to_df == True:
        return pd.DataFrame(list_of_followers)
    else:
        return list_of_followers
    
    
    
    
    
    
    


# 

# In[172]:


import pandas as pd
get_followers('GA', ['screen_name','followers_count'], to_df=True)


# In[110]:


user_followers_json


# In[ ]:





# In[ ]:




