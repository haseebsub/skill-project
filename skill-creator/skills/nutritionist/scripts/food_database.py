#!/usr/bin/env python3
"""
Food Database and Analysis Tool
Provides nutritional information for common foods and analyzes meal composition.
"""

import json
from typing import Dict, List, Tuple

class FoodDatabase:
    def __init__(self):
        self.food_data = self._load_food_database()

    def _load_food_database(self) -> Dict:
        """Load comprehensive food database"""
        return {
            # Proteins
            'chicken_breast': {'calories': 165, 'protein': 31, 'carbs': 0, 'fat': 3.6, 'serving': '100g'},
            'salmon': {'calories': 208, 'protein': 25, 'carbs': 0, 'fat': 12, 'serving': '100g'},
            'eggs': {'calories': 155, 'protein': 13, 'carbs': 1.1, 'fat': 11, 'serving': '2 large'},
            'greek_yogurt': {'calories': 59, 'protein': 10, 'carbs': 3.6, 'fat': 0.4, 'serving': '100g'},
            'tofu': {'calories': 76, 'protein': 8, 'carbs': 1.9, 'fat': 4.8, 'serving': '100g'},
            'lentils': {'calories': 116, 'protein': 9, 'carbs': 20, 'fat': 0.4, 'serving': '100g'},

            # Carbohydrates
            'brown_rice': {'calories': 111, 'protein': 2.6, 'carbs': 23, 'fat': 0.9, 'serving': '100g cooked'},
            'quinoa': {'calories': 120, 'protein': 4.4, 'carbs': 21, 'fat': 1.9, 'serving': '100g cooked'},
            'sweet_potato': {'calories': 86, 'protein': 1.6, 'carbs': 20, 'fat': 0.1, 'serving': '100g'},
            'oats': {'calories': 389, 'protein': 16.9, 'carbs': 66, 'fat': 6.9, 'serving': '100g dry'},
            'whole_wheat_bread': {'calories': 247, 'protein': 13, 'carbs': 41, 'fat': 3.2, 'serving': '100g'},
            'banana': {'calories': 89, 'protein': 1.1, 'carbs': 23, 'fat': 0.3, 'serving': '100g'},

            # Vegetables
            'broccoli': {'calories': 34, 'protein': 2.8, 'carbs': 7, 'fat': 0.4, 'serving': '100g'},
            'spinach': {'calories': 23, 'protein': 2.9, 'carbs': 3.6, 'fat': 0.4, 'serving': '100g'},
            'carrots': {'calories': 41, 'protein': 0.9, 'carbs': 10, 'fat': 0.2, 'serving': '100g'},
            'bell_pepper': {'calories': 20, 'protein': 0.9, 'carbs': 4.6, 'fat': 0.2, 'serving': '100g'},
            'avocado': {'calories': 160, 'protein': 2, 'carbs': 9, 'fat': 15, 'serving': '100g'},

            # Fats
            'olive_oil': {'calories': 884, 'protein': 0, 'carbs': 0, 'fat': 100, 'serving': '100g'},
            'almonds': {'calories': 579, 'protein': 21, 'carbs': 22, 'fat': 50, 'serving': '100g'},
            'peanut_butter': {'calories': 588, 'protein': 25, 'carbs': 20, 'fat': 50, 'serving': '100g'},
            'chia_seeds': {'calories': 486, 'protein': 17, 'carbs': 42, 'fat': 31, 'serving': '100g'},

            # Fruits
            'apple': {'calories': 52, 'protein': 0.3, 'carbs': 14, 'fat': 0.2, 'serving': '100g'},
            'berries': {'calories': 57, 'protein': 0.7, 'carbs': 12, 'fat': 0.7, 'serving': '100g'},
            'orange': {'calories': 47, 'protein': 0.9, 'carbs': 12, 'fat': 0.1, 'serving': '100g'},
            'kiwi': {'calories': 61, 'protein': 1.1, 'carbs': 15, 'fat': 0.5, 'serving': '100g'},
        }

    def get_food_info(self, food_name: str) -> Dict:
        """Get nutritional information for a specific food"""
        return self.food_data.get(food_name.lower(), None)

    def analyze_meal(self, meal_items: List[Tuple[str, float]]) -> Dict:
        """
        Analyze a meal's nutritional content
        meal_items: List of (food_name, serving_size_in_grams)
        """
        total_calories = 0
        total_protein = 0
        total_carbs = 0
        total_fat = 0

        for food_name, serving_size in meal_items:
            food_info = self.get_food_info(food_name)
            if food_info:
                # Calculate for actual serving size
                multiplier = serving_size / 100  # Most foods are per 100g
                total_calories += food_info['calories'] * multiplier
                total_protein += food_info['protein'] * multiplier
                total_carbs += food_info['carbs'] * multiplier
                total_fat += food_info['fat'] * multiplier

        return {
            'calories': round(total_calories, 1),
            'protein_g': round(total_protein, 1),
            'carbs_g': round(total_carbs, 1),
            'fat_g': round(total_fat, 1),
            'macros_ratio': self._calculate_macros_ratio(total_protein, total_carbs, total_fat)
        }

    def _calculate_macros_ratio(self, protein_g: float, carbs_g: float, fat_g: float) -> Dict:
        """Calculate macronutrient ratio percentages"""
        total_calories = protein_g * 4 + carbs_g * 4 + fat_g * 9

        if total_calories == 0:
            return {'protein': 0, 'carbs': 0, 'fat': 0}

        protein_pct = (protein_g * 4 / total_calories) * 100
        carbs_pct = (carbs_g * 4 / total_calories) * 100
        fat_pct = (fat_g * 9 / total_calories) * 100

        return {
            'protein': round(protein_pct, 1),
            'carbs': round(carbs_pct, 1),
            'fat': round(fat_pct, 1)
        }

    def find_high_protein_foods(self, min_protein: float = 20) -> List[str]:
        """Find foods with high protein content"""
        high_protein = []
        for food_name, nutrition in self.food_data.items():
            if nutrition['protein'] >= min_protein:
                high_protein.append(food_name)
        return high_protein

    def find_low_carb_foods(self, max_carbs: float = 10) -> List[str]:
        """Find foods with low carbohydrate content"""
        low_carb = []
        for food_name, nutrition in self.food_data.items():
            if nutrition['carbs'] <= max_carbs:
                low_carb.append(food_name)
        return low_carb

    def create_balanced_meal(self, target_calories: int) -> Dict:
        """Create a sample balanced meal"""
        # Sample meal: Protein + Carbs + Vegetables + Healthy Fats
        meal = {
            'chicken_breast': 150,  # 150g
            'brown_rice': 100,       # 100g cooked
            'broccoli': 150,         # 150g
            'olive_oil': 10,         # 10g (1 tsp)
        }

        meal_analysis = self.analyze_meal([(k, v) for k, v in meal.items()])

        return {
            'meal_components': meal,
            'nutrition': meal_analysis,
            'meal_description': "Grilled chicken breast with brown rice, steamed broccoli, and olive oil"
        }

    def compare_foods(self, food1: str, food2: str) -> Dict:
        """Compare nutritional content of two foods"""
        info1 = self.get_food_info(food1)
        info2 = self.get_food_info(food2)

        if not info1 or not info2:
            return {'error': 'One or both foods not found in database'}

        comparison = {
            'food1': info1,
            'food2': info2,
            'differences': {
                'calories_diff': info1['calories'] - info2['calories'],
                'protein_diff': info1['protein'] - info2['protein'],
                'carbs_diff': info1['carbs'] - info2['carbs'],
                'fat_diff': info1['fat'] - info2['fat']
            }
        }

        return comparison

def main():
    """Interactive food database tool"""
    db = FoodDatabase()

    print("FOOD DATABASE & ANALYSIS TOOL")
    print("=" * 40)

    while True:
        print("\n1. Get food information")
        print("2. Analyze meal")
        print("3. Find high protein foods")
        print("4. Find low carb foods")
        print("5. Create balanced meal")
        print("6. Compare foods")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == '1':
            food = input("Enter food name: ")
            info = db.get_food_info(food)
            if info:
                print(f"\n{food.title()} (per {info['serving']}):")
                print(f"  Calories: {info['calories']}")
                print(f"  Protein: {info['protein']}g")
                print(f"  Carbs: {info['carbs']}g")
                print(f"  Fat: {info['fat']}g")
            else:
                print(f"Food '{food}' not found in database")

        elif choice == '2':
            print("\nAdd meal components (food name, serving size in grams):")
            meal_items = []
            while True:
                food = input("Food name (or 'done' to finish): ")
                if food.lower() == 'done':
                    break
                try:
                    serving = float(input("Serving size (grams): "))
                    meal_items.append((food, serving))
                except ValueError:
                    print("Please enter a valid number for serving size")

            if meal_items:
                analysis = db.analyze_meal(meal_items)
                print(f"\nMeal Analysis:")
                print(f"  Total Calories: {analysis['calories']}")
                print(f"  Protein: {analysis['protein_g']}g ({analysis['macros_ratio']['protein']}%)")
                print(f"  Carbs: {analysis['carbs_g']}g ({analysis['macros_ratio']['carbs']}%)")
                print(f"  Fat: {analysis['fat_g']}g ({analysis['macros_ratio']['fat']}%)")

        elif choice == '3':
            min_protein = float(input("Minimum protein (default 20g): ") or 20)
            foods = db.find_high_protein_foods(min_protein)
            print(f"\nFoods with >= {min_protein}g protein per 100g:")
            for food in foods:
                protein = db.food_data[food]['protein']
                print(f"  {food.title()}: {protein}g protein")

        elif choice == '4':
            max_carbs = float(input("Maximum carbs (default 10g): ") or 10)
            foods = db.find_low_carb_foods(max_carbs)
            print(f"\nFoods with <= {max_carbs}g carbs per 100g:")
            for food in foods:
                carbs = db.food_data[food]['carbs']
                print(f"  {food.title()}: {carbs}g carbs")

        elif choice == '5':
            target_calories = int(input("Target meal calories (default 500): ") or 500)
            meal = db.create_balanced_meal(target_calories)
            print(f"\nBalanced Meal Plan:")
            print(f"  {meal['meal_description']}")
            print(f"  Components:")
            for food, amount in meal['meal_components'].items():
                print(f"    {food.replace('_', ' ').title()}: {amount}g")
            print(f"  Nutrition: {meal['nutrition']['calories']} calories")
            print(f"  Macros: {meal['nutrition']['protein_g']}g P, {meal['nutrition']['carbs_g']}g C, {meal['nutrition']['fat_g']}g F")

        elif choice == '6':
            food1 = input("First food: ")
            food2 = input("Second food: ")
            comparison = db.compare_foods(food1, food2)
            if 'error' in comparison:
                print(f"Error: {comparison['error']}")
            else:
                print(f"\nComparison: {food1.title()} vs {food2.title()}")
                print(f"  {food1.title()} has {comparison['differences']['calories_diff']:+} calories")
                print(f"  {food1.title()} has {comparison['differences']['protein_diff']:+}g protein")
                print(f"  {food1.title()} has {comparison['differences']['carbs_diff']:+}g carbs")
                print(f"  {food1.title()} has {comparison['differences']['fat_diff']:+}g fat")

        elif choice == '7':
            print("Thanks for using the Food Database!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()