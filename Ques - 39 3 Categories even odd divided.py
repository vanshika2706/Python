start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

for num in range(start , end + 1) :
    if num % 5 == 0:
        print(f"{num} is divisible by 5")

    elif num % 2 == 0 :
        print(f"{num} is even")

    else :
        print(f"{num} is odd")

print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")
