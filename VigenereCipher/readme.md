# Vigenere Cipher

### What is?
> Method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword. Though the 'chiffre indéchiffrable' is easy to understand and implement, for three centuries it resisted all attempts to break it.
> 
![alt text](https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/FIG-VIG-Table.jpg)

### Logic Algorithm
```
message = this is so cruel
key = cruel
table = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'BCDEFGHIJKLMNOPQRSTUVWXYZA', 'CDEFGHIJKLMNOPQRSTUVWXYZAB', 'DEFGHIJKLMNOPQRSTUVWXYZABC', 'EFGHIJKLMNOPQRSTUVWXYZABCD', 'FGHIJKLMNOPQRSTUVWXYZABCDE', 'GHIJKLMNOPQRSTUVWXYZABCDEF', 'HIJKLMNOPQRSTUVWXYZABCDEFG', 'IJKLMNOPQRSTUVWXYZABCDEFGH', 'JKLMNOPQRSTUVWXYZABCDEFGHI', 'KLMNOPQRSTUVWXYZABCDEFGHIJ', 'LMNOPQRSTUVWXYZABCDEFGHIJK', 'MNOPQRSTUVWXYZABCDEFGHIJKL', 'NOPQRSTUVWXYZABCDEFGHIJKLM', 'OPQRSTUVWXYZABCDEFGHIJKLMN', 'PQRSTUVWXYZABCDEFGHIJKLMNO', 'QRSTUVWXYZABCDEFGHIJKLMNOP', 'RSTUVWXYZABCDEFGHIJKLMNOPQ', 'STUVWXYZABCDEFGHIJKLMNOPQR', 'TUVWXYZABCDEFGHIJKLMNOPQRS', 'UVWXYZABCDEFGHIJKLMNOPQRST', 'VWXYZABCDEFGHIJKLMNOPQRSTU', 'WXYZABCDEFGHIJKLMNOPQRSTUV', 'XYZABCDEFGHIJKLMNOPQRSTUVW', 'YZABCDEFGHIJKLMNOPQRSTUVWX', 'ZABCDEFGHIJKLMNOPQRSTUVWXY']

- ENCRYPTION
1. Generate key with message length
message = thisissocruel
key = cruelcruelcru

2. get column and row in the alphabet table for vigenere
chr(T) = 84 - 65 = 19# message/column
chr(C) = 67 - 64 = 2# Key/row
table[2][19] = V

- DECRYPTION
1. Generate key with message length
ciphertext = VYCWTUJIGCWVF
key = cruelcruelcru

2. get column and row in the alphabet table for vigenere
chr(C) = 67 - 64 = 2# Key/row
from that row, find the chr(V) index in the column
chr(V) index + 65 = 84 = T


```
### 

For more information, you can connect with me [@paiscapital](https://www.instagram.com/paiscapital).
