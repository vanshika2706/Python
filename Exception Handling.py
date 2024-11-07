try:
    number = int(input("Enter a number : "))
    result = 10 / number
except ZeroDivisionError :
    print("ERROR : Cannot divided by zero .")
except ValueError:
    print("Error : Invalid input . Please enter a valid number ")


print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")