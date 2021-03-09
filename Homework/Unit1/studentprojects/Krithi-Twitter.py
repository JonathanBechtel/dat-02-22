#Twitter API homework

import requests
from requests_oauthlib import OAuth1 
import pandas as pd

auth_token = OAuth1('2OusxJeTbxUR4vkQYoZGtddOn', 'UhLUw0XAJY9rIKhiWwwLv95ihm640RICQwwuxvLdjML4keVsU1',
             '1366799032350253056-N0r1Z3QDrEeo6nEmfEvvcLXXfoCBhN', 'DJpmMZEWGlRXzyAHJ5AsKPLie8bkO47kolwDFZ0rraxlW')


def find_user(screen_name, keys=[]):
    name = screen_name.replace('@','')
 
    base_url = 'https://api.twitter.com/1.1/users/show.json'
    user = requests.get(f"{base_url}?screen_name={name}", auth=auth_token).json()

    if keys:
        user = {k : user[k] for k in keys}

    return user


def find_hashtag(hashtag, count=None, search_type=None):
    base_url = 'https://api.twitter.com/1.1/search/tweets.json'

    if hashtag[0] == '#':
        hashtag = hashtag[1:]

    params='?q=%23'+hashtag
    
    if count:
        params += f"&count={count}"   
    if search_type:
        params += f"&result_type={search_type}"   

    search_url = base_url+params
    print(search_url)
    
    tweets = requests.get(search_url, auth=auth_token).json()['statuses']
   
    return tweets


def get_followers(screen_name, keys=['name', 'followers_count', 'friends_count', 'screen_name'], to_df=False):
    name = screen_name.replace('@','')
 
    base_url = 'https://api.twitter.com/1.1/followers/list.json'
    resp = requests.get(f"{base_url}?screen_name={name}", auth=auth_token).json()

    followers = resp['users']
    
    follower_list = []
    for user in followers:
        user_dict = {key: user[key] for key in keys} 
        follower_list.append(user_dict)

    if to_df:
        return(pd.DataFrame(follower_list))

    return follower_list

# u = find_user('@GA')
# u = find_user('GA')
# u = find_user('GA', ['name', 'screen_name', 'followers_count', 'friends_count'])
# print(u)

# res = find_hashtag('#DataScience')
# res = find_hashtag('DataScience', count=2, search_type='popular')
# print(res)

# res = get_followers('GA', ['name', 'screen_name', 'followers_count', 'friends_count'], True)
# print(res)

                            