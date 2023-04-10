import unittest
import src.nutrition

class TestNutrition(unittest.TestCase):

    def test_get_url(self):
        # Test if the function returns the correct URL
        ingredient = "chicken"
        expected = f"https://api.nal.usda.gov/fdc/v1/foods/search?api_key={src.nutrition.api_key}&query={ingredient}"
        result = src.nutrition.get_url(ingredient)
        self.assertEqual(expected, result)

    def test_lookup_nutrition(self):
        # Test if the function returns a dictionary with nutritional information
        ingredient = "chicken"
        result = src.nutrition.lookup_nutrition(ingredient)
        self.assertIsInstance(result, dict)
        self.assertIn("calories", result)
        self.assertIn("protein", result)
        self.assertIn("carbs", result)
        self.assertIn("fiber", result)

        # Test if the function returns None when the ingredient is not found
        ingredient = "dededezddfvergregttrhhrtyhrthrt"
        result = src.nutrition.lookup_nutrition(ingredient)
        self.assertIsNone(result)

    def test_calculate_nutrition(self):
        # Test if the function returns a list of dictionaries with nutritional information
        items = [
            {"ingredient": "chicken", "balance": 100},
            {"ingredient": "rice", "balance": 200}
        ]
        result = src.nutrition.calculate_nutrition(items)
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), len(items))
        for item in result:
            self.assertIsInstance(item, dict)
            self.assertIn("ingredient", item)
            self.assertIn("balance", item)
            self.assertIn("calories", item)
            self.assertIn("protein", item)
            self.assertIn("carbs", item)
            self.assertIn("fiber", item)

        # Test if the function adds an error message when the nutritional information is not found
        items = [
            {"ingredient": "chicken", "balance": 100},
            {"ingredient": "dededezddfvergregttrhhrtyhrthrt", "balance": 200}
        ]
        result = src.nutrition.calculate_nutrition(items)
        for item in result:
            if item["ingredient"] == "dededezddfvergregttrhhrtyhrthrt":
                self.assertIn("error", item)
                break
        else:
            self.fail("Error message not found")

if __name__ == "__main__":
    unittest.main()