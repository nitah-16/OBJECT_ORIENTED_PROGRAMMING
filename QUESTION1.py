# ==========================================
# QUESTION 1
# SCHOOL CAFETERIA MEAL PLANNING SYSTEM
# ==========================================

# Constants / Rules
SCHOOL_DAYS_PER_WEEK = 5
HIGH_SPENDER_THRESHOLD = 15000


def process_cafeteria_data(meal_records):
    """Processes cafeteria tuples and returns calculated metrics.

    Args:
        meal_records (list): List of tuples (student, meal, daily_price)

    Returns:
        dict: Processed results including student spend, meal revenues, and
        popular meals
    """
    meal_groups = {}
    student_weekly_spend = {}
    meal_weekly_revenue = {}
    meal_popularity = {}

    for student, meal, price in meal_records:
        # 1. Group students by meal preference
        if meal not in meal_groups:
            meal_groups[meal] = []
        meal_groups[meal].append(student)

        # 2. Calculate weekly spend per student
        weekly_spend = price * SCHOOL_DAYS_PER_WEEK
        student_weekly_spend[student] = weekly_spend

        # 3. Calculate weekly revenue per meal type
        if meal not in meal_weekly_revenue:
            meal_weekly_revenue[meal] = 0
            meal_popularity[meal] = 0

        meal_weekly_revenue[meal] += weekly_spend
        meal_popularity[meal] += 1

    # 4. Identify high spenders (> 15,000 UGX)
    high_spenders = {
        student: spend
        for student, spend in student_weekly_spend.items()
        if spend > HIGH_SPENDER_THRESHOLD
    }

    # 5. Determine the most popular meal
    most_popular_meal = max(meal_popularity, key=meal_popularity.get)

    return {
        "groups": meal_groups,
        "student_spend": student_weekly_spend,
        "high_spenders": high_spenders,
        "meal_revenue": meal_weekly_revenue,
        "popular_meal": most_popular_meal,
    }


def generate_cafeteria_report(results, dataset_title="DATASET"):
    """Prints a clean, formatted report for non-technical users."""
    print(f"\n==========================================")
    print(f" CAFETERIA REPORT: {dataset_title}")
    print(f"==========================================")

    print("\n--- Student Meal Groups ---")
    for meal, students in results["groups"].items():
        print(f"  • {meal}: {', '.join(students)}")

    print("\n--- Weekly Expenditure per Student (5 Days) ---")
    for student, spend in results["student_spend"].items():
        print(f"  • {student}: {spend:,} UGX")

    print("\n--- High Spenders (> 15,000 UGX/week) ---")
    if results["high_spenders"]:
        for student, spend in results["high_spenders"].items():
            print(f"  • {student}: {spend:,} UGX")
    else:
        print("  None")

    print("\n--- Weekly Revenue Generated per Meal Type ---")
    for meal, revenue in results["meal_revenue"].items():
        print(f"  • {meal}: {revenue:,} UGX")

    print(f"\nMost Popular Meal: {results['popular_meal']}")
    print("==========================================\n")


# ---------------------------------------------------------
# TESTING THE PROGRAM
# ---------------------------------------------------------

# Supplied Dataset
supplied_meal_data = [
    ("John", "Pizza", 2500),
    ("Sarah", "Burger", 2000),
    ("Mike", "Pasta", 2200),
    ("Grace", "Chicken and Rice", 3500),
    ("Peter", "Pizza", 2500),
]

# Additional Test Dataset (Normal + Edge Cases)
additional_meal_data = [
    ("David", "Rolex", 1000),  # Edge: Very low spend (5,000 weekly)
    ("Anita", "Chicken and Rice", 3500),  # Edge: High spend (17,500 weekly)
    ("Brian", "Rolex", 1000),  # Creates a tie for popular meal
]

if __name__ == "__main__":
    # Test 1: Supplied Data
    res1 = process_cafeteria_data(supplied_meal_data)
    generate_cafeteria_report(res1, "SUPPLIED DATASET")

    # Test 2: Additional Data
    #THE CAFETERIA REPORT
    res2 = process_cafeteria_data(additional_meal_data)
    generate_cafeteria_report(res2, "ADDITIONAL TEST DATASET")