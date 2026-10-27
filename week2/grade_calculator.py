"""Week 2 project: Student Grade Calculator."""


def get_grade_and_message(marks):
    """Return the grade and an encouraging message for valid marks."""
    if 90 <= marks <= 100:
        return "A", "Excellent work! Keep shining! 🌟"
    elif 80 <= marks < 90:
        return "B", "Very good! Keep it up! 👍"
    elif 70 <= marks < 80:
        return "C", "Good effort! Keep improving! 💪"
    elif 60 <= marks < 70:
        return "D", "You passed! Keep practicing! 📚"
    else:
        return "F", "Don't give up. Learn from mistakes and try again! 🌱"


def get_valid_marks():
    """Keep asking until the user enters a number from 0 to 100."""
    while True:
        raw_marks = input("Enter marks (0-100): ").strip()

        try:
            marks = float(raw_marks)
        except ValueError:
            print("Invalid input. Please enter a number, such as 85 or 72.5.")
            continue

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100. Please try again.")
            continue

        return marks


def main():
    """Run the student grade calculator."""
    student_name = input("Enter student name: ").strip()

    while not student_name:
        print("Student name cannot be empty.")
        student_name = input("Enter student name: ").strip()

    marks = get_valid_marks()
    grade, message = get_grade_and_message(marks)

    # Display whole-number marks without a trailing .0.
    marks_display = int(marks) if marks.is_integer() else marks

    print(f"\n📊 RESULT FOR {student_name.upper()}")
    print(f"Marks: {marks_display}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


if __name__ == "__main__":
    main()
