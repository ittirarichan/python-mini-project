# main.py

import calendar_module
import input_validation

def get_input(prompt, validator):
    """
    Function to get and validate user input using a provided validator function.
    """
    while True:
        user_input = input(prompt)
        is_valid, value = validator(user_input)
        if is_valid:
            return value
        else:
            print("Invalid input. Please try again.")

def main():
    print("Welcome to the Python Calendar App!\n")

    while True:
        year = get_input("Enter year (e.g., 2024): ", input_validation.validate_year)
        month = get_input("Enter month (1-12): ", input_validation.validate_month)

        calendar_module.display_calendar(year, month)

        choice = input("\nDo you want to view another calendar? (yes/no): ")
        if choice.lower() != 'yes':
            break

    print("\nThank you for using the Python Calendar App!")

if __name__ == "__main__":
    main()
