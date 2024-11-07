rows = 5
print(" 1st part ")
for i in range(1, rows + 1):
    print('*' * i)

print(" 2nd part ")

for i in range(1, rows + 1):
    print(''.join(str(num) for num in range(1, i + 1)))

print(" 3rd part ")

for i in range(1, rows + 1):
    print(''.join(str(i) for _ in range(i)))

print(" 4th part ")

for i in range(rows, 0, -1):
    print('*' * i)

print(" 5th part ")

for i in range(rows, 0, -1):
    print(''.join(str(num) for num in range(i, 0, - 1)))

print(" 6th part ")
for i in range(rows, 0, -1):
    print(''.join(str(i) for _ in range(i)))

print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")