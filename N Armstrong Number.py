def is_armstrong(number):
    total = 0
    num_digits = len(str(number))
    temp = number


    while temp > 0:
        digit = temp % 10
        total += digit ** num_digits
        temp //= 10

    return total == number


def find_n_armstrong_after_x(x, n):
    count = 0
    current = x + 1

    print(f"First {n} Armstrong numbers after {x}:")
    while count < n:
        if is_armstrong(current):
            print(current, end=" ")
            count += 1
        current += 1



x = int(input("Enter the number after which to find Armstrong numbers: "))
n = int(input("Enter the count of Armstrong numbers to find: "))

print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")


find_n_armstrong_after_x(x, n)
