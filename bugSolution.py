def function_with_uncommon_error_solution(a, b):
    if a == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    else:
        result = b / a
        return result

# Example usage
print(function_with_uncommon_error_solution(0, 10)) # This raises the ZeroDivisionError
print(function_with_uncommon_error_solution(10, 0)) # This raises the ZeroDivisionError
print(function_with_uncommon_error_solution(5,2))