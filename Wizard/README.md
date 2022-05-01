```
You have stumbled upon a wizard on your path to the flag. You must answer his questions!

We are seeing some trouble with the very last question, asking for hexadecimal, when it really takes the answer in plaintext. We are rebuilding the challenge image but in the interim, please send it the plaintext rendition of your answer for question 6.

PS (not challenge related), thank you so much to Hadrian for supporting NahamCon 2022!

Press the Start button on the top-right to begin this challenge.

Connect with:
nc challenge.nahamcon.com 30766
Please allow up to 30 seconds for the challenge to become available.
```

```
$ nc challenge.nahamcon.com 30766

/------------------------------------------\
| Why hello passerby. I see you wish to    |
| pass, however you must answer my six     |
| questions correctly in order to do so.   |
\---------------  -------------------------/
                \/
              _,._
  .||,       /_ _\\
 \.`',/      |'L'| |
 = ,. =      | -,| L
 / || \    ,-'\"/,'`.
   ||     ,'   `,,. `.
   ,|____,' , ,;' \| |
  (3|\    _/|/'   _| |
   ||/,-''  | >-'' _,\\
   ||'      ==\ ,-'  ,'
   ||       |  V \ ,|
   ||       |    |` |
   ||       |    |   \
   ||       |    \    \
   ||       |     |    \
   ||       |      \_,-'
   ||       |___,,--")_\
   ||         |_|   ccc/
   ||        ccc/
   ||

First Question: What is the ASCII plaintext corresponding to this binary string?
010110100110010101110010011011110111001100100000001001100010000001001111011011100110010101110011

pt = Zeros & Ones

Second Question: What is the ASCII plaintext corresponding to this hex string?
4f6820776f77777721204261736520313020697320636f6f6c20616e6420616c6c2062757420486578787878

pt = Oh wowww! Base 10 is cool and all but Hexxxx

Third Question: What is the ASCII plaintext corresponding to this octal string?
(HINT: octal -> int -> hex -> chars)
535451006154133420162312701623127154533472040334725553046256234620151334201413347444030460563312201673122016730267164

pt = We can represent numbers in any base we want

Fourth Question: What is the ACII representation of this integer?
(HINT: int -> hex -> chars)
8889185069805239596091046045687553579520816794635237831028832039457

pt = This is one big 'ol integer!

Fifth Question: What is the ASCII plaintext of this Base64 string?
QmFzZXMgb24gYmFzZXMgb24gYmFzZXMgb24gYmFzZXMgOik=

pt = Bases on bases on bases on bases :)

Last Question: What is the Big-Endian representation of this Little-Endian hex string?
293a2065636e657265666669642065687420776f6e6b206f7420646f6f672073277449

plaintext (Big-Endian) = It's good to know the difference :)

Very well, my friend. Here is your reward for your witts: flag{c2ed35aba037cd93381b298caa2720ee}
```