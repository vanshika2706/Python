def fibonacci(n):
    a,b = 0 , 1
    while a< n:
        yield a
        a,b= b,a+b
for num in fibonacci(10):
    print(num)
print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")