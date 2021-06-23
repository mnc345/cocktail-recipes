import os
from dotenv import load_dotenv

from requests.models import encode_multipart_formdata
import requests
import random
import webbrowser
import json

load_dotenv()



# SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY") -- FOR SENDGRID
# SENDER_EMAIL_ADDRESS = os.getenv("SENDER_EMAIL_ADDRESS") -- FOR SENDGRID

def liquor_type():
    liquor = input("Please select a liquor type: ").lower()
    valid_selections = ["whiskey", "whisky", "beer", "port", "vermouth", "everclear", "absinthe", "cider", "brandy", "aperol", "wine", "gin", "vodka", "rum", "tequila"]
    if liquor not in valid_selections:
        print("OOPS! Invalid liquor type. Please try again.")
        exit()
    else:
        print(f"Selected liquor: '{liquor}'")
        print("\n")
        
    
    request_url = f"https://www.thecocktaildb.com/api/json/v1/1/filter.php?i={liquor}"
    response = requests.get(request_url)
    liquor_data = json.loads(response.text)

    drinks = liquor_data["drinks"]

    while True:
        random_drink = random.choice(drinks)
        print("Cocktail choice:",random_drink["strDrink"])

        user_choice = input("Do you want this type of cocktail? If so, type 'yes' If no, hit 'enter': ").lower()
        if  user_choice == "yes":
            break
            
            print("\n")
    
    drink_id = random_drink["idDrink"]

    request_url_id = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drink_id}"
    id_response = requests.get(request_url_id)
    id_data = json.loads(id_response.text)
    
    print("\n")
    print("Instructions: ")

    for i in (id_data["drinks"]):
        print(i["strInstructions"], "\n")

        
        print("Ingredients: ")
        print(i["strIngredient1"])
        print(i["strIngredient2"])
        print(i["strIngredient3"])
        print(i["strIngredient4"])
        print(i["strIngredient5"])
        print(i["strIngredient6"])
        print(i["strIngredient7"])
        print(i["strIngredient8"])
        print(i["strIngredient9"])
        print(i["strIngredient10"])
        print(i["strIngredient11"])
#need to figure out how to not print ingredients with null values

        url = i["strDrinkThumb"]
        webbrowser.open(url)


liquor_type()