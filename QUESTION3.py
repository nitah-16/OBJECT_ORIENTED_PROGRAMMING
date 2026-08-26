# ==========================================
# QUESTION 3
# SMALL BUSINESS SALES PERFORMANCE MONITOR
# ==========================================

TOP_BONUS = 50000
REGULAR_BONUS = 20000
SLOW_DAY_THRESHOLD = 2000000


def analyze_sales(sales_records):
    salesperson_totals = {}
    brand_totals = {}
    day_totals = {}

    for day, person, brand, amount in sales_records:
        salesperson_totals[person] = (
            salesperson_totals.get(person, 0) + amount
        )
        brand_totals[brand] = brand_totals.get(brand, 0) + amount
        day_totals[day] = day_totals.get(day, 0) + amount

    if not salesperson_totals:
        return {}

    # Find Top Performer(s) and resolve ties
    max_sales = max(salesperson_totals.values())
    top_performers = [
        person
        for person, total in salesperson_totals.items()
        if total == max_sales
    ]

    # Award Bonuses
    bonuses = {}
    for person in salesperson_totals:
        if person in top_performers:
            bonuses[person] = TOP_BONUS
        else:
            bonuses[person] = REGULAR_BONUS

    # Best brand
    top_brand = max(brand_totals, key=brand_totals.get)

    # Slow days
    slow_days = {
        day: total
        for day, total in day_totals.items()
        if total < SLOW_DAY_THRESHOLD
    }

    return {
        "person_sales": salesperson_totals,
        "top_performers": top_performers,
        "bonuses": bonuses,
        "brand_sales": brand_totals,
        "top_brand": top_brand,
        "day_sales": day_totals,
        "slow_days": slow_days,
    }


def generate_sales_report(results, title="DATASET"):
    print(f"\n==========================================")
    print(f" SALES PERFORMANCE REPORT: {title}")
    print(f"==========================================")

    print("--- Salesperson Performance & Bonuses ---")
    for person, total in results["person_sales"].items():
        bonus = results["bonuses"][person]
        status = " (TOP PERFORMER)" if person in results["top_performers"] else ""
        print(f"  • {person}: {total:,} UGX | Bonus: {bonus:,} UGX{status}")

    print(f"\n--- Brand Performance (Top: {results['top_brand']}) ---")
    for brand, total in results["brand_sales"].items():
        print(f"  • {brand}: {total:,} UGX")

    print("\n--- Daily Totals & Slow Days ---")
    for day, total in results["day_sales"].items():
        is_slow = " [SLOW DAY]" if day in results["slow_days"] else ""
        print(f"  • {day}: {total:,} UGX{is_slow}")

    print("==========================================\n")


# ---------------------------------------------------------
# TESTING THE PROGRAM
# ---------------------------------------------------------

supplied_sales = [
    ("Monday", "Alice", "Samsung", 1200000),
    ("Monday", "Brian", "Tecno", 850000),
    ("Tuesday", "Alice", "iPhone", 2500000),
    ("Tuesday", "Charles", "Samsung", 1100000),
    ("Wednesday", "Brian", "Infinix", 900000),
    ("Wednesday", "Alice", "Samsung", 1600000),
    ("Thursday", "Charles", "Tecno", 700000),
    ("Friday", "Brian", "Samsung", 2300000),
]

# Additional dataset with an explicit TIE for first place
additional_sales = [
    ("Monday", "Dennis", "Nokia", 1500000),
    ("Monday", "Emma", "Pixel", 1500000),  # Tie with Dennis
    ("Tuesday", "Dennis", "Nokia", 500000),  # Total 2.0M
    ("Tuesday", "Emma", "Pixel", 500000),  # Total 2.0M
]

if __name__ == "__main__":
    res1 = analyze_sales(supplied_sales)
    generate_sales_report(res1, "SUPPLIED DATASET")

    res2 = analyze_sales(additional_sales)
    generate_sales_report(res2, "ADDITIONAL TEST DATASET (TIE EDGE CASE)")