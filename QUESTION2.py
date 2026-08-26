# ==========================================
# QUESTION 2
# COMMUNITY LIBRARY BOOK DONATION MANAGER
# ==========================================

GOLD_DONOR_THRESHOLD = 5


# Helper function to extract the second element (book count) from a tuple
def get_second_element(item):
    """
    Helper function used for sorting.
    Input: A tuple like ('Alice', 6)
    Output: 6 (the element at index 1)
    """
    return item[1]


def process_donations(donation_records):
    """
    Aggregates donation metrics, identifies Gold Donors,
    and ranks the Top 3 donors using get_second_element.
    """
    donor_totals = {}
    genre_totals = {}
    overall_books = 0

    # 1. Loop through all donation records
    for donor, genre, count in donation_records:
        overall_books += count

        # Accumulate total books per donor
        donor_totals[donor] = donor_totals.get(donor, 0) + count

        # Accumulate total books per genre
        genre_totals[genre] = genre_totals.get(genre, 0) + count

    # 2. Identify Gold Donors (contributed at least 5 books)
    gold_donors = {
        donor: count
        for donor, count in donor_totals.items()
        if count >= GOLD_DONOR_THRESHOLD
    }

    # 3. Sort donors by number of books in descending order
    # donor_totals.items() gives a list of tuples: [('Alice', 6), ('Brian', 12), ...]
    # key=get_second_element tells sorted() to extract item[1] (book count) for comparison
    sorted_donors = sorted(
        donor_totals.items(), key=get_second_element, reverse=True
    )

    # 4. Extract Top 3 Donors using list slicing [:3]
    top_3_donors = sorted_donors[:3]

    # 5. Determine the Most Popular Genre based on total books
    most_popular_genre = (
        max(genre_totals, key=genre_totals.get) if genre_totals else "None"
    )

    return {
        "donor_totals": donor_totals,
        "genre_totals": genre_totals,
        "gold_donors": gold_donors,
        "overall_books": overall_books,
        "popular_genre": most_popular_genre,
        "top_3_donors": top_3_donors,
    }


def generate_library_report(metrics, title="DATASET"):
    """Displays formatted donation metrics for non-technical users."""
    print(f"\n==========================================")
    print(f" LIBRARY DONATION REPORT: {title}")
    print(f"==========================================")

    print(f"Overall Books Donated: {metrics['overall_books']}")
    print(f"Most Popular Genre:    {metrics['popular_genre']}")

    print("\n--- Books Received per Genre ---")
    for genre, count in metrics["genre_totals"].items():
        print(f"  • {genre}: {count} books")

    print("\n--- Gold Donors (>= 5 Books Contributed) ---")
    if metrics["gold_donors"]:
        for donor, count in metrics["gold_donors"].items():
            print(f"  • {donor} ({count} books)")
    else:
        print("  None")

    print("\n--- Top 3 Donors ---")
    for rank, (donor, count) in enumerate(metrics["top_3_donors"], start=1):
        print(f"  {rank}. {donor} - {count} books")

    print("==========================================\n")


# ---------------------------------------------------------
# TESTING THE PROGRAM
# ---------------------------------------------------------

# Supplied Dataset
supplied_donations = [
    ("Alice", "Fiction", 3),
    ("Brian", "Technology", 6),
    ("Carol", "History", 2),
    ("Alice", "Technology", 3),
    ("Daniel", "Fiction", 7),
    ("Grace", "Science", 5),
]

# Additional Test Dataset (Normal + Edge Cases)
additional_donations = [
    ("Xavier", "Math", 1),    # Edge case: single small donation
    ("Yolanda", "Math", 2),
    ("Zack", "History", 1),   # Edge case: under threshold, tie values
]

if __name__ == "__main__":
    # Test 1: Supplied Data
    res1 = process_donations(supplied_donations)
    generate_library_report(res1, "SUPPLIED DATASET")

    # Test 2: Additional Test Data
    res2 = process_donations(additional_donations)
    generate_library_report(res2, "ADDITIONAL TEST DATASET")