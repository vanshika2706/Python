#bytes data type
print("Bytes Example")
#Creating a byte object
b = bytes ([65,66,67,68])
print(b)
print(b[0])
print(b[2])

for byte in b :
    print(byte,end ='')
    print("\n")

#Bytearray Example
print("Bytearray Example")
#Creating Bytearray object
ba =bytearray([65,66,67,68])
print(ba)

#modifying elements in a bytearray
ba[0]= 97 #changing bytearray from 65 to 97
print(ba)

for bytearray  in ba :
    print(bytearray,end ='')
    print("\n")

    #Memoryview Example
    print("Memoryview Example:")
    #creating a byte object
    b_mv = bytes([65,66,67,68,69])

    # Creating a memoryview object
    mv = memoryview(b_mv)
    print(mv)
    # Accesing elements through memoryview
    print(mv[0])

    #Slicing memory
    mv_slice = mv[1:4]
    print(mv_slice.tobytes())

    #creating a bytearray and a memoryview
    ba_mv = bytes([65,66,67,68,69])
    mv_ba = memoryview(ba_mv)

    #Modifying the orignal bytearray through memoryview
    mv_ba[0] = 97
    # Changing 'A'(65) to 'a'(97)
    print(mv_ba)
    #Output: bytearray(b'aBCD')

print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")

