#!/usr/bin/env python3
"""
Gym Trainer - Workout Routine Generator
Generates personalized workout routines based on user input.
"""

import random

def calculate_calories(weight_kg, height_cm, age, gender, activity_level):
    """Calculate daily caloric needs using Mifflin-St Jeor equation"""
    if gender.lower() == 'male':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

    activity_multipliers = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very_active': 1.9
    }

    return bmr * activity_multipliers.get(activity_level, 1.55)

def generate_workout_routine(fitness_level, goal, equipment_available, days_per_week):
    """Generate a personalized workout routine"""
    routines = {
        'beginner': {
            'full_body': [
                'Warm-up: 5-10 minutes light cardio',
                'Bodyweight Squats: 3 sets of 10-15 reps',
                'Push-ups (knee or wall if needed): 3 sets of 5-10 reps',
                'Dumbbell Rows: 3 sets of 10-12 reps',
                'Plank: 3 sets, hold 20-30 seconds',
                'Cool-down: 5-10 minutes stretching'
            ],
            'upper_lower': [
                'Upper Day: Push-ups, Rows, Plank, Light Weights',
                'Lower Day: Squats, Lunges, Glute Bridges, Core Work'
            ]
        },
        'intermediate': {
            'push_pull_legs': [
                'Push Day: Bench Press, Overhead Press, Tricep Dips, Chest Flyes',
                'Pull Day: Deadlifts, Pull-ups, Rows, Bicep Curls',
                'Leg Day: Squats, Lunges, Leg Press, Calf Raises'
            ],
            'upper_lower': [
                'Upper Day: Bench Press, Rows, Overhead Press, Pull-ups, Accessories',
                'Lower Day: Squats, Deadlifts, Lunges, Leg Curls, Core'
            ]
        },
        'advanced': {
            'bro_split': [
                'Chest Day: Bench Press, Incline Press, Flyes, Dips',
                'Back Day: Deadlifts, Pull-ups, Rows, Face Pulls',
                'Leg Day: Squats, Leg Press, Hamstring Curls, Calves',
                'Shoulder Day: Overhead Press, Lateral Raises, Rear Delt Flyes',
                'Arm Day: Bicep Curls, Tricep Extensions, Preacher Curls, Skullcrushers'
            ],
            'upper_lower_push_pull': [
                'Upper Day 1: Heavy compounds and volume',
                'Lower Day 1: Squats, Deadlifts, Accessories',
                'Push Day: Chest, Shoulders, Triceps focus',
                'Pull Day: Back, Biceps, Rear Delts focus',
                'Upper Day 2: Hypertrophy work',
                'Lower Day 2: Volume and isolation work'
            ]
        }
    }

    # Select appropriate routine based on fitness level
    if fitness_level == 'beginner':
        routine_type = 'full_body' if days_per_week <= 3 else 'upper_lower'
    elif fitness_level == 'intermediate':
        routine_type = 'push_pull_legs' if days_per_week >= 4 else 'upper_lower'
    else:
        routine_type = 'bro_split' if days_per_week >= 5 else 'upper_lower_push_pull'

    return routines[fitness_level][routine_type]

def generate_nutrition_plan(calories, goal):
    """Generate macronutrient recommendations"""
    protein_calories = 2.2 * 4  # 2.2g protein per kg, 4 cal/g
    protein_grams = min(150, max(100, protein_calories / 4))

    if goal == 'bulking':
        total_calories = calories + 500
        carb_ratio = 0.5
        fat_ratio = 0.25
    elif goal == 'cutting':
        total_calories = calories - 500
        carb_ratio = 0.4
        fat_ratio = 0.3
    else:  # maintenance
        total_calories = calories
        carb_ratio = 0.45
        fat_ratio = 0.25

    protein_calories = protein_grams * 4
    remaining_calories = total_calories - protein_calories
    carbs_grams = int((remaining_calories * carb_ratio) / 4)
    fat_grams = int((remaining_calories * fat_ratio) / 9)

    return {
        'total_calories': total_calories,
        'protein_grams': protein_grams,
        'carbs_grams': carbs_grams,
        'fat_grams': fat_grams
    }

if __name__ == "__main__":
    print("Gym Trainer - Workout and Nutrition Generator")
    print("=" * 50)

    # Get user information
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (cm): "))
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ")
    activity = input("Enter activity level (sedentary/light/moderate/active/very_active): ")
    fitness_level = input("Enter fitness level (beginner/intermediate/advanced): ")
    goal = input("Enter goal (bulking/cutting/maintenance): ")
    equipment = input("Available equipment (bodyweight/dumbbells/full_gym): ")
    days = int(input("Days per week you can train: "))

    # Calculate needs
    calories = calculate_calories(weight, height, age, gender, activity)
    nutrition = generate_nutrition_plan(calories, goal)
    workout = generate_workout_routine(fitness_level, goal, equipment, days)

    # Display results
    print("\n" + "=" * 50)
    print("YOUR PERSONALIZED FITNESS PLAN")
    print("=" * 50)

    print(f"\nDaily Caloric Needs: {nutrition['total_calories']:.0f} calories")
    print(f"Macronutrients:")
    print(f"  Protein: {nutrition['protein_grams']}g ({nutrition['protein_grams']*4} calories)")
    print(f"  Carbs: {nutrition['carbs_grams']}g ({nutrition['carbs_grams']*4} calories)")
    print(f"  Fat: {nutrition['fat_grams']}g ({nutrition['fat_grams']*9} calories)")

    print(f"\nWorkout Routine ({fitness_level.upper()} - {days} days/week):")
    if isinstance(workout, list):
        for i, day in enumerate(workout, 1):
            print(f"  Day {i}: {day}")
    else:
        print(f"  {workout}")

    print("\nRemember:")
    print("- Adjust weights to reach muscle fatigue in the recommended rep range")
    print("- Stay hydrated and get adequate sleep")
    print("- Track your progress and adjust as needed")
    print("- Listen to your body and rest when needed")