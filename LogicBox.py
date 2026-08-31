# ==========================================
# Project: Logic Box
# Pattern Generator and Number Analyzer
# ==========================================


# ---------- Pattern Generator ----------

def generate_pattern():
    rows = int(input("Enter the number of rows for the pattern: "))

    # Input validation
    if rows <= 0:
        print("Please enter a positive number of rows.")
        return

    print("\nPattern:")

    # Nested loop
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()


# ---------- Number Analyzer ----------

def analyze_numbers():
    start = int(input("Enter the start of the range: "))
    end = int(input("Enter the end of the range: "))

    # Input validation
    if start > end:
        print("Invalid range! Start number must be less than or equal to end number.")
        return

    total = 0

    print()

    # Analyze every number
    for number in range(start, end + 1):

        # Check Even or Odd
        if number % 2 == 0:
            print("Number", number, "is Even")
        else:
            print("Number", number, "is Odd")

        # Calculate sum
        total = total + number

    print()
    print("Sum of all numbers from", start, "to", end, "is:", total)


# ---------- Main Program ----------

print("==========================================")
print("   Welcome to the Pattern Generator and")
print("          Number Analyzer!")
print("==========================================")

while True:

    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    # Option 1
    if choice == "1":

        try:
            generate_pattern()

        except ValueError:
            print("Invalid input! Please enter a valid number.")

    # Option 2
    elif choice == "2":

        try:
            analyze_numbers()

        except ValueError:
            print("Invalid input! Please enter valid numbers.")

    # Option 3
    elif choice == "3":

        print("\nThank you for using Logic Box!")
        print("Exiting the program. Goodbye!")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please select 1, 2, or 3.")