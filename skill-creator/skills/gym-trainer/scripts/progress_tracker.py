#!/usr/bin/env python3
"""
Gym Trainer - Progress Tracking System
Tracks workouts, measurements, and progress over time.
"""

import json
import datetime
from pathlib import Path

class ProgressTracker:
    def __init__(self, user_id="default"):
        self.user_id = user_id
        self.data_file = Path(f"gym_progress_{user_id}.json")
        self.load_data()

    def load_data(self):
        """Load existing progress data or create new structure"""
        if self.data_file.exists():
            with open(self.data_file, 'r') as f:
                self.data = json.load(f)
        else:
            self.data = {
                "user_profile": {},
                "workouts": [],
                "measurements": [],
                "goals": []
            }

    def save_data(self):
        """Save progress data to file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)

    def add_profile(self, name, age, weight, height, fitness_level):
        """Add or update user profile"""
        self.data["user_profile"] = {
            "name": name,
            "age": age,
            "weight": weight,
            "height": height,
            "fitness_level": fitness_level,
            "start_date": datetime.datetime.now().isoformat()
        }
        self.save_data()
        print("Profile updated successfully!")

    def add_workout(self, workout_type, exercises, notes=""):
        """Add a completed workout"""
        workout = {
            "date": datetime.datetime.now().isoformat(),
            "type": workout_type,
            "exercises": exercises,
            "notes": notes
        }
        self.data["workouts"].append(workout)
        self.save_data()
        print("Workout logged successfully!")

    def add_measurement(self, weight, body_fat=None, chest=None, waist=None, arms=None, legs=None):
        """Add body measurements"""
        measurement = {
            "date": datetime.datetime.now().isoformat(),
            "weight": weight,
            "body_fat": body_fat,
            "chest": chest,
            "waist": waist,
            "arms": arms,
            "legs": legs
        }
        self.data["measurements"].append(measurement)
        self.save_data()
        print("Measurement recorded successfully!")

    def add_goal(self, goal_type, target_value, target_date, description=""):
        """Add a fitness goal"""
        goal = {
            "type": goal_type,
            "target_value": target_value,
            "target_date": target_date,
            "description": description,
            "start_date": datetime.datetime.now().isoformat(),
            "completed": False
        }
        self.data["goals"].append(goal)
        self.save_data()
        print("Goal added successfully!")

    def get_progress_summary(self):
        """Get a summary of progress"""
        profile = self.data["user_profile"]
        measurements = self.data["measurements"]
        workouts = self.data["workouts"]
        goals = self.data["goals"]

        print("\n" + "="*50)
        print("PROGRESS SUMMARY")
        print("="*50)

        if profile:
            print(f"\nUser: {profile['name']}")
            print(f"Fitness Level: {profile['fitness_level']}")
            print(f"Height: {profile['height']}cm")

        if measurements:
            latest = measurements[-1]
            print(f"\nLatest Measurements:")
            print(f"Weight: {latest['weight']}kg")
            if latest.get('body_fat'):
                print(f"Body Fat: {latest['body_fat']}%")
            if latest.get('chest'):
                print(f"Chest: {latest['chest']}cm")
            if latest.get('waist'):
                print(f"Waist: {latest['waist']}cm")

            if len(measurements) > 1:
                first = measurements[0]
                weight_change = latest['weight'] - first['weight']
                print(f"\nWeight Change: {'+' if weight_change > 0 else ''}{weight_change:.1f}kg")

        print(f"\nWorkout Statistics:")
        print(f"Total Workouts: {len(workouts)}")
        if workouts:
            # Count workout types
            types = {}
            for w in workouts:
                types[w['type']] = types.get(w['type'], 0) + 1

            for workout_type, count in types.items():
                print(f"  {workout_type}: {count}")

        if goals:
            print(f"\nGoals:")
            for i, goal in enumerate(goals, 1):
                status = "✓ Completed" if goal['completed'] else "✗ Active"
                print(f"  {i}. {goal['type']}: {goal['target_value']} ({status})")

    def print_workout_log(self, limit=10):
        """Print recent workout log"""
        workouts = self.data["workouts"][-limit:]
        print(f"\nRECENT WORKOUTS (Last {len(workouts)}):")
        print("-" * 40)

        for i, workout in enumerate(reversed(workouts), 1):
            date = datetime.datetime.fromisoformat(workout['date']).strftime("%Y-%m-%d")
            print(f"\n{i}. {date} - {workout['type']}")
            if workout.get('notes'):
                print(f"   Notes: {workout['notes']}")
            for exercise in workout['exercises']:
                print(f"   • {exercise}")

if __name__ == "__main__":
    tracker = ProgressTracker()

    print("Gym Progress Tracker")
    print("=" * 30)

    while True:
        print("\n1. Add Profile")
        print("2. Add Workout")
        print("3. Add Measurement")
        print("4. Add Goal")
        print("5. View Progress Summary")
        print("6. View Workout Log")
        print("7. Exit")

        choice = input("\nEnter your choice (1-7): ")

        if choice == '1':
            name = input("Name: ")
            age = int(input("Age: "))
            weight = float(input("Weight (kg): "))
            height = float(input("Height (cm): "))
            level = input("Fitness Level (beginner/intermediate/advanced): ")
            tracker.add_profile(name, age, weight, height, level)

        elif choice == '2':
            workout_type = input("Workout Type: ")
            exercises = input("Exercises (comma-separated): ").split(',')
            exercises = [e.strip() for e in exercises]
            notes = input("Notes (optional): ")
            tracker.add_workout(workout_type, exercises, notes)

        elif choice == '3':
            weight = float(input("Weight (kg): "))
            body_fat = input("Body Fat % (optional): ")
            chest = input("Chest (cm, optional): ")
            waist = input("Waist (cm, optional): ")
            arms = input("Arms (cm, optional): ")
            legs = input("Legs (cm, optional): ")

            tracker.add_measurement(
                weight,
                float(body_fat) if body_fat else None,
                float(chest) if chest else None,
                float(waist) if waist else None,
                float(arms) if arms else None,
                float(legs) if legs else None
            )

        elif choice == '4':
            goal_type = input("Goal Type: ")
            target = input("Target Value: ")
            date = input("Target Date (YYYY-MM-DD): ")
            desc = input("Description: ")
            tracker.add_goal(goal_type, target, date, desc)

        elif choice == '5':
            tracker.get_progress_summary()

        elif choice == '6':
            limit = int(input("How many workouts to show? "))
            tracker.print_workout_log(limit)

        elif choice == '7':
            print("Thanks for using Gym Progress Tracker!")
            break

        else:
            print("Invalid choice. Please try again.")