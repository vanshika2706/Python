myAge = input("Enter age :")
myAge = int(myAge)
if myAge >= 18:
    myComment = "You Can Vote"
else:
    if myAge >= 10 :
        myComment = "You Are In middle school"
    else:
        if myAge    >= 6:
            myComment = "You are In primary School"
        else:
            myComment = "You are too small to learn python"
print("At age :" + str(myAge) + "-> " +myComment)

print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")
