# description -> Madara attacked leaf village. everyone wants Naruto to turn into Nine-Tails, Naruto don't know what's the SECRET to change its role to 'NineTails'? can you as a shinobi help Naruto??? username: Naruto Password: Chakra

**No sorce code was provided in this challenge**

# link -> http://34.132.132.69:8004/ 

**after reading the description i notice that we have to know a secret and use it change our role to NineTails but what secert that we need to know**

**after logining in using the provide crids**

**I saw to links like this**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/b19224ad-eaab-4ad0-aa06-50bfa35a508d)

**i cliked on the the first link but i didnt undestand anything**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/41352f2d-637a-4dee-8d97-5788950bc7d0)

**then i clicked on the second link**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/7c5a6ecb-a08a-4d7e-aeba-95c51daa1d65)

**It told me I'm not allowed to know the secret, and the title was "Access Denied"**

**Then a question crossed my mind: how does he know that I'm not allowed to see the secret? The answer lay in the session.**

**I obtained the session, and it turned out to be a JWT session**

**after decodeing  the session using jwt.io it looked like this**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/d0f86f1e-ddd6-4058-93b0-964460ec18f6)

**so here i saw a role in the data and the traget is to get the secret and change our role to NineTails**

**so i used hashcat to crack the jwt and get the secret**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/a337121e-3730-4c02-857a-2b5f24e21fa4)

**After this i used this python code to get generate a new jwt token**
`import jwt
  encoded_jwt = jwt.encode({  "username": "Naruto","role": "NineTails"}, "minato", algorithm="HS256")
  print(encoded_jwt)
`
**And it gave me this token ->eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Ik5hcnV0byIsInJvbGUiOiJOaW5lVGFpbHMifQ.rDZ26ZE_F4l0Ve4E-2sKP4qKNuadhLU8nrThW7YGVPg**

**And then i replace the token on the website with the one that i genertae and tried to access the secret_of_Kurama end point** 

**And pingo it wokred and the secert was the flag :D**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/ee7ca72f-aa6c-4b29-8ccb-72c2f8fe0266)








