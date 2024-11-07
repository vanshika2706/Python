# WRITE A PYTHON CODE WITHOUT AND WITH THE THIRD VARIABLE
# METHOD 1
a = int (input("Enter the 1st number :-"))
b = int (input("Enter the 2nd number:- "))

a = a+b
b = a-b
a = a-b
print(f"The Swapping Number  of a is {a} " 
      f"The Swapping Number  of b is {b}")

# METHOD 2
c = int (input("Enter the 1 number :-"))
d = int (input("Enter the 2 number:- "))
c,d = d,c
print(f"The Swapping Number  of c is {c} " 
      f"The Swapping Number  of d is {d}")

# METHOD 2 WITH 3RD VARIABLE
A = int (input("Enter the value of A  :-"))
B = int (input("Enter the value of B :- "))

temp = A
A = B
B = temp
print(f"The Swapping Number  of A is {A} " 
      f"The Swapping Number  of B is {B}")
print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")
