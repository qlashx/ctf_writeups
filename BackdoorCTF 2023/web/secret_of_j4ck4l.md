# description -> (I left a message for you. You will love it definitely) 
**The challenge also included a source code.**
# challenge link -> http://34.132.132.69:8003/

**This is the main page in the given website**

**It's nothing out of the ordinary, but if you check the URL, you'll notice a "file" parameter in the GET request, indicating a possible link to an LFI or LFD vulnerability.** 

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/e6916b1b-8830-444d-8e3b-2431aeb1d30f)

**But lets first examin the sorce code**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/2ba882e7-a4a7-44b9-bdd5-3c3f8bca9298)

Upon reviewing the files in the source code, it becomes apparent that the flag is likely stored on the server. Our objective is to identify a server-side vulnerability to obtain the flag.


