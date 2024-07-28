## Walkthrough :
  **the challenge was provided was a source code lets look at it**

  ![image](https://github.com/user-attachments/assets/f9717d91-d817-4ab9-b444-be24f6ba98d7)

  **upper is the app.py**

  **as we can see there is no validation or sanitizaion so we can execute code as we want but we cannont see the output of it**

  **and if the code made an error we are not able to see the error also**

  **why we cannot see errors -> bc os.system does not raise exceptions, the except blocks for subprocess.CalledProcessError and subprocess.TimeoutExpired will never be executed**
  
  **first thing came to my mind is to copy the flag to the static dir but unfortunately i cannot make a write operation to the  /app dir** 
  
  **then i thought of Time based data exfiltration and made this payload ;cat+/flag.txt+|cut+-c+1|+grep+-q+'^b'+%26%26+sleep+10  lets explain it**

  **first it will cat the flag and pass it to cut that will take the first char and then pass it to grep if the char is b grep will match and then the server will sleep if not it will not sleep**

  **so it is clear that you have to bruteforce the chars till you get the flag by increasing the cut one every time cut -c 2 to grep the secound char .....etc**
