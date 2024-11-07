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


marks = result/5
if marks >= 80 :
    print(" Your grade is O ")
elif marks >= 70 :
    print("Your grade is A+ ")
elif marks >= 60 :
    print(" Your grade is A ")
elif marks >= 50 :
    print("Your grade is B+ ")
elif marks >= 40 :
    print("Your grade is C ")
else:
    print("Your grade is D \n you`re fail")


print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")