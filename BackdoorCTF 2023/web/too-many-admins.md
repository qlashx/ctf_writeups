#description -> Too many admins spoil the broth. Can you login as the right admin and get the flag ?

**there was a sorce code provided with this challenge**

## link -> http://34.132.132.69:8000/

**This is the main page for the website**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/d622f991-682a-4b00-9c1d-022eec4e5f83)

**Let's begin by examining the source code first.**

**The source code mainly consisted of four files.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/288e6a9f-8121-43cf-8b02-fee3d6ea96fb)

**Let's begin by reviewing the contents of the "dump.sql" file.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/1c5ddf28-abb8-4298-8d56-c86eb6c4f8bc)

**First, the code initiates the creation of a table named "users," defining columns, and other associated elements.**

**Then, a function is created to generate 500 random admin users, with one specific admin whose bio contains the flag.** 

**Now, the idea that came to mind is to search for SQL injection vulnerabilities, dump the data from the database, and retrieve the flag! 😄**

**Now, let's begin by examining the content of the "index.php" file to find the sqli .**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/7806de29-5758-4b49-9802-a0bcd004b19c)

**After some investigation, I discovered that the page accepts a "all" parameter in the GET request, allowing for the dumping of all data. However, this feature is less useful since the flag is located in the bio, making it challenging to extract through a standard data dump.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/1d0b0ddd-68b2-4ca1-9c18-238283249e2d)

**Then, I observed that the application processes a POST request containing a supplied username and password**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/4a1cec47-f70c-4f30-bb97-5aded8e27194)

**so here It seems there might be a potential SQL injection (SQLi) vulnerability, as the username appears to go directly into the database without proper validation or the use of parameterized queries. This lack of input sanitization could be an entry point for exploiting SQL injection.**
**but It appears there's an additional layer of complexity in the authentication process. After taking your password, it's hashed and subjected to certain operations. The resulting hash is then compared with the stored password from the database and a static value. This adds a challenge to exploiting a straightforward SQL injection, as the hashed and manipulated password needs to match the expected values for successful authentication.**
**but i noticed smth that he cast the returend password from the database as int and compare it with $mysupersecurehash which is a string and then compare agin the mysupersecurehash with another integer value**
**here i start thinking of type juglling (magic hash) which is when comparing string hashes to integers. If a string hash starts with "0e" followed by only numbers, PHP interprets this as scientific notation and the hash is treated as a float in comparison operations. for more info look here -> https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md**

**So, I began contemplating how to structure my input so that, after being hashed and subjected to operations, it starts with "0e" followed by numeric values.**
**The only solution that came to mind was to resort to a brute-force approach.**
**So, I sought assistance from a friend, and together we created a Python script to iterate and obtain the desired value.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/0c1debf7-515c-4c73-8364-7b76d782b224)

**After running this script it output this number**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/d69a663a-7263-4dd7-ad24-04ec3ae6adce)

**After obtaining the numeric value, I revisited the main page and inputted the username as 'admin' OR 1=1 -- - and the password as the obtained numeric value, which was 355933.**
**And pingo we got the flag :D**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/f236d4ff-17eb-4270-bfbe-8e625fbc0464)






