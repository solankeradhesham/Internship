# Week 2: Student Grade Calculator

## Project Overview

The **Student Grade Calculator** is a beginner-friendly Python project that accepts a student's name and marks, calculates the corresponding grade, and displays an encouraging message.

This project practices decision-making, loops, functions, comparison operators, and basic error handling.

## Features

- Accepts a student's name and marks.
- Validates that marks are a number between 0 and 100.
- Uses `if` / `elif` / `else` to assign a grade.
- Uses a function to calculate the grade and message.
- Uses a `while` loop to keep asking until valid marks are entered.
- Displays an encouraging message for each grade.

## Grading Rules

| Marks | Grade | Message |
|---:|:---:|---|
| 90–100 | A | Excellent work! Keep shining! 🌟 |
| 80–89 | B | Very good! Keep it up! 👍 |
| 70–79 | C | Good effort! Keep improving! 💪 |
| 60–69 | D | You passed! Keep practicing! 📚 |
| 0–59 | F | Don't give up. Learn from mistakes and try again! 🌱 |

## Project Structure

```text
student-grade-calculator/
├── README.md
├── grade_calculator.py
├── test_cases.txt
└── screenshots/
    └── (add your program screenshots here)
```

## Requirements

- Python 3
- A terminal or code editor such as Visual Studio Code

No third-party Python packages are required.

## How to Run

1. Download and extract the project.
2. Open the `student-grade-calculator` folder in your terminal.
3. Run one of these commands:

   **Windows**
   ```powershell
   python grade_calculator.py
   ```
   If needed:
   ```powershell
   py grade_calculator.py
   ```

   **macOS/Linux**
   ```bash
   python3 grade_calculator.py
   ```

4. Enter the student's name and marks when prompted.

## Example Output

```text
Enter student name: Priya
Enter marks (0-100): 85

📊 RESULT FOR PRIYA
Marks: 85/100
Grade: B
Message: Very good! Keep it up! 👍
```

## Concepts Practiced

- **`if` / `elif` / `else`:** Selects the grade based on marks.
- **Comparison operators:** Checks the marks range.
- **`while` loop:** Repeats the input prompt until marks are valid.
- **Functions:** Keeps grade calculation reusable.
- **Error handling:** Handles non-numeric marks with `try` / `except`.

## Testing

Use the cases in `test_cases.txt` to check grade boundaries and invalid inputs. Try marks such as `100`, `90`, `89`, `80`, `79`, `70`, `69`, `60`, `59`, and `0`. Also test a negative number, a number above 100, and text such as `hello`.

## Screenshot Instructions

1. Run the program in your terminal.
2. Enter sample details, such as `Priya` and `85`.
3. Take a screenshot showing the result.
4. Save it in the `screenshots/` folder, for example as `grade-result.png`.

Screenshots are not generated automatically; capture them from your own program run.

## GitHub Submission

After creating or connecting this folder to a Git repository, run:

```bash
git add .
git commit -m "Complete Week 2 Student Grade Calculator"
git push
```

## Learning Outcome

By completing this project, you will practice Python conditions, comparison operators, loops, functions, and input validation in a practical program.

## Author

Add your name here.
