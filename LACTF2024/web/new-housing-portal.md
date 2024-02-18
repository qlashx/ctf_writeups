## Description:

**After that old portal, we decided to make a new one that is ultra secure and not based off any real housing sites. Can you make Samy tell you his deepest darkest secret?
Hint - You can send a link that the admin bot will visit as samy.
Hint - Come watch the real Samy's talk if you are stuck!
Site - new-housing-portal.chall.lac.tf
Admin Bot - https://admin-bot.lac.tf/new-housing-portal**

**There was a source code provided with the chall**

## Walkthrough:
**First, let's access the main page of the website.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/562b27fc-267a-4bb0-9360-dd340f64812e)

**So, there are a lot of functions here. Let's interact more with the web app.**

**After some time spent interacting with the web app, I noticed two other functions: "find" and "invite." Let's take a look at the source code to gain a deeper understanding.**

**Initially, the user data was stored as a map.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/a930a03e-e701-4879-ad67-7d7abe5d89bd)

**There is a user called Samy who has a flag in his data. How can we retrieve the flag?**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/f6fbd19e-4251-4e6a-837d-ed8c268c2c12)

**There is a function called /finder that takes the input and only trims it. It then searches the map for the name and sends an invite with the sender's information, along with the deepestDarkestSecret -> flag in Samy's data.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/cf0267c4-8bd9-45aa-942a-9672f8b30166)

**so we need smay to send an invite to us to get the flag but how**

**There is a route called /register that takes the user input and puts it in the map without any validation or sanitization.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/bd07474a-3c8b-4ac0-8c10-07c14b1d4a

**We could exploit the lack of validation and sanitization in the /register route by registering with an input that contains JavaScript code to send an invite to ahmed2 (my username). Then, we could use the /finder route to search for the JavaScript code and send the link to Samy. When Samy clicks on the link, the JavaScript code would execute in his browser, inviting you and potentially allowing you to retrieve the flag.**

**And this was right i used this script 
```<img src="x" onerror='fetch("https://new-housing-portal.chall.lac.tf/finder", {method: "POST", mode: "no-cors", headers: {"Content-Type": "application/x-www-form-urlencoded"}, body:"username=ahmed2"});'>```
as name and send the link like this 
https://new-housing-portal.chall.lac.tf/finder/?q=%3Cimg%20src%3D%22x%22%20onerror%3D%27fetch(%22https%3A%2F%2Fnew-housing-portal.chall.lac.tf%2Ffinder%22%2C%20%7Bmethod%3A%20%22POST%22%2C%20mode%3A%20%22no-cors%22%2C%20headers%3A%20%7B%22Content-Type%22%3A%20%22application%2Fx-www-form-urlencoded%22%7D%2C%20body%3A%22username%3Dahmed2%22%7D)%3B%27%3E to samy and i got the invite :D and the flag**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/df1008d4-4a3c-4c7c-8933-378adc157305)

