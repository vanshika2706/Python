def countdown(n):
    while n > 0:
        yield n
        n -= 1
for number in countdown(5):
    print(number)
print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")