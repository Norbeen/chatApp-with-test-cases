import json,random
from requests import *
from app import *
from google.auth.transport import requests
import google.auth.transport.requests
def yelp_api():
    
    api_key = 'rT9VSegJs8wVNjfYsEq2_qkY_3-m4qh3H_9jThKO4r04rVc0hGWIzEPKyEtFQvIbv1wSdhdkP-zZeBiiZazTBK1E5osi5AUvp3dm4gxRFBWBU__jALfOxwLiaXpiXnYx'
    headers = {'Authorization': 'Bearer %s' % api_key}
 
    url = 'https://api.yelp.com/v3/businesses/search'

    params = {'term':'food','location':'baltimore'}
    
    req = request.get(url, params=params, headers=headers)
    print(req)
    parsed = json.loads(req.text)

    restaurant_name = []
    restaurant_url= []

    businesses = parsed["businesses"]
    
    for business in businesses:
        restaurant = business["name"]
        restaurant_name.append(restaurant)
    
        url = business["url"]
        restaurant_url.append(url)
    
    randomNum = random.randint(0,len(restaurant_name))
    
    resName = ("".join(restaurant_name[randomNum-1]))
    resUrl = ("".join(restaurant_url[randomNum-1]))
    return resName, resUrl