# ==========================================
# QUESTION 5 (GRAND CHALLENGE)
# UNIVERSITY COURSE ENROLLMENT SYSTEM
# ==========================================


def calculate_average(marks):
    """Calculates average from a list of numerical marks."""
    return sum(marks) / len(marks) if marks else 0.0


def assign_grade(average):
    """Assigns letter grade based on course average."""
    if average >= 85:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"


def determine_status(course_grades):
    """Determines student academic standing based on letter grades list."""
    grades = course_grades.values()
    if "F" in grades:
        return "Critical"
    elif "C" in grades:
        return "At-Risk"
    else:
        return "Good Standing"


def process_student_records(students):
    """Processes individual performance for all students."""
    processed = []

    for student in students:
        name = student["name"]
        courses = student["courses"]

        course_averages = {}
        course_grades = {}
        improvement_needed = []
        all_marks = []

        for course_name, marks in courses.items():
            avg = calculate_average(marks)
            grade = assign_grade(avg)

            course_averages[course_name] = avg
            course_grades[course_name] = grade
            all_marks.extend(marks)

            if grade in ["C", "F"]:
                improvement_needed.append(course_name)

        status = determine_status(course_grades)
        overall_avg = calculate_average(all_marks)
        needs_tutoring = status in ["Critical", "At-Risk"]

        processed.append(
            {
                "name": name,
                "course_averages": course_averages,
                "course_grades": course_grades,
                "overall_avg": overall_avg,
                "status": status,
                "improvement_needed": improvement_needed,
                "needs_tutoring": needs_tutoring,
            }
        )

    return processed


def calculate_course_statistics(students):
    """Calculates overall department course statistics."""
    course_data = {}

    for student in students:
        for course_name, marks in student["courses"].items():
            if course_name not in course_data:
                course_data[course_name] = {"all_marks": [], "enrolled": 0, "passed": 0}

            avg = calculate_average(marks)
            course_data[course_name]["all_marks"].extend(marks)
            course_data[course_name]["enrolled"] += 1

            if assign_grade(avg) != "F":
                course_data[course_name]["passed"] += 1

    stats = {}
    for cname, data in course_data.items():
        overall_avg = calculate_average(data["all_marks"])
        stats[cname] = {
            "overall_avg": overall_avg,
            "enrolled": data["enrolled"],
            "passed": data["passed"],
        }

    lowest_course = min(stats, key=lambda c: stats[c]["overall_avg"])
    return stats, lowest_course


def create_intervention_priority(processed_students):
    """Ranks students by priority (Critical -> At-Risk -> Good Standing)."""
    priority_order = {"Critical": 1, "At-Risk": 2, "Good Standing": 3}

    # Sort primarily by priority rank, secondarily by overall average descending
    sorted_list = sorted(
        processed_students,
        key=lambda s: (priority_order[s["status"]], -s["overall_avg"]),
    )
    return sorted_list


def generate_university_report(students_data, title="DATASET"):
    processed = process_student_records(students_data)
    course_stats, lowest_course = calculate_course_statistics(students_data)
    priority_list = create_intervention_priority(processed)

    print(f"\n==========================================")
    print(f" UNIVERSITY ACADEMIC REPORT: {title}")
    print(f"==========================================")

    print("\n--- Part A: Individual Student Performance ---")
    for s in processed:
        print(
            f"\nStudent: {s['name']} | Status: {s['status']} | Overall Avg: {s['overall_avg']:.2f}"
        )
        for course, avg in s["course_averages"].items():
            print(f"  • {course}: Avg = {avg:.2f} (Grade: {s['course_grades'][course]})")
        if s["improvement_needed"]:
            print(f"    Needs Improvement In: {', '.join(s['improvement_needed'])}")
        print(f"    Tutoring Recommended: {'Yes' if s['needs_tutoring'] else 'No'}")

    print("\n--- Part B: Course Statistics ---")
    for cname, stat in course_stats.items():
        print(
            f"  • {cname}: Avg = {stat['overall_avg']:.2f} | Enrolled = {stat['enrolled']} | Passed = {stat['passed']}"
        )
    print(
        f"\n⚠️ Course Requiring Greatest Attention: {lowest_course} (Lowest Avg: {course_stats[lowest_course]['overall_avg']:.2f})"
    )

    print("\n--- Part C: Intervention Priority List ---")
    for rank, s in enumerate(priority_list, start=1):
        print(
            f"  {rank}. {s['name']} - [{s['status']}] (Avg: {s['overall_avg']:.2f})"
        )

    print("==========================================\n")


# ---------------------------------------------------------
# TESTING THE PROGRAM
# ---------------------------------------------------------

supplied_students = [
    {"name": "Amos", "courses": {"Math": [75, 80, 78], "English": [85, 88, 90]}},
    {"name": "Betty", "courses": {"Math": [60, 58, 62], "English": [92, 94, 89]}},
    {"name": "Charles", "courses": {"Math": [85, 88, 90], "Science": [80, 82, 85]}},
    {"name": "Diana", "courses": {"Math": [45, 48, 50], "English": [70, 72, 68]}},
]

additional_students = [
    # All A student
    {
        "name": "Edward",
        "courses": {"Math": [95, 98, 100], "English": [90, 92, 95]},
    },
    # Multiple F student
    {"name": "Fiona", "courses": {"Math": [30, 40, 20], "Science": [50, 40, 45]}},
]

if __name__ == "__main__":
    generate_university_report(supplied_students, "SUPPLIED DATASET")
    generate_university_report(additional_students, "ADDITIONAL TEST DATASET")