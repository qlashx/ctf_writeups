###description -> Welcome to LA CTF 2024! All you have to do is accept the terms and conditions and you get a flag!
-------------------------------------------------------------------------------------------------------------------
**upon the description lets access the website and accept the conditions :D**

**the main page was like this and i cannot click on the accept button (it use js and play with it)**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/edd1c2f8-b241-4a9f-911d-ddf80c8c2c0b)

**so made view page source and start seeing the code**

**there was an intersting js file called analytics.js that is hosted in the same server with the app (not a third party code) so lets open and see what dose it has**

![image](https://github.com/qlashx/ctf_writeups/assets/106611511/631029ed-f02e-429e-88ac-4c9bf711b05b)

**so this code seems to be a obfuscated js code so lets make it readable (i used https://obf-io.deobfuscate.io/ to make it readable) and the output was like this**

```document.getElementById("accept").addEventListener("click", () => {
  const _0x4eb4e0 = document.getElementById("mainscript");
  if (!_0x4eb4e0 || _0x4eb4e0.innerText.length < 1000) {
    alert("silly you... you don't get to disable javascript...");
  } else {
    alert("ob`wexwkbw\\avwwlm\\tbp\\gfejmjwfoz\\mlw\\lmf\\le\\wkf\\wfqnp~".split``.map(_0x286792 => String.fromCharCode(_0x286792.charCodeAt(0) ^ 3)).join``);
  }
});
1;```
**so lets convert the else part to be readable i used this code to convert it**

```const characters = "ob`wexwkbw\\avwwlm\\tbp\\gfejmjwfoz\\mlw\\lmf\\le\\wkf\\wfqnp~".split('');
const transformedCharacters = characters.map(char => String.fromCharCode(char.charCodeAt(0) ^ 3));
const result = transformedCharacters.join('');
alert(result);
```
**after decoding the value and alerting  the result -> i got the flag -> lactf{that_button_was_definitely_not_one_of_the_terms}**
