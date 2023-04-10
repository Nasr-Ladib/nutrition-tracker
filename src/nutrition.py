import requests

# Define a function to look up the nutritional information for an ingredient using the USDA FoodData Central API
def lookup_nutrition(ingredient):
    api_key = "YOUR_API_KEY" # Replace with your own API key
    url = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={api_key}&query={ingredient}"
    
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
    total_calories = 0
    total_protein = 0
    total_carbs = 0
    total_fiber = 0
    
    for item, amount in items.items():
        # Look up the nutritional information for the item
        item_nutrients = lookup_nutrition(item)
        
        if item_nutrients:
            # Calculate the nutritional intake for the given amount of the item
            calories = item_nutrients["calories"] * amount / 100
            protein = item_nutrients["protein"] * amount / 100
            carbs = item_nutrients["carbs"] * amount / 100
            fiber = item_nutrients["fiber"] * amount / 100
            
            # Add the nutritional intake to the total
            total_calories += calories
            total_protein += protein
            total_carbs += carbs
            total_fiber += fiber
            
            # Print the nutritional values for the item
            print(f"{item} ({amount}g): {calories:.1f}kcal | {protein:.2f}g protein | {carbs:.2f}g carbs | {fiber:.1f}g fiber")
        else:
            # Print an error message if the nutritional information is not found for the item
            print(f"Error: Nutritional information not found for {item}")
    
    # Print the total nutritional values
    print(f"Total: {total_calories:.1f}kcal | {total_protein:.2f}g protein | {total_carbs:.2f}g carbs | {total_fiber:.1f}g fiber")

# Example usage:
items = {
    "apple": 198,
    "banana": 100,
}

calculate_nutrition(items)
