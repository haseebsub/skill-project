# Nutritionist Skill

A comprehensive personal nutritionist assistant that provides diet guidance, explains macronutrient differences (carbs vs protein), creates meal plans, and offers personalized nutrition advice. This skill transforms Claude into your expert nutrition guide for achieving optimal health and dietary goals.

## 🍎 What This Skill Does

This skill provides complete nutritional guidance including:

- **Macronutrient Education** - Comprehensive explanation of carbs vs protein differences
- **Personalized Nutrition Planning** - Daily calorie and macro calculations
- **Meal Planning & Guidance** - Balanced meal plans and portion control strategies
- **Food Analysis** - Nutritional analysis of meals and food comparisons
- **Daily Tracking** - Tools for monitoring dietary intake and progress

## 📋 Quick Start

### For Users
1. **Use the skill when you need:**
   - Understanding macronutrient differences
   - Personalized nutrition calculations
   - Daily meal planning guidance
   - Food quality analysis
   - Nutrition tracking tools

2. **Example requests:**
   - "Explain the difference between carbohydrates and protein"
   - "Calculate my daily calorie and macro needs"
   - "Create a balanced meal plan for weight loss"
   - "Analyze the nutrition of my typical meals"
   - "Help me track my daily nutrition intake"

### For Developers
The skill includes:

- **SKILL.md** - Main skill documentation and comprehensive nutrition guidance
- **Scripts/** - Interactive tools for calculations and food analysis
- **References/** - Detailed educational content on macronutrients and meal planning
- **Assets/** - Printable templates for meal planning and nutrition tracking

## 🛠️ Included Tools

### Scripts

#### `nutrition_calculator.py`
Comprehensive nutrition calculator that:
- Calculates BMR and TDEE using Mifflin-St Jeor equation
- Determines personalized macronutrient requirements
- Creates sample daily meal plans with timing
- Provides food suggestions for each meal
- Saves personalized nutrition plans to JSON files

**Key Features:**
- Goal-specific calculations (weight loss, muscle gain, maintenance)
- Activity level adjustments
- Meal distribution across 4-6 meals per day
- Practical food suggestions for each meal type

**Usage:**
```bash
python scripts/nutrition_calculator.py
```

#### `food_database.py`
Comprehensive food database and analysis tool:
- Nutritional information for 25+ common foods
- Meal analysis and macro breakdown
- Food comparison capabilities
- High-protein and low-carb food identification
- Balanced meal creation suggestions

**Key Features:**
- Interactive food information lookup
- Custom meal analysis with macro ratios
- Food quality comparisons
- Sample meal creation with nutrition facts

**Usage:**
```bash
python scripts/food_database.py
```

### References

#### `carbs_vs_protein_guide.md`
Complete guide explaining the fundamental differences between carbohydrates and proteins including:
- Chemical structure and digestion differences
- Energy production and storage mechanisms
- Biological functions and health impacts
- Food sources and quality considerations
- Metabolic pathways and practical applications
- Optimal timing and distribution strategies
- Common misconceptions and facts

#### `daily_meal_planning_guide.md`
Comprehensive meal planning guide covering:
- Daily calorie and macro calculation methods
- Plate method and portion control techniques
- Sample meal plans for different goals (2000, 1800, 2200 calories)
- Meal timing strategies for various objectives
- Grocery shopping and meal prep strategies
- Budget-friendly options and dining out tips
- Progress tracking and adjustment methods

### Assets

#### `weekly_meal_planner.txt`
Printable weekly meal planning template with:
- Daily calorie and macro tracking
- Meal planning for 7 days
- Grocery list organization
- Weekly summary and goal tracking
- Notes section for adjustments and observations

#### `nutrition_tracker_log.txt`
Daily nutrition tracking template featuring:
- Complete meal logging (6 meals/snacks)
- Macro and calorie tracking
- Hydration monitoring
- Supplement tracking
- Energy and satisfaction ratings
- Food quality assessment
- Daily reflections and improvement notes

#### `carbs_vs_protein_comparison_chart.txt`
Quick reference comparison chart showing:
- Side-by-side macronutrient differences
- Food source categories
- Daily requirement guidelines
- When to focus on each macronutrient
- Health benefits and potential issues
- Metabolic pathways overview
- Best food combinations
- Key takeaways summary

## 🎮 Using the Skill

### When to Use This Skill

Use this skill when users request:

- **Macronutrient Education**: "Explain the difference between carbs and protein"
- **Nutrition Calculations**: "Calculate my daily calorie needs"
- **Meal Planning**: "Create a meal plan for muscle building"
- **Food Analysis**: "Analyze the nutrition of this meal"
- **Dietary Guidance**: "Help me understand balanced eating"

### Example Workflow

1. **User Request**: "I want to lose weight and need help understanding nutrition. Explain carbs vs protein and create a meal plan."

2. **Skill Activation**: Claude uses the skill to:
   - Explain macronutrient differences using the comprehensive guide
   - Calculate personalized nutrition needs
   - Create a weight loss meal plan
   - Provide tracking tools for monitoring progress

3. **Ongoing Support**: Users can continue to:
   - Track daily nutrition with provided templates
   - Analyze food choices using the database
   - Adjust meal plans based on progress
   - Learn more about nutrition principles

## 📊 Skill Statistics

- **Total Lines of Code**: ~850 lines
- **Scripts**: 2 interactive calculation and analysis tools
- **References**: 2 comprehensive educational guides
- **Assets**: 3 printable templates for planning and tracking
- **Coverage**: Complete nutrition education and practical application

## 🔧 Technical Details

### Dependencies
- Python 3.6+
- Standard library only (no external dependencies for core functionality)
- JSON support for data storage and export

### File Structure
```
nutritionist/
├── SKILL.md                        # Main skill documentation
├── README.md                       # This file
├── scripts/
│   ├── nutrition_calculator.py     # Personalized nutrition calculations
│   └── food_database.py            # Food analysis and comparison tool
├── references/
│   ├── carbs_vs_protein_guide.md   # Complete macronutrient education
│   └── daily_meal_planning_guide.md # Meal planning strategies
└── assets/
    ├── weekly_meal_planner.txt         # 7-day meal planning template
    ├── nutrition_tracker_log.txt       # Daily nutrition tracking
    └── carbs_vs_protein_comparison_chart.txt # Quick reference guide
```

### Integration Points
- **Direct API**: Users can run Python scripts for calculations
- **Template System**: Printable templates for offline use
- **Educational Content**: Comprehensive guides for learning
- **Tracking System**: Daily and weekly nutrition monitoring

## 🎯 Skill Benefits

### For Nutrition Beginners
- Clear explanations of complex nutritional concepts
- Step-by-step meal planning guidance
- Practical tracking tools for daily use
- Educational content to build knowledge

### For Fitness Enthusiasts
- Performance nutrition strategies
- Goal-specific meal planning
- Macro timing for optimal results
- Food quality analysis tools

### For Health-Conscious Individuals
- Balanced eating principles
- Portion control strategies
- Budget-friendly healthy eating
- Long-term sustainable habits

## 🚀 Future Enhancements

Potential improvements to consider:
- Integration with nutrition tracking apps
- Barcode scanning for food analysis
- Personalized recipe suggestions
- Integration with fitness trackers
- AI-powered meal recommendations

## 📞 Support

For questions about using this skill:
1. Check the SKILL.md for detailed instructions
2. Review the reference guides for specific topics
3. Use the provided scripts for calculations and analysis
4. Follow the templates for consistent tracking

## 📝 License

This skill is provided under the terms specified in LICENSE.txt

---

**Transform your relationship with food through expert nutritional guidance, personalized planning, and comprehensive education about the science of nutrition.**