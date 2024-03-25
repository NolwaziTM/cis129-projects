# Module 08- lab 08
# Author: Nolwazi Moyo
# Title : PALINDROME TESTER
# Date: 03/25/2023

def is_palindrome(s):
    # Function to preprocess the string: remove spaces and punctuation and convert to lowercase
    def preprocess(s):
        return ''.join(char.lower() for char in s if char.isalnum())

    # Preprocess the input string
    s = preprocess(s)
    
    # Create an empty stack
    stack = []
    
    # Push each character of the first half of the string onto the stack
    for char in s[:len(s)//2]:
        stack.append(char)
    
    # Compare each character in the second half of the string with the popped characters from the stack
    for char in s[len(s)//2 + len(s)%2:]:
        if char != stack.pop():
            return False
    
    # If the loop completes without returning False, the string is a palindrome
    return True

# Test the function
print(is_palindrome('radar'))  # True
print(is_palindrome('A man, a plan, a canal, Panama'))  # True
print(is_palindrome('hello'))  # False
