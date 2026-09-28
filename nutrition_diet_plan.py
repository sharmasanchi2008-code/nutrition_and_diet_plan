# Nutrition and Diet Plan
# Beginner-level Python project

def calculate_bmi(weight, height):
    height_m = height / 100
    bmi = weight / (height_m * height_m)
    return bmi


def calculate_calories(age, gender, weight, height, activity):
    if gender == "male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    if activity == 1:
        calories = bmr * 1.2
    elif activity == 2:
        calories = bmr * 1.375
    elif activity == 3:
        calories = bmr * 1.55
    else:
        calories = bmr * 1.725

    return calories


def show_bmi_result(bmi):
    print("\nYour BMI is:", round(bmi, 2))

    if bmi < 18.5:
        print("BMI Category: Underweight")
    elif bmi < 25:
        print("BMI Category: Normal")
    elif bmi < 30:
        print("BMI Category: Overweight")
    else:
        print("BMI Category: Obese")


def get_diet_plan(goal):
    plans = {
        "1": {
            "goal": "Weight Loss",
            "breakfast": "2 boiled eggs + 1 fruit + 1 glass of milk",
            "lunch": "2 chapatis + dal + mixed vegetables + salad",
            "snack": "1 fruit + handful of roasted chana",
            "dinner": "2 chapatis + vegetable curry + salad"
        },
        "2": {
            "goal": "Maintain Weight",
            "breakfast": "Poha/upma + 1 fruit + milk",
            "lunch": "2-3 chapatis + dal + vegetables + curd + salad",
            "snack": "Fruit + handful of nuts",
            "dinner": "2 chapatis + dal/paneer + vegetables"
        },
        "3": {
            "goal": "Weight Gain",
            "breakfast": "Paneer sandwich + banana + glass of milk",
            "lunch": "3 chapatis + rice + dal + vegetables + curd",
            "snack": "Banana shake + handful of nuts",
            "dinner": "3 chapatis + paneer/soybean curry + vegetables"
        }
    }
    return plans[goal]


def show_diet_plan(plan):
    print("\n========== DIET PLAN ==========")
    print("Goal:", plan["goal"])
    print("Breakfast:", plan["breakfast"])
    print("Lunch:", plan["lunch"])
    print("Snack:", plan["snack"])
    print("Dinner:", plan["dinner"])
    print("================================")


def nutrition_tips():
    print("\n========== BASIC NUTRITION TIPS ==========")
    print("1. Drink enough water during the day.")
    print("2. Include fruits and vegetables in your meals.")
    print("3. Try to include a source of protein in your meals.")
    print("4. Avoid eating too much junk food.")
    print("5. Get enough sleep and stay physically active.")
    print("===========================================")


def main():
    print("======================================")
    print("       NUTRITION AND DIET PLAN")
    print("======================================")

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (male/female): ").lower()
    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in cm: "))

    print("\nSelect your activity level:")
    print("1. Little or no exercise")
    print("2. Light exercise")
    print("3. Moderate exercise")
    print("4. Heavy exercise")

    activity = int(input("Enter your choice (1-4): "))

    bmi = calculate_bmi(weight, height)
    calories = calculate_calories(age, gender, weight, height, activity)

    print("\nHello", name + "!")
    show_bmi_result(bmi)
    print("Estimated daily calorie requirement:", round(calories), "calories")

    print("\nSelect your goal:")
    print("1. Weight Loss")
    print("2. Maintain Weight")
    print("3. Weight Gain")

    goal = input("Enter your choice (1-3): ")

    if goal in ["1", "2", "3"]:
        plan = get_diet_plan(goal)
        show_diet_plan(plan)
    else:
        print("Invalid goal choice.")

    nutrition_tips()
    print("\nNote: This is a basic educational project and not a medical diet plan.")


main()
