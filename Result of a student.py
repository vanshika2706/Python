name = input("Enter the name of student :- ")
Roll_no = input("Enter the roll no of student :- ")
Class = input("Enter the Class of student :- ")

English = int (input("Enter the Marks of english :-"))
Maths = int (input("Enter the Marks of maths :- "))
Science = int ( input("Enter the Marks of science:- "))
Social_science = int(input("Enter the Marks of sst :-"))
computer = int(input("Enter the Marks of computer :- "))

result = English + Maths + Science + Social_science + computer
print("---------------------------------------------------------------")
print(f" Name :{name} \n Roll No : {Roll_no}  \n Class : {Class}")
print("---------------------------------------------------------------")
print(f" Subject       Full marks      Obtained Marks")

print(f" English         100             {English}")
print(f" Maths           100             {Maths}")
print(f" Science         100             {Science}")
print(f" Social science  100             {Social_science}")
print(f" computer        100             {computer}")
print("---------------------------------------------------------------")
print(f"Total :          500            " ,  result )


print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")