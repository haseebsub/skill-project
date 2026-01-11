#!/usr/bin/env python3
"""
Nutrition Calculator - Daily Calorie and Macronutrient Calculator
Calculates personalized nutrition needs based on user input and goals.
"""

import json
import datetime

class NutritionCalculator:
    def __init__(self):
        self.user_data = {}

    def calculate_bmr(self, weight_kg, height_cm, age, gender):
        """Calculate Basal Metabolic Rate using Mifflin-St Jeor equation"""
        if gender.lower() == 'male':
            bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
        else:
            bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
        return bmr

    def calculate_tdee(self, bmr, activity_level):
        """Calculate Total Daily Energy Expenditure"""
        activity_multipliers = {
            'sedentary': 1.2,      # Little or no exercise
            'light': 1.375,        # Light exercise 1-3 days/week
            'moderate': 1.55,      # Moderate exercise 3-5 days/week
            'active': 1.725,       # Heavy exercise 6-7 days/week
            'very_active': 1.9     # Very heavy exercise & physical job
        }
        return bmr * activity_multipliers.get(activity_level, 1.55)

    def calculate_macros(self, weight_kg, goal, activity_level):
        """Calculate macronutrient requirements"""
        # Protein requirements based on goal and activity
        if goal == 'muscle_gain':
            protein_g = min(2.2 * weight_kg, 180)  # Cap at 180g for most people
        elif goal == 'weight_loss':
            protein_g = min(2.0 * weight_kg, 150)
        else:  # maintenance
            protein_g = min(1.6 * weight_kg, 120)

        # Fat requirements (25-35% of total calories)
        fat_calories = 0.30 * self.tdee  # 30% from fat
        fat_g = fat_calories / 9

        # Carbohydrate requirements (remaining calories)
        protein_calories = protein_g * 4
        remaining_calories = self.tdee - protein_calories - fat_calories
        carbs_g = remaining_calories / 4

        return {
            'protein_g': round(protein_g, 1),
            'fat_g': round(fat_g, 1),
            'carbs_g': round(carbs_g, 1),
            'protein_calories': round(protein_g * 4),
            'fat_calories': round(fat_g * 9),
            'carbs_calories': round(carbs_g * 4)
        }

    def create_meal_plan(self, calories, macros):
        """Create a sample daily meal plan"""
        # Distribute calories across 4-6 meals
        meals = {
            'Breakfast': {'percentage': 0.20, 'time': '7:00 AM'},
            'Mid-Morning Snack': {'percentage': 0.10, 'time': '10:00 AM'},
            'Lunch': {'percentage': 0.30, 'time': '1:00 PM'},
            'Afternoon Snack': {'percentage': 0.15, 'time': '4:00 PM'},
            'Dinner': {'percentage': 0.25, 'time': '7:00 PM'}
        }

        meal_plan = {}
        for meal_name, info in meals.items():
            meal_calories = round(calories * info['percentage'])
            meal_protein = round(macros['protein_g'] * info['percentage'])
            meal_carbs = round(macros['carbs_g'] * info['percentage'])
            meal_fat = round(macros['fat_g'] * info['percentage'])

            meal_plan[meal_name] = {
                'time': info['time'],
                'calories': meal_calories,
                'protein_g': meal_protein,
                'carbs_g': meal_carbs,
                'fat_g': meal_fat,
                'suggestions': self.get_meal_suggestions(meal_name, meal_calories, meal_protein, meal_carbs, meal_fat)
            }

        return meal_plan

    def get_meal_suggestions(self, meal_type, calories, protein, carbs, fat):
        """Generate food suggestions for each meal"""
        suggestions = []

        if meal_type == 'Breakfast':
            suggestions.append(f"• Greek yogurt (150g) + berries + 1/4 cup granola")
            suggestions.append(f"• 2 eggs + 1 slice whole grain toast + avocado")
            suggestions.append(f"• Oatmeal (1/2 cup dry) + protein powder + banana")

        elif meal_type == 'Mid-Morning Snack':
            suggestions.append(f"• Apple + 2 tbsp peanut butter")
            suggestions.append(f"• Handful of almonds + cheese stick")
            suggestions.append(f"• Protein shake with water")

        elif meal_type == 'Lunch':
            suggestions.append(f"• Grilled chicken (150g) + quinoa (1 cup) + mixed vegetables")
            suggestions.append(f"• Turkey wrap with whole wheat tortilla + salad")
            suggestions.append(f"• Lentil soup + side salad + whole grain bread")

        elif meal_type == 'Afternoon Snack':
            suggestions.append(f"• Cottage cheese + pineapple")
            suggestions.append(f"• Hummus + veggie sticks + whole grain crackers")
            suggestions.append(f"• Protein bar + fruit")

        elif meal_type == 'Dinner':
            suggestions.append(f"• Salmon (150g) + sweet potato + broccoli")
            suggestions.append(f"• Lean beef stir-fry + brown rice + vegetables")
            suggestions.append(f"• Tofu + quinoa + roasted vegetables")

        return suggestions

    def run_calculator(self):
        """Main calculator interface"""
        print("NUTRITION CALCULATOR")
        print("=" * 40)

        # Get user information
        name = input("Enter your name: ")
        weight = float(input("Enter your weight (kg): "))
        height = float(input("Enter your height (cm): "))
        age = int(input("Enter your age: "))
        gender = input("Enter your gender (male/female): ")
        activity = input("Activity level (sedentary/light/moderate/active/very_active): ")
        goal = input("Goal (weight_loss/muscle_gain/maintenance): ")

        # Calculate needs
        bmr = self.calculate_bmr(weight, height, age, gender)
        self.tdee = self.calculate_tdee(bmr, activity)
        macros = self.calculate_macros(weight, goal, activity)

        # Create meal plan
        meal_plan = self.create_meal_plan(self.tdee, macros)

        # Display results
        print("\n" + "=" * 50)
        print(f"NUTRITION PLAN FOR {name.upper()}")
        print("=" * 50)

        print(f"\nDaily Caloric Needs: {self.tdee:.0f} calories")
        print(f"Basal Metabolic Rate: {bmr:.0f} calories")

        print(f"\nMacronutrient Breakdown:")
        print(f"Protein: {macros['protein_g']}g ({macros['protein_calories']} calories)")
        print(f"Carbohydrates: {macros['carbs_g']}g ({macros['carbs_calories']} calories)")
        print(f"Fat: {macros['fat_g']}g ({macros['fat_calories']} calories)")

        print(f"\nPercentage Distribution:")
        print(f"Protein: {(macros['protein_calories']/self.tdee)*100:.1f}%")
        print(f"Carbs: {(macros['carbs_calories']/self.tdee)*100:.1f}%")
        print(f"Fat: {(macros['fat_calories']/self.tdee)*100:.1f}%")

        print(f"\nDaily Meal Plan:")
        for meal, info in meal_plan.items():
            print(f"\n{meal} ({info['time']}): {info['calories']} calories")
            print(f"  Protein: {info['protein_g']}g | Carbs: {info['carbs_g']}g | Fat: {info['fat_g']}g")
            print(f"  Suggestions:")
            for suggestion in info['suggestions'][:2]:  # Show 2 suggestions per meal
                print(f"    {suggestion}")

        print(f"\nKey Tips:")
        print(f"• Drink 2-3 liters of water daily")
        print(f"• Focus on whole, minimally processed foods")
        print(f"• Adjust portions based on progress")
        print(f"• Track your intake for the first week")

        return {
            'user_data': {
                'name': name, 'weight': weight, 'height': height,
                'age': age, 'gender': gender, 'activity': activity, 'goal': goal
            },
            'calories': self.tdee,
            'macros': macros,
            'meal_plan': meal_plan
        }

if __name__ == "__main__":
    calc = NutritionCalculator()
    result = calc.run_calculator()

    # Save results to file
    filename = f"nutrition_plan_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w') as f:
        json.dump(result, f, indent=2)

    print(f"\nPlan saved to {filename}")
    print("Keep this plan for reference and adjust as needed!")