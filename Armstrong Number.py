number = int (input("Enter the number :-"))
def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    total = sum(int(digit) ** num_digits for digit in num_str)

    return total == number


# Test the function

if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")

print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")