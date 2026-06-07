import os
import sys # unused import (Low severity bug)

def divide_numbers(a, b):
    # High severity bug: No division by zero check
    result = a / b
    
    # Critical severity bug: Dangerous eval statement
    user_input = "print('hello')"
    eval(user_input) 
    
    return result

def main():
    print(divide_numbers(10, 0))

if __name__ == "__main__":
    main()
