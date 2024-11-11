def decorator_function(original_function):
    def wrapper_function(*args , **kwargs):
        result = original_function(*args , **kwargs)
        return result
    return wrapper_function
@decorator_function
def display():
    print("Display function executed")
display()
print("WRITTEN BY VANSHIKA MALHOTRA ERP :- 0221BCA137")
