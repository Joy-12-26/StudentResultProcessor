from student import Student
from results import calculate_total, calculate_average, calculate_grade
from display import display_result


def main():
    students = []
    num_students = int(input("Enter number of students: "))
    num_subjects = 5

    for i in range(1, num_students + 1):
        print(f"\nStudent {i}")
        name = input("Name: ")
        marks = []

        for j in range(1, num_subjects + 1):
            mark = int(input(f"  Subject {j} marks: "))
            marks.append(mark)

        s = Student(name, i, marks)
        s.total = calculate_total(s.marks)
        s.average = calculate_average(s.total, num_subjects)
        s.grade = calculate_grade(s.average)
        students.append(s)

    print("\nStudent Results")
    display_result(students)


if __name__ == "__main__":
    main()
