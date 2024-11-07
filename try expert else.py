try:
    number = int(input("Enter a number : "))
    result = 10 / number
except ZeroDivisionError :
    print("ERROR : Cannot divided by zero .")
except ValueError:
    print("Error : Invalid input . Please enter a valid number ")
else:
    print(f"The result is : {result}")

print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")