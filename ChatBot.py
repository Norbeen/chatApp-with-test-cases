import json, random
import requests 


jokeList = [
    ["Did you hear the one about the guy with the broken hearing aid? Neither did he."],
    ["What do you call a fly without wings? A walk."],
    ["When my wife told me to stop impersonating a flamingo, I had to put my foot down."],
    ["What do you call someone with no nose? Nobody knows."],
    ["What time did the man go to the dentist? Tooth hurt-y."],
    ["Why can’t you hear a pterodactyl go to the bathroom? The p is silent."],
    ["How many optometrists does it take to change a light bulb? 1 or 2? 1... or 2?"],
    ["I was thinking about moving to Moscow but there is no point Russian into things."],
    ["Why does Waldo only wear stripes? Because he doesn't want to be spotted."],
    ["Do you know where you can get chicken broth in bulk? The stock market."],
    ["I used to work for a soft drink can crusher. It was soda pressing."],
    ["A ghost walks into a bar and asks for a glass of vodka but the bar tender says, “sorry we don’t serve spirits”"],
    ["I went to the zoo the other day, there was only one dog in it. It was a shitzu."],
    ["I gave all my dead batteries away today, free of charge."],
    ["Why are skeletons so calm? Because nothing gets under their skin."],
    ["There’s a new type of broom out, it’s sweeping the nation."],
    ["Why don’t seagulls fly over the bay? Because then they’d be bay-gulls!"],
    ["What did celery say when he broke up with his girlfriend? She wasn't right for me, so I really don't carrot all"],
    ["Q: What’s 50 Cent’s name in Zimbabwe? A: 400 Million Dollars."],
    ["What's the worst thing about ancient history class? The teachers tend to Babylon."]
        ]
        
randNum = random.randint(0,len(jokeList)-1)


api_key = 'rT9VSegJs8wVNjfYsEq2_qkY_3-m4qh3H_9jThKO4r04rVc0hGWIzEPKyEtFQvIbv1wSdhdkP-zZeBiiZazTBK1E5osi5AUvp3dm4gxRFBWBU__jALfOxwLiaXpiXnYx'
headers = {'Authorization': 'Bearer %s' % api_key}
 
url = 'https://api.yelp.com/v3/businesses/search'
params = {'term':'food','location':'baltimore'}

req = requests.get(url, params=params, headers=headers)
parsed = json.loads(req.text)

restaurant_name = []
restaurant_url= []

businesses = parsed["businesses"]
    
for business in businesses:
    restaurant = business["name"]
    restaurant_name.append(restaurant)
    
    url = business["url"]
    restaurant_url.append(url)
    
    Rand = random.randint(0,len(restaurant_name)-1)
    
    resName = ("".join(restaurant_name[Rand-1]))
    resUrl = ("".join(restaurant_url[Rand-1]))
    
def Bot(name, message):
  
    if message == "!! say something":
        message = "Hello, welcome to the chatroom. I am Jarvis, here to help you!"
    elif message == "!! about":
         message = "Hi, I am Jarvis. I was designed by Nabin in Maryland for this project."
    elif message == "!! help":
        message = "Commands: '!! about','!! say something','!! source','!! developer', '!! Jarvis food near me', '!! Jarvis food','!! Make me happy', '!! jokes', '!! humor'"
    elif message == "!! source":
        message = "To find the source code of this web-app, visit the github.com/norbeen tab at the top the page."
    elif message == "!! developer":
        message = "I was designed by Nabin for his project. Want to know more about him? Visit github.com/norbeen."
    elif message == "!! Jarvis food near me" or message == "!! Jarvis food":
          message = resName + " " + resUrl
          name = "Jarvis"
    elif message == "!! jokes":
         message = jokeList[randNum]
    elif message == "!! humor":
         message = jokeList[randNum]
    elif message == "!! Make me happy":
        message = jokeList[randNum]
    else:
        message= "Sorry! I am unable to answer this question. Type '!! help' to see the lists of commands."
    return name, message


# name= "nabin"
# message= "!! Jarvis food"
# print(Bot(name, message)) 