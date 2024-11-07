text = "Hello, World !"

lowercase_text  = text.lower()
uppercase_text = text.upper()
trimmed_text = text.strip()

replaced_text = trimmed_text.replace("World" , "Python")
#Splitting And Joining
words = trimmed_text.split()
joined_text = "-".join(words)

#Formatting strings
name = "Alice"
language = "Python"
formatted_string = f"{name} loves {language}"

#Output the result
print(f"{lowercase_text}")
print(f"{uppercase_text}")
print(f"{trimmed_text}")
print(f"{replaced_text}")
print(f"{joined_text }")
print(f"{formatted_string}")

normal_string = "This is a newline character : \n"

raw_string = "This is newline character : \n"
print("Normal String : " , normal_string )

print(" Raw String : " , raw_string)

print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")
