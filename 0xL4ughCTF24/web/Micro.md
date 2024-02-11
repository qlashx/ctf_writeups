## description -> Remember Bruh 1,2 ? This is bruh 3 : D login with admin:admin and you will get the flag :*
-------------------------------------------------------------------------------------------------------------
**The challenge also included a source code**
**so lets first see the main page of the website** 
![image](https://github.com/qlashx/ctf_writeups/assets/106611511/433432f5-c0f3-45d8-af64-dd3502f6b2ae)
**this is a very basic login page so lets try to login with admi/admin and see what will happen**
![image](https://github.com/qlashx/ctf_writeups/assets/106611511/f2bdebfc-7460-4a97-86c0-3f59b5583ada)
**as i was expecting never trust the description**
**so lets take a look at the provided source code**
**we was having two main files app.py and index.php**
**but there was an intersting file calleed init.db which was creating an db and inserting only admin as a username and password**
**so now we now we have only admin in the db and we need login with it but when we tried it it give us the upper text response**
**so lets take a look at the index.php**
**the index.php was consisting of 3 main functions**
**1- Check_Admi**
![image](https://github.com/qlashx/ctf_writeups/assets/106611511/8cf9f216-213c-4b64-bc51-7ec136924ed9)

**2-send_to_api**
![image](https://github.com/qlashx/ctf_writeups/assets/106611511/5f5887dd-c84e-4157-b504-a1a2ea9dc734)

**3- post request handeler**
![image](https://github.com/qlashx/ctf_writeups/assets/106611511/f739198b-843d-48df-8f0a-866d4334caae)
**so lets know undesrtand how the code work**
**first it take on the data that is comming from the post request and save it in the username and passsword and then send the username to check admin function and get the ip of the sender of the request and compare it to the localhost ip**
**so lets examin the check-admin fucntion**
**it is a normal regex that will match admin word if beining inserted weather in small or capital form**
**here i thought i could bypass the regex and can insert admin but depending on hacktricks i couldnt bypass this regex with smth like \n so i started looking in another way**
**Then i searched alot to force the server to send that the orginating ip is 127.0.0.1 to php but i cannt also (i used 403 header bypass but it didnt work :( )**
**after a while of testing and trying to send payloads like douple url encoding i notice an important thing that the data when it get to the api when i send it like douple url encoding it make only a single url encode and acording to my knwoladge it was strange bc the server take the data at first and then decode it (first url decode) and then php check on the data and it will bypass and send it to the api and when the api get the data it will decode it once again so why there is an only one url encode happens**
**it turned of that php in the post request handeler it dosent send the encoded data but it send the row request agin to the api and here is the vuln that we can use http parameter pullition to get admin acceses but why**
**bc in php when it see two parameters witht the same name it take the second but in python it take the first so wen could send a request like this -> username=admin&username=qlashx&password=admin -> and this will work bc php will validate on qlashx as username and send all of the request data agin to api and api is working python will get the first username which was admin**
![image](https://github.com/qlashx/ctf_writeups/assets/106611511/66b8377c-dea6-4f3a-8b98-3efed6ee1335)
`0xL4ugh{M1cr0_Serv!C3_My_Bruuh}`
