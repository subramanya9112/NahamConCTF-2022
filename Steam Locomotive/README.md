```
I keep accidentally mistyping the ls command!

Press the Start button on the top-right to begin this challenge.
Connect with:
# Password is "userpass"
ssh -p 30822 user@challenge.nahamcon.com
```

```
$ echo "cat flag.txt" | ssh -p 30822 user@challenge.nahamcon.com
Pseudo-terminal will not be allocated because stdin is not a terminal.
user@challenge.nahamcon.com's password:
flag{4f9b10a81141c7a07a494c28bd91d05b}
```