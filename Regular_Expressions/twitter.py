import re

url = input("URL: ").strip()

if matches := re.search(r"^(?:https?://)?(?:wwww\.)?twitter\.com/([a-z0-9_]+)$",url,re.IGNORECASE):
    print("Username:", matches.group(1))

# username = re.sub(r"^(http(s)?://)?(wwww\.)?twitter\.com/", "", url)
# print(f"Username: {username}")