# src/nutrition.py

import requests
import os

api_key = os.environ.get("FOODDATA_API_KEY")  # get the API key from an environment variable

def get_url(ingredient):
    return f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={api_key}&query={ingredient}"

# Define a function to look up the nutritional information for an ingredient using the USDA FoodData Central API
def lookup_nutrition(ingredient):
    url = get_url(ingredient)
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if data["foods"]:
            food = data["foods"][0]
            nutrients = food["foodNutrients"]
            calories = next((n["value"] for n in nutrients if n["nutrientName"] == "Energy"), None)
            protein = next((n["value"] for n in nutrients if n["nutrientName"] == "Protein"), None)
            carbs = next((n["value"] for n in nutrients if n["nutrientName"] == "Carbohydrate, by difference"), None)
            fiber = next((n["value"] for n in nutrients if n["nutrientName"] == "Fiber, total dietary"), None)
            
            return {
                "calories": calories,
                "protein": protein,
                "carbs": carbs,
                "fiber": fiber
            }
        
    return None

# Define a function to calculate the nutritional intake
def calculate_nutrition(items):
    result = []
    for item in items:
        name = item["ingredient"]
        amount = item["balance"]
        # Look up the nutritional information for the item
        item_nutrients = lookup_nutrition(name)
        
        if item_nutrients:
            # Calculate the nutritional intake for the given amount of the item
            calories = item_nutrients["calories"] * amount / 100
            protein = item_nutrients["protein"] * amount / 100
            carbs = item_nutrients["carbs"] * amount / 100
            fiber = item_nutrients["fiber"] * amount / 100
            
            # Add the nutritional intake to the result list
            result.append({
                "ingredient": name,
                "balance": amount,
                "calories": calories,
                "protein": protein,
                "carbs": carbs,
                "fiber": fiber
            })
        else:
            # Add an error message to the result list if the nutritional information is not found for the item
            result.append({
                "ingredient": name,
                "balance": amount,
                "error": "Nutritional information not found"
            })
    
    return result

