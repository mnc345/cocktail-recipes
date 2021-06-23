import os
from dotenv import load_dotenv

from requests.models import encode_multipart_formdata

import requests
import json

load_dotenv()

import random 


# COCKTAIL_API = os.getenv("COCKTAIL_API") -- NOT SURE WE NEED THIS

def liquor_type():
    liquor = input("Please select a liquor type: ").lower()
    valid_selections = ["whiskey", "whisky", "beer", "port", "vermouth", "everclear", "absinthe", "cider", "brandy", "aperol", "wine", "gin", "vodka", "rum", "tequila"]
    if liquor not in valid_selections:
        print("OOPS, invalid liquor type. Please try again.")
        exit()
    else:
        print(f"SELECTED LIQUOR: '{liquor}'")
        
    
    request_url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={liquor}"
    response = requests.get(request_url)
    liquor_data = json.loads(response.text)

    drinks = liquor_data["drinks"]

    while True:
        random_drink = random.choice(drinks)
        print("*Cocktail choice:",random_drink["strDrink"])

        user_choice = input("Do you want this type of cocktail? If so, type 'yes' If no, hit enter: ").lower()
        if  user_choice == "yes":
            break

    drink_id = random_drink["idDrink"]

    request_url_id = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drink_id}"
    id_response = requests.get(request_url_id)
    id_data = json.loads(id_response.text)

    for i in (id_data["drinks"]):
        print(i["strInstructions"], "\n")
        print(i["strIngredient1"])
        print(i["strIngredient2"])
        print(i["strIngredient3"])
        print(i["strIngredient4"])
        print(i["strIngredient5"])
        print(i["strIngredient6"])
        print(i["strIngredient7"])
        print(i["strIngredient8"])
        print(i["strIngredient9"])

liquor_type()

# # import webbrowser
# # def cocktails():
# #     cocktail_type = input("please select type of cocktail: ")
# #     request_url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail_type}"
# #     data = requests.get(request_url)
# #     tt = json.loads(data.text)
    
    
# #     for i in (tt["drinks"]):
# #         print(i["strDrink"], "\n")
# #         print(i["strInstructions"], "\n")
        
# #         print(i["strIngredient1"])
# #         print(i["strIngredient2"])
# #         print(i["strIngredient3"])
# #         print(i["strIngredient4"])
# #         url = i["strDrinkThumb"]
# #         webbrowser.open(url)
# # cocktails()
