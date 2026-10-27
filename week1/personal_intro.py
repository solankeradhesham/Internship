"""
Week 1 Python Project: Personal Introduction Program
Asks a few questions and prints a personalized welcome message.
"""

def main():
    print("=" * 42)
    print("       WELCOME TO MY INTRODUCTION")
    print("=" * 42)

    name = input("What is your name? ").strip()
    age_text = input("How old are you? ").strip()
    hobby = input("What is your favorite hobby? ").strip()
    city = input("Which city do you live in? ").strip()
    favorite_food = input("What is your favorite food? ").strip()

    try:
        age = int(age_text)
        if age < 0:
            print("Age cannot be negative. Please run the program again.")
            return
    except ValueError:
        print("Please enter your age as a whole number. Run the program again.")
        return

    name = name or "Friend"
    hobby = hobby or "exploring new things"
    city = city or "your city"
    favorite_food = favorite_food or "something delicious"

    print("\n" + "=" * 42)
    print(f"🎉 Welcome, {name}! 🎉")
    print(f"You are {age} years old and enjoy {hobby}.")
    print(f"You live in {city}, and your favorite food is {favorite_food}.")
    print("Thanks for introducing yourself. Have a great day!")
    print("=" * 42)


if __name__ == "__main__":
    main()
