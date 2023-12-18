# description -> (I left a message for you. You will love it definitely) 
**The challenge also included a source code.**
# challenge link -> http://34.132.132.69:8003/

**This is the main page in the given website**

**It's nothing out of the ordinary, but if you check the URL, you'll notice a "file" parameter in the GET request, indicating a possible link to an LFI or LFD vulnerability.** 

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/e6916b1b-8830-444d-8e3b-2431aeb1d30f)

**But lets first examin the sorce code**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/2ba882e7-a4a7-44b9-bdd5-3c3f8bca9298)

**Upon reviewing the files in the source code, it becomes apparent that the flag is likely stored on the server. Our objective is to identify a server-side vulnerability to obtain the flag.**


**so lets start examining the app.py file**

**The source code had two primary routes. The initial route was for the main page ("/"), and the second route was designated for the "/read_secret_message" endpoint**

**And here is the code for both routes**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/1bd67ad9-3b8b-4b4c-8e63-7abd047bf374)

**At first the route for the main page is just a normal route nothing suspicious in it**

**But The "/read_secret_message" route could potentially serve as our entry point to solve the challenge.**

**if we looked at the read_file function and start analyzing it**

**Initially, it retrieves a parameter named "file" from the GET request.**

**And pass it to function called useless we will look at it later on**

**And then take the returned value from the useless and reasgin it to file_param**

**And after it use os.path.join (built in fucntion) and add the base_directory varibale to our file_param**

**And then try to open this file and read its content and return it as response**

**in this stage i was sure that iam facing an lfd challenge with some input validation**

**so lets get back to thee useless function and see what dose it do**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/74fc9b63-530a-4e6c-bded-a064a58470a0)

**in the useless function it call two other functions called ignore_it and another_useless_function** 

**so lets examine both function** 

**At first the ignore it function take the file param (file parameter from the get request)**

**Then, it utilizes the replace function to substitute every "." and "/" with a space. This is a common input validation technique aimed at preventing attackers from accessing files within the system.)**

**The another_useless_function was used to make url decode**

**At first i tried to bypass the replace function and being able to inject . and / without removing it but i failed :(**

**Returning to the seemingly useless function, I noticed that it calls another_useless_function multiple times. This presented an opportunity for me to leverage URL encoding, potentially bypassing the validation. By encoding the . and / in my paload , when the another_useless_function is invoked, it automatically decodes my input. This strategy allows me to inject "." and "/" without the risk of them being removed by the replace function.**

**And this was right but if we looked at the useless fucntion we will see that he start with calling the ignore_it and then another_useless_function and then the ignore_it agin and then 2 more times he call the another_useless_function so to make this work we have to make 3 time url encode :)**

**so now we know what we will do but we have to know where is the flag at the server**

**if we looked at the docker file we will see that he copy the flag to this place /secret_of_j4ck4l/flag.txt**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/d386773c-dd5e-4843-a885-8febfbf35dfd)

**Here, I successfully bypassed the useless function. As for the os.path.join function appending a path to our input, it wasn't a significant issue. Notably, if you provide os.path.join with an absolute path (a path that starts with "/"), it will disregard the other paths and won't concatenate them together. You can verify this in the Python documentation for further details.** 



**so finally our payload will be like this** 
**/secret_of_j4ck4l/flag.txt but we will encode the / and . theree times to be like this**
### %25252Fsecret_of_j4ck4l%25252Fflag%25252Etxt

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/c8befc90-871b-4564-80b9-2123aafebb20)






      
