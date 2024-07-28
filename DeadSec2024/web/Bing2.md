## Walkthrough :
  **the challange was provided with a source code so lets check it first**
  
  ![image](https://github.com/user-attachments/assets/2b71162a-fac3-4ddd-902e-7e68502247f0)


  ![image](https://github.com/user-attachments/assets/85e83dc8-d548-4995-a31f-0802ea61b76e)

  **upper code is the bing.php hmmmmm so our goal is to bypass the validations and be able to execute commands on the server right? (os command injection) but how ?**
  
  **first is that str_replace search for the string and remove all of the occurrence of it in the input but it does not make a back track after the remove operation**
  
  **so if your input is like this cacatt -> it will match the inner cat and remove it so when it remove it will continue serach from the next char which in our case is t but it will not look back**
  
  **okay we now can insert commands but it fillter any ; and | ....etc**
  
  **so if we take a look at the substitutions array will see a key (; ) which mean ; and space after it and str_replace will search for the exact string so what about inserting (;) only the code will not fillter it**

  **it do the same for the (/ ) which means that we can use the same bypass by inserting only /**

  **note even if you insert the space after the / or ; it will get matched by the first key in the array and get deleted so .........**

  **we can now build our payload to get the flag**
  **payload -> ;cacatt%09/flaflagg.txt**
