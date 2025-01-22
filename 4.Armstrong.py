def is_armstrong(number):
    # Convert the number to a string to easily get each digit
    digits = str(number)
    num_digits = len(digits)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the sum of powers is equal to the original number
    return sum_of_powers == number

# Input from the user
number = int(input("Enter a number to check if it's an Armstrong number: "))

# Check and display result
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
