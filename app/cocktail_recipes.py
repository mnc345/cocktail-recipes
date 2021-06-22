import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

import random

# COCKTAIL_API = os.getenv("COCKTAIL_API")

def liquor_type():
    liquor = input("Please select a liquor type: ")
    if (liquor == "whiskey") or (liquor == "whisky") or (liquor == "brandy") or (liquor == "wine") or (liquor == "gin") or (liquor == "vodka") or (liquor == "tequila") or (liquor == "rum"):
        print(f"SELECTED LIQUOR: '{liquor}'")
    else:
        print("OOPS, invalid liquor type. Please try again.")
        exit()
    
    request_url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={liquor}"
    response = requests.get(request_url)
    liquor_data = json.loads(response.text)

    for l in (liquor_data["drinks"]):
        valid_options = [l["strDrink"]]
        cocktail_choice = random.choice(valid_options)
        print("Cocktail choice:", cocktail_choice)
       #print(valid_options)

liquor_type()




# import webbrowser
# def cocktails():
#     cocktail_type = input("please select type of cocktail: ")
#     request_url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail_type}"
#     data = requests.get(request_url)
#     tt = json.loads(data.text)
    
    
#     for i in (tt["drinks"]):
#         print(i["strDrink"], "\n")
#         print(i["strInstructions"], "\n")
        
#         print(i["strIngredient1"])
#         print(i["strIngredient2"])
#         print(i["strIngredient3"])
#         print(i["strIngredient4"])
#         url = i["strDrinkThumb"]
#         webbrowser.open(url)
# cocktails()