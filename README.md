# Nutrition Calculator

This is a Python project that calculates the nutritional intake of a list of food items. It uses the USDA FoodData Central API to look up the nutritional information for each item.

## Requirements
To run this project, you will need:

Python 3.x
Flask
requests
You can install Flask and requests using pip:

```
pip install Flask requests
```

## Usage

You can use the nutrition.py module to calculate the nutritional intake of a list of food items. The module contains two functions:

lookup_nutrition(ingredient): looks up the nutritional information for an ingredient using the USDA FoodData Central API. It returns a dictionary containing the nutritional values for the ingredient, or None if the information is not found.
calculate_nutrition(items): calculates the nutritional intake for a list of food items. It takes a dictionary where the keys are the item names and the values are the amounts in grams.
Example usage:

python

```
import nutrition

# Look up the nutritional information for an ingredient

apple_nutrients = nutrition.lookup_nutrition('apple')
print(apple_nutrients)

# Calculate the nutritional intake for a list of food items

items = {'apple': 100, 'banana': 120}
nutrition.calculate_nutrition(items)
```

You can also use the app.py module to run a Flask web application that provides an API for calculating the nutritional intake. The API accepts POST requests with a JSON body containing a list of food items with their amounts. It returns a JSON response containing the nutritional values for each item.

To run the web application, run the following command in the terminal:

1. Obtain an API key for the USDA FoodData Central API.

2. Set the `FOODDATA_API_KEY` environment variable to your API key:

```
export FOODDATA_API_KEY=YOUR_API_KEY
```
3. 
```
export FLASK_APP=app.py
flask run
```

You can then send a POST request to <http://localhost:5000/nutrition> with the following JSON body:

json

```
{
  "items": [
    {"ingredient": "apple", "balance": 100},
    {"ingredient": "banana", "balance": 120}
  ]
}
```

The API will return a JSON response like this:

json

```
[
  {
    "ingredient": "apple",
    "balance": 100,
    "calories": 52,
    "protein": 0.26,
    "carbs": 13.81,
    "fiber": 2.4
  },
  {
    "ingredient": "banana",
    "balance": 120,
    "calories": 106.8,
    "protein": 1.31,
    "carbs": 27.41,
    "fiber": 3.12
  }
]
```

## Running the unit tests

To run the unit tests, you can use the following command:

python -m unittest discover -v

python
Copy code

This will discover and run all the unit tests in the `test` directory and its subdirectories.

### Unit Test Results

The following are the results of the unit tests for the `nutrition` module:

#### Test e: Test if the function adds an error message when the nutritional information is not found

```python
def test_calculate_nutrition(self):
    items = [
        {"ingredient": "chicken", "balance": 100},
        {"ingredient": "dededezddfvergregttrhhrtyhrthrt", "balance": 200}
    ]
    result = src.nutrition.calculate_nutrition(items)
    for item in result:
        if item["ingredient"] == "nonexistent ingredient":
            self.assertIn("error", item)
            break
    else:
        self.fail("Error message not found")
```

You can run the unit tests using the above command, and the results will be displayed in the terminal.

To generate a JSON report of the test results, you can use the following command:

```
python -m unittest discover -v -j <num_workers> --json-report
```

Replace <num_workers> with the number of worker processes to use for running the tests in parallel. This command will generate a JSON report file in the test-reports directory, which you can use to analyze the test results.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
