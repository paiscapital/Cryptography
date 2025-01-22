table = [''.join(chr((j + i) % 26 + ord('A')) for j in range(26)) for i in range(26)]

def keyGenerator(message,key):
        key = key.upper()

        if len(message)==len(key):
                return key
        else:
                return (key * (len(message)//len(key) + 1))[:len(message)]

def encryption(plaintext,key):
        text = plaintext.upper().replace(" ","")
        key = keyGenerator(text,key)
        ciphertext = str()

        for i in range(len(text)):
                if text[i] in table[0]:
                        mindex = ord(text[i]) - ord("A")
                        kindex = ord(key[i]) - ord("A")

                        ciphertext += table[kindex][mindex]
                else:
                        ciphertext += text[i]

        return ciphertext

def decryption(ciphertext,key):
        key = keyGenerator(ciphertext,key)
        plaintext = str()

        for i in range(len(ciphertext)):
                kindex = ord(key[i]) - ord("A")
                mindex = table[kindex].find(ciphertext[i])

                plaintext += chr(mindex + ord("A"))

        return plaintext

text = "this is so cruel"
key = "cruel"
cipher = encryption(text,key)
print(f"text: {text}\nkey: {key}\nciphertext : {cipher}")
plaintext = decryption(cipher,key)
print(f"plaintext : {plaintext}")
