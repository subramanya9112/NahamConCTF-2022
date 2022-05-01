```
Have you ever broken out of jail? Maybe it is easier than you think!

PS (not challenge related), thank you so much to Zero-Point Security for supporting NahamCon 2022!

Press the Start button on the top-right to begin this challenge.

Connect with:
# Password is "userpass"
ssh -p 32634 user@challenge.nahamcon.com
Please allow up to 30 seconds for the challenge to become available.
```

```
Press ctrl-d to come out of try-except block
>>> import os
>>> os.getcwd()
'/home/user'
>>> files = os.listdir('.')
>>> print(files)
['flag.txt', 'jail.py', '.user-entrypoint.sh', '.profile', '.bashrc']
>>> print(open("flag.txt", "r").read())
flag{c31e05a24493a202fad0d1a827103642}
```