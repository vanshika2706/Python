# Function to check if a number is perfect
def is_perfect(n):
    divisors_sum = sum([i for i in range(1, n) if n % i == 0])
    return divisors_sum == n

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to check if a number is Armstrong
def is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    armstrong_sum = sum([int(digit)**num_len for digit in num_str])
    return armstrong_sum == n

# Get input from the user
user_input = int(input("Enter a number: "))

# Lists to store the numbers
perfect_numbers = []
prime_numbers = []
armstrong_numbers = []

# Check for each number smaller than user_input
for num in range(1, user_input):
    if is_perfect(num):
        perfect_numbers.append(num)
    if is_prime(num):
        prime_numbers.append(num)
    if is_armstrong(num):
        armstrong_numbers.append(num)

# Print the results
print(f"Perfect numbers smaller than {user_input}: {perfect_numbers}")
print(f"Prime numbers smaller than {user_input}: {prime_numbers}")
print(f"Armstrong numbers smaller than {user_input}: {armstrong_numbers}")

print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")
