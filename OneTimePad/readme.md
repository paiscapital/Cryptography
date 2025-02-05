# One-Time-Pad Cipher

### What is?
> Encryption technique that cannot be cracked, but requires the use of a single-use pre-shared key that is larger than or equal to the size of the message being sent. In this technique, a plaintext is paired with a random secret key.
>
![alt text](https://media.springernature.com/m685/springer-static/image/art%3A10.1038%2Fsrep03543/MediaObjects/41598_2013_Article_BFsrep03543_Fig1_HTML.jpg)

### Logic Algorithm
```
key = iloveyou
message = its good for you, good for you

keyGenerator = iloveyouiloveyouiloveyouiloveyou

^ stand for XOR

ENCRYPT
i ^ i
t ^ l
s ^ o
...

DECRYPT
cipher = \x00\x18\x1cV\x02\x16\x00\x11I\n\x00\x04E\x00\x00\x00EL\x08\x19\n\x1dO\x13\x06\x1eO\x0f\n\x0c
keyGenerator = iloveyouiloveyouiloveyouiloveyou

\x00 ^ i
\x18 ^ l
\x1c ^ o
...
```
### 

For more information, you can connect with me [@paiscapital](https://www.instagram.com/paiscapital).
