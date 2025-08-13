def is_palindrome(s):
    cleaned_str = ''.join(s.split()).lower()
    return cleaned_str == cleaned_str[::-1]

test_strings = ["racecar", "hello", "A man a plan a canal Panama", "madam", "12321"]

for test_string in test_strings:
    if is_palindrome(test_string):
        print(f"'{test_string}' is a palindrome!")
    else:
        print(f"'{test_string}' is not a palindrome.")
