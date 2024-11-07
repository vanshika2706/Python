a = b = [1,2,3]
c = [1,2,3]
print('id(a)', id(a) , 'id(b)', id(b), 'id(c)', id(c))
#id of a and b is same , but c's is diffrent
var1 = a is  b #output: True
print(var1)
var2 = a is c #output: False
print(var2)
#a and c are diffrent objects
print("Written By Vanshika Malhotra ERP :- 0221BCA137")