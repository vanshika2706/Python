rows = 5
print(" 7th part ")
for i in range(1, rows + 1):
    print(' ' * ( rows - i) * 2  , end = '')
    print(' '.join('*' for _ in range(i)))
print("\n")
print(" 8th part \n")
n = 5
for i in range (1, n + 1):
    print(' ' * (n-i) + '*' * (2 * i - 1) )
print("\n")
print(" 9th part \n")
for i in range(n):
    print(' ' * ( n - i ) , end = ' ')
    print(' *' * ( i + 1))

for i in range( n - 2 , -1, -1):
    print(' ' * ( n - i ) , end = ' ')
    print(' *' * ( i + 1))

print("\n")
print(" 10th part \n")
for i in range(rows, 0, -1):
    print(' ' * (rows - i) , end='')
    print(' * ' * i )

print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")