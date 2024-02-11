## description -> Remember Bruh 1,2 ? This is bruh 3 : D login with admin:admin and you will get the flag :*
-------------------------------------------------------------------------------------------------------------
**The challenge also included a source code**

**so lets first see the main page of the website** 

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/433432f5-c0f3-45d8-af64-dd3502f6b2ae)

**this is a very basic login page so lets try to login with admi/admin and see what will happen**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/f2bdebfc-7460-4a97-86c0-3f59b5583ada)
**As i was expecting never trust the description**

**So lets take a look at the provided source code**

**We was having two main files app.py and index.php.**

**There was an interesting file named "init.db" that was creating a database and inserting only "admin" as both the username and password.**

**So, now that we only have "admin" in the database and we attempted to log in with it, we received the aforementioned response.**

**Let's examine the "index.php" file to understand how the login functionality is implemented and why it might be returning the upper response**

**The index.php consisted of three main functions.**

**1- Check_Admi**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/8cf9f216-213c-4b64-bc51-7ec136924ed9)

**2-send_to_api**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/5f5887dd-c84e-4157-b504-a1a2ea9dc734)

**3- post request handeler**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/f739198b-843d-48df-8f0a-866d4334caae)
**so lets now  undesrtand how the code work**

**The first function receives the data from the POST request and saves it in variables for username and password. It then passes the username to a function called "check_admin" and retrieves the IP address of the sender of the request, comparing it to the localhost IP**

**Let's examine the "check_admin" function to understand its implementation and how it interacts with the login process.**

**The "check_admin" function appears to be a regular expression that matches the word "admin" regardless of its case (whether in lowercase or uppercase).**

**So, since attempts to bypass the regex filter using techniques like inserting newline characters (\n) were unsuccessful,so i strated exploring alternative approaches.**

** The other approache was that  i extensively researched methods to manipulate the server into indicating that the originating IP is 127.0.0.1 to PHP, but despite attempting a 403 header bypass, I was unsuccessful. :( )**

**After some testing and attempts to send payloads such as double URL encoding, I noticed a significant detail: when the data reaches the application and I send it with double URL encoding, it only undergoes a single URL encoding process. This seemed strange to me because, as far as I understand, the server initially receives the data and then decodes it (first URL decode). Following this, PHP checks the data, allowing it to bypass and sending it to the API. Finally, when the API receives the data, it decodes it once again. Hence, I found it puzzling why only one URL encoding process occurs.**

**It appears that in the PHP post request handler, encoded data isn't sent, but rather the raw request is sent again to the API. This reveals a vulnerability wherein we can utilize HTTP parameter pollution to gain admin access. However, the reason behind this vulnerability isn't immediately clear. but why i will try HTTP parameter pollution**

**bc In PHP, when encountering two parameters with the same name, it prioritizes the second parameter. However, in Python, it prioritizes the first. Hence, we can exploit this by sending a request like this: "username=admin&username=qlashx&password=admin". PHP will validate "qlashx" as the username and resend all the request data to the API. Python, on the other hand, will receive the first username, which is "admin"**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/66b8377c-dea6-4f3a-8b98-3efed6ee1335)

`0xL4ugh{M1cr0_Serv!C3_My_Bruuh}`
