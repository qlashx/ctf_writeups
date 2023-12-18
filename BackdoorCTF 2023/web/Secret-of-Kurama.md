# description -> Madara attacked leaf village. everyone wants Naruto to turn into Nine-Tails, Naruto don't know what's the SECRET to change its role to 'NineTails'? can you as a shinobi help Naruto??? username: Naruto Password: Chakra

**No sorce code was provided in this challenge**

# link -> http://34.132.132.69:8004/ 

**after reading the description i notice that we have to know a secret and use it change our role to NineTails but what secert that we need to know**

**after logining in using the provide credentials**

**I saw two links like this.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/b19224ad-eaab-4ad0-aa06-50bfa35a508d)

**And here as well, I clicked on the first link, but I didn't understand anything.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/41352f2d-637a-4dee-8d97-5788950bc7d0)

**Next, I clicked on the second link.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/7c5a6ecb-a08a-4d7e-aeba-95c51daa1d65)

**It informed me that I'm not permitted to discover the secret, and the title displayed "Access Denied."**

**Later, a question popped into my mind: how did he know I wasn't allowed to access the secret? The answer became apparent through the session.**

**I acquired the session, and it happened to be a JWT session.**

**After decoding the session using jwt.io, it appeared in this manner.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/d0f86f1e-ddd6-4058-93b0-964460ec18f6)

**Here, I noticed a "role" in the data, and the objective is to obtain the secret and switch our role to "NineTails**

**so I used  Hashcat to crack the JWT and retrieve the secret.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/a337121e-3730-4c02-857a-2b5f24e21fa4)

**Following that, I utilized this Python code to generate a new JWT token.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/631ecf90-4138-4972-a3ad-af0e4e16d767)

`
**And it gave me this token ->eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Ik5hcnV0byIsInJvbGUiOiJOaW5lVGFpbHMifQ.rDZ26ZE_F4l0Ve4E-2sKP4qKNuadhLU8nrThW7YGVPg**

**Afterward, I replaced the token on the website with the one I generated and attempted to access the "secret_of_Kurama" endpoint.** 

**And pingo it wokred and the secert was the flag :D**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/ee7ca72f-aa6c-4b29-8ccb-72c2f8fe0266)








