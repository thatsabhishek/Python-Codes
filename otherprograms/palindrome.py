"""
Check if entered string is palindrome or not.
"""

entered_text = input("Enter something: ")
reverse_text = entered_text[::-1] # this will reverse the entered string and stored it in variable reverse_text

if entered_text == reverse_text:
    print(f"Yes {entered_text} is a palindrome!")
else:
    print(f"No {entered_text} is not a palindrome!")