def is_armstrong(number):
    total = 0
    num_digits = len(str(number))
    temp = number


    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10

    return total == number

def find_armstrong_in_range(start, end):
    count = 0
    print(f"Armstrong numbers between {start} and {end}:")
    for number in range(start, end + 1):
        if is_armstrong(number):
            print(number, end=" ")
            count += 1
    print(f"\nTotal Armstrong numbers found: {count}")



start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))


find_armstrong_in_range(start, end)

print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")
