email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print('Valid')
else:
    print("Invalid")

# basic example how to search if the string is a email or not
# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")