import json,random
import requests 



def yelp_api():
    
    api_key = 'rT9VSegJs8wVNjfYsEq2_qkY_3-m4qh3H_9jThKO4r04rVc0hGWIzEPKyEtFQvIbv1wSdhdkP-zZeBiiZazTBK1E5osi5AUvp3dm4gxRFBWBU__jALfOxwLiaXpiXnYx'
    headers = {'Authorization': 'Bearer %s' % api_key}
 
    url = 'https://api.yelp.com/v3/businesses/search'

    params = {'term':'food','location':'baltimore'}
    
    req = requests.get(url, params=params, headers=headers)
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
    return resName + " " + resUrl
    
def Bot(name, message):
  
    if message == "!! say something":
        message = "Hello, welcome to the chatroom. I am Jarvis, here to help you!"
    elif message == "!! about":
         message = "Hi, I am Jarvis. I was designed by Nabin in Maryland for this project."
    elif message == "!! help":
        message = "Commands: '!! about','!! say something','!! source','!! developer'"
    elif message == "!! source":
        message = "To find the source code of this web-app, visit the github.com/norbeen tab at the top the page."
    elif message == "!! developer":
        message = "I was designed by Nabin for his project. Want to know more about him? Visit github.com/norbeen."
    elif message == "!! Jarvis food near me" or message == "!! Jarvis food":
          message = yelp_api()
          name = "Jarvis"
    else:
        message= "Sorry! I am unable to answer this question. Type '!! help' to see the lists of commands."
    return name, message


# name= "nabin"
# message= "!! Jarvis food"
# print(Bot(name, message)) 