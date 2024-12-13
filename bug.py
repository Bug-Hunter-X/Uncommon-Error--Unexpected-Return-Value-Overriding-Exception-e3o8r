def function_with_uncommon_error(a, b):
    if a == 0:
        return 0 # This return statement is problematic
    else:
        result = b / a
        return result

#Example usage
print(function_with_uncommon_error(0, 10))
print(function_with_uncommon_error(10,0))