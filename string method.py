text = "Hello, World !"
#changing case
lowercase_text  = text.lower()
uppercase_text = text.upper()
title_text = text.title()

#Trimming Whitespace
stripped_text = text.strip()

words = stripped_text.split(",")
joined_text = "-".join(words)

#Replacing and finding
replaced_text = stripped_text.replace("World" , "Python")
index = stripped_text.find("World")
count = stripped_text.count("o")

print(f"{lowercase_text}")
print(f"{uppercase_text}")
print(f"{title_text}")
print(f"{stripped_text}")
print(f"{joined_text}")
print(f"{words}")
print(f"{replaced_text}")
print(f"{index}")
print(f"{count}")

print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")