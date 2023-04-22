import re

password = input("Enter a password: ")
if len(password) < 8:
    print("Password length should be at least 8 characters.")
else:
    lowercase_regex = re.compile('[a-z]')
    if not lowercase_regex.search(password):
        print("Password should contain at least one lowercase letter between a and z.")
        
    uppercase_regex = re.compile('[A-Z]')
    if not uppercase_regex.search(password):
        print("Password should contain at least one uppercase letter between A and Z.")
    digit_regex = re.compile('[0-9]')
    if not digit_regex.search(password):
        print("Password should contain at least one digit between 0 and 9.")
    special_regex = re.compile('[$#@]')
    if not special_regex.search(password):
        print("Password should contain at least one special character from $, #, @.")
    if (lowercase_regex.search(password) and uppercase_regex.search(password)
            and digit_regex.search(password) and special_regex.search(password)):
        print("Password is valid.")
