

print ("********************************************************************")
print ("This program is designed to calculate the sum of molecular mass")
print ("and amino acid mass in dalton")
print ("********************************************************************")



# Function to add two values
def add_two_numbers():
    # Take input from the user
    num1 = input("Enter the molcular formula mass: ")
    num2 = input("Enter the amino acid (protien) molcular weight: ")

    try:
        # Convert inputs to float and add them
        result = float(num1) + float(num2)
        print(f"The sum of molcular formula mass {num1} and amino acid {num2} is: {result}")
    except ValueError:
        print("Please enter valid numbers.")

# Call the function
add_two_numbers()
input ("Enter to exit")
