import functools

# Decorator function to check for permissions
def requires_permission(permission):
    def decorator(func):
        @functools.wraps(func)  # Corrected functools.wraps usage
        def wrapper(*args, **kwargs):
            user_permission = get_current_user_permission()  # Assumes this function is defined
            if permission in user_permission:
                return func(*args, **kwargs)
            else:
                raise PermissionError("You do not have permission to access this resource")
        return wrapper
    return decorator

# Applying the decorator to the delete_user function
@requires_permission('admin')
def delete_user(user_id):  # Fixed the function name, replaced '-' with '_'
    print(f"User {user_id} deleted")

# Example usage (you need to define `get_current_user_permission` for it to work)
