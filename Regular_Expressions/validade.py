import re

email = input("What's your email? ").strip()

if re.search(".+@.+", email):
    print("Valid")
else:
    print("Invalid")

#creating a new method to check if the entered string is an email address
# username, domain = email.split("@")

# if username and domain.endswith(".edu"):
#     print('Valid')
# else:
#     print("Invalid")

# basic example how to search if the string is a email or not
# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")