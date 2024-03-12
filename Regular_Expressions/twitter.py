import re

url = input("URL: ").strip()

username = re.sub(r"^(http(s)?://)?(wwww\.)?twitter\.com/", "", url)

print(f"Username: {username}")