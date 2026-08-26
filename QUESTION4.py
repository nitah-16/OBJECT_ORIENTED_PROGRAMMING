# ==========================================
# QUESTION 4
# CLINIC PATIENT STATUS CLASSIFICATION
# ==========================================


def classify_patient_bp(systolic, diastolic):
    """Classifies BP according to the worst-case reading achieved."""
    if systolic >= 160 or diastolic >= 100:
        return "Stage 2 / Urgent"
    elif (140 <= systolic <= 159) or (90 <= diastolic <= 99):
        return "Stage 1"
    elif (120 <= systolic <= 139) or (80 <= diastolic <= 89):
        return "Elevated"
    else:
        return "Normal"


def process_clinic_data(patient_records):
    categories = {
        "Normal": [],
        "Elevated": [],
        "Stage 1": [],
        "Stage 2 / Urgent": [],
    }

    total_sys = 0
    total_dia = 0
    alerts = []
    follow_ups = []

    for name, sys, dia in patient_records:
        total_sys += sys
        total_dia += dia

        status = classify_patient_bp(sys, dia)
        categories[status].append((name, sys, dia))

        if status == "Stage 2 / Urgent":
            alerts.append(f"URGENT ALERT: {name} (BP: {sys}/{dia})")
            follow_ups.append(name)
        elif status in ["Stage 1", "Elevated"]:
            follow_ups.append(name)

    count = len(patient_records)
    avg_sys = total_sys / count if count > 0 else 0
    avg_dia = total_dia / count if count > 0 else 0

    return {
        "categories": categories,
        "avg_sys": avg_sys,
        "avg_dia": avg_dia,
        "alerts": alerts,
        "follow_ups": follow_ups,
    }


def generate_clinic_report(results, title="DATASET"):
    print(f"\n==========================================")
    print(f" CLINIC PATIENT REPORT: {title}")
    print(f"==========================================")

    print(
        f"Average Readings: {results['avg_sys']:.1f} Systolic / {results['avg_dia']:.1f} Diastolic"
    )

    print("\n--- Category Breakdown ---")
    for cat, patients in results["categories"].items():
        names = [p[0] for p in patients]
        print(f"  • {cat} ({len(patients)}): {', '.join(names) if names else 'None'}")

    print("\n--- Active Alerts ---")
    if results["alerts"]:
        for alert in results["alerts"]:
            print(f"  🚨 {alert}")
    else:
        print("  No urgent alerts.")

    print("\n--- Patients Requiring Follow-Up ---")
    print(
        f"  {', '.join(results['follow_ups']) if results['follow_ups'] else 'None'}"
    )

    print("==========================================\n")


# ---------------------------------------------------------
# TESTING THE PROGRAM
# ---------------------------------------------------------

supplied_patients = [
    ("Alice", 115, 75),
    ("Brian", 128, 84),
    ("Carol", 145, 95),
    ("Daniel", 165, 105),
    ("Grace", 118, 78),
]

# Additional dataset covering exact boundaries (Edge Cases)
additional_patients = [
    ("Borderline Normal", 119, 79),  # Exact upper limits of normal
    ("Isolated Systolic Urgent", 165, 75),  # High sys, normal dia
    ("Isolated Diastolic Urgent", 115, 102),  # Normal sys, high dia
]

if __name__ == "__main__":
    res1 = process_clinic_data(supplied_patients)
    generate_clinic_report(res1, "SUPPLIED DATASET")

    res2 = process_clinic_data(additional_patients)
    generate_clinic_report(res2, "ADDITIONAL TEST DATASET")