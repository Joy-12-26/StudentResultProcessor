def display_result(students):
    print("\n" + "-" * 60)
    print(f"{'Roll':<6} {'Name':<20} {'Total':<8} {'Average':<10} {'Grade'}")
    print("-" * 60)
    for s in students:
        print(f"{s.roll_no:<6} {s.name:<20} {s.total:<8} {s.average:<10.2f} {s.grade}")
    print("-" * 60)
