def divide_numbers():
    while True:
        try:
            # Taking input from the user
            num1 = int(input("Enter the molecular weight of protien without unit: "))
            num2 = int ("110")

            # Performing division
            result = num1 / num2
            print(f"The esstimated numbers of amino acid {result} in protein " )

            # Option to continue or exit
            continue_choice = input("Do you want to calculate numbers of amino acid in protien? (yes/no): ").lower()
            if continue_choice != 'yes':
                break

        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except ZeroDivisionError:
            print("Error: Cannot divide by zero. Please enter a non-zero divisor.")

if __name__ == "__main__":
    divide_numbers()
