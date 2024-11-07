num = int (input("Enter a  number to reverse:-"))
print(f"The Orignal Number is {num}")
reversed_number = 0

while num > 0 :
    digit = num % 10
    reversed_number = reversed_number * 10 + digit
    num = num // 10
    print(f"The Reversed Number is {reversed_number}")

print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")