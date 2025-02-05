def keyGenerator(key,message):
        key = key

        if len(message)==len(key):
                return key
        else:
                return (key * (len(message)//len(key) + 1))[:len(message)]

def encryption(key, message):

        plaintext = bytes([p ^ k for p, k in zip(message.encode("utf-8"), key.encode("utf-8"))])

        return plaintext

def decryption(key, ciphertext):
        ciphertext = bytes([c ^ k for c, k in zip(ciphertext, key.encode("utf-8"))])

        return ciphertext

text = "its good for you, good for you"
key = keyGenerator("iloveyou",text)
cipher = encryption(key,text)
print(f"text: {text}\nciphertext : {cipher}")
plaintext = decryption(key, cipher)
print(f"plaintext : {plaintext}")
