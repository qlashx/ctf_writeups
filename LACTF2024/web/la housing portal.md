## Description:
**Portal Tips Double Dashes ("--") Please do not use double dashes in any text boxes you complete or emails you send through the portal. The portal will generate an error when it encounters an attempt to insert double dashes into the database that stores information from the portal**
**Also, apologies for the very basic styling. Our unpaid LA Housing(tm) RA who we voluntold to do the website that we gave FREE HOUSING for decided to quit - we've charged them a fee for leaving, but we are stuck with this website. Sorry about that.**
**Please note, we do not condone any actual attacking of websites without permission, even if they explicitly state on their website that their systems are vulnerable.**

**There was a source code provided with the chall**

## Walkthrough:

**First, let's access the main page of the website.**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/7037c2f9-db42-407c-b173-1c363ba96d76)

**So, let's install the source code and try to understand what dose the app do with this form**

**After installing the source code, I found a route called /submit that accepts POST requests containing the submitted data from the main page.** 

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/a9df0eb1-2a6d-4b88-89ef-fa38dbeef52a)

**There is extensive input validation in place. For instance, you cannot input '--' or '(/*)', and the value must not exceed 50 characters while the key must not exceed 10 characters.**

**After your code passes the validation, it is sent to the 'get_matching_roommates' function, which contains the vulnerability**

**so lets understand get_matching_roommates function**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/76577f23-b2f2-4dc5-8105-b58787e29bf9)

**It takes the input as a dictionary (key and value) and proceeds to insert the data into the database without any validation or using parameterized queries**

**So, we can craft a payload containing a SQL injection to exploit this vulnerability and read the flag. The flag is stored in another table in the database, which can be seen in the data.sql file**

**However, there are constraints on the payload size and commenting out portions of the SQL query is blocked within the search_roommates function in the /submit route code.**

**So, I considered a different approach by attempting to fix the SQL query directly instead of commenting out portions of it. However, I encountered difficulties due to the size limitation, especially when using operators like the LIKE operator.**

**But finally i used made this payload ```'UNION+SELECT+1,2,3,4,5,*+FROM+flag+where+'a'='a``` to get the flag lets understand it**

**At first, I used a single quote ' to close the open quote, and the UNION operator to execute another query. The selection of 1,2,3,4,5 was necessary because the first query returned 6 rows, and to make the UNION operation work, the two queries must return the same number of columns. Then, I selected the table called 'flag,' and the condition in the 'WHERE' clause was set to 'a'='a to ensure it always evaluates to true+to make the sql query dosent make error (there is a ' that we used to make comment to make the sql work)****

