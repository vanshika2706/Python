# Function to check if a string is a palindrome
def is_palindrome(string):
    # Convert the string to lowercase and remove spaces
    string = string.lower().replace(" ", "")

    # Check if the string is equal to its reverse
    return string == string[::-1]


# Input from the user
user_input = input("Enter a string: ")

# Check and print if the input is a palindrome
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")