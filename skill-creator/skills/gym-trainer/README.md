# Gym Trainer Skill

A comprehensive fitness and nutrition guidance assistant that helps users achieve their health and fitness goals through personalized workout routines, exercise instruction, diet planning, and progress tracking.

## 🎯 What This Skill Does

This skill transforms Claude into your personal gym trainer, providing:

- **Personalized Workout Plans** - Custom routines based on fitness level and goals
- **Exercise Instruction** - Detailed form guidance and technique tips
- **Nutrition Planning** - Calorie and macronutrient calculations with meal planning
- **Progress Tracking** - Workout logs, measurements, and goal monitoring
- **Fitness Education** - Comprehensive guides on training principles and nutrition

## 📋 Quick Start

### For Users
1. **Use the skill when you need:**
   - Workout routine recommendations
   - Exercise form guidance
   - Diet and nutrition planning
   - Fitness progress tracking
   - General fitness advice

2. **Example requests:**
   - "Help me create a beginner workout routine"
   - "How do I perform a proper squat?"
   - "Calculate my daily calorie needs for muscle building"
   - "Track my workout progress over time"

### For Developers
The skill includes:

- **SKILL.md** - Main skill documentation and guidance
- **Scripts/** - Executable tools for calculations and tracking
- **References/** - Comprehensive guides and educational content
- **Assets/** - Templates and resources for users

## 🛠️ Included Tools

### Scripts

#### `workout_generator.py`
Generates personalized workout routines based on:
- Fitness level (beginner/intermediate/advanced)
- Goals (bulking/cutting/maintenance)
- Equipment availability
- Training frequency

**Usage:**
```bash
python scripts/workout_generator.py
```

#### `progress_tracker.py`
Comprehensive progress tracking system for:
- Workout logging
- Body measurements
- Goal setting and tracking
- Progress analysis

**Usage:**
```bash
python scripts/progress_tracker.py
```

### References

#### `exercise_guide.md`
Complete exercise library including:
- Proper form techniques
- Muscle targeting information
- Exercise variations
- Common mistakes to avoid
- Progressive overload principles

#### `nutrition_guide.md`
Comprehensive nutrition guidance covering:
- Macronutrient requirements
- Meal timing strategies
- Healthy recipe ideas
- Hydration guidelines
- Supplement recommendations

### Assets

#### `workout_log_template.txt`
Printable template for tracking workouts including:
- Exercise tracking
- Set/reps/weight logging
- Notes and observations
- Workout rating system

#### `daily_meal_plan_template.txt`
Daily nutrition tracking template with:
- Calorie and macro tracking
- Meal timing
- Water intake monitoring
- Supplement tracking

## 🎮 Using the Skill

### When to Use This Skill

Use this skill when users request:

- **Workout Planning**: "Create a 4-day split routine for muscle building"
- **Exercise Guidance**: "How do I perform deadlifts with proper form?"
- **Nutrition Advice**: "Calculate my macros for fat loss"
- **Progress Tracking**: "Help me track my fitness progress"
- **Fitness Education**: "Explain progressive overload"

### Example Workflow

1. **User Request**: "I'm a beginner wanting to build muscle. Help me create a workout plan."

2. **Skill Activation**: Claude uses the skill to:
   - Generate appropriate beginner workout routine
   - Provide form guidance for key exercises
   - Calculate nutrition needs
   - Suggest tracking methods

3. **Ongoing Support**: Users can continue to:
   - Track progress with provided tools
   - Get exercise form corrections
   - Adjust nutrition plans
   - Set and monitor fitness goals

## 📊 Skill Statistics

- **Total Lines of Code**: ~900 lines
- **Scripts**: 2 interactive tools
- **References**: 2 comprehensive guides
- **Assets**: 2 printable templates
- **Coverage**: Complete fitness and nutrition guidance

## 🔧 Technical Details

### Dependencies
- Python 3.6+
- Standard library only (no external dependencies)

### File Structure
```
gym-trainer/
├── SKILL.md                    # Main skill documentation
├── README.md                   # This file
├── scripts/
│   ├── workout_generator.py    # Workout routine generator
│   └── progress_tracker.py     # Progress tracking system
├── references/
│   ├── exercise_guide.md       # Complete exercise library
│   └── nutrition_guide.md      # Nutrition and diet guidance
└── assets/
    ├── workout_log_template.txt    # Printable workout log
    └── daily_meal_plan_template.txt # Meal planning template
```

### Integration Points
- **Direct API**: Users can run Python scripts directly
- **Template System**: Printable templates for offline use
- **Progress Tracking**: JSON-based data storage for persistence

## 🎯 Skill Benefits

### For Fitness Beginners
- Step-by-step guidance through workout creation
- Form instruction to prevent injuries
- Simple nutrition planning
- Progress tracking to stay motivated

### For Intermediate Users
- Advanced workout programming
- Detailed exercise technique
- Performance nutrition
- Comprehensive progress analysis

### For Fitness Enthusiasts
- Educational content on training principles
- Reference materials for form checking
- Tools for tracking complex metrics
- Templates for detailed planning

## 🚀 Future Enhancements

Potential improvements to consider:
- Integration with fitness apps and wearables
- AI-powered form analysis from photos/videos
- Personalized supplement recommendations
- Social features for accountability
- Integration with meal delivery services

## 📞 Support

For questions about using this skill:
1. Check the SKILL.md for detailed instructions
2. Review the reference guides for specific topics
3. Use the provided scripts for calculations and tracking
4. Follow the templates for consistent tracking

## 📝 License

This skill is provided under the terms specified in LICENSE.txt

---

**Transform your fitness journey with personalized guidance, expert advice, and comprehensive tracking tools.**