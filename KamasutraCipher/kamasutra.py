keypair_table = {
        "A":"N",
        "B":"O",
        "C":"P",
        "D":"Q",
        "E":"R",
        "F":"S",
        "G":"T",
        "H":"U",
        "I":"V",
        "J":"W",
        "K":"X",
        "L":"Y",
        "M":"Z"
}

def mapping():
        backward_pair = {v: k for k, v in keypair_table.items()}
        return {**keypair_table, **backward_pair}

def encryption(plaintext):                                                                                        
        text = plaintext.upper().replace(" ","")
        ciphertext = str()

        for i in text:
                try:
                        ciphertext += mapping()[i]
                except:
                        ciphertext += i #Safety for character not in table

        return ciphertext

def decryption(ciphertext):
        plaintext = str()

        for i in ciphertext:
                try:
                        plaintext += mapping()[i]
                except:
                        plaintext += i

        return plaintext    
  
text = "HELLO WORLD"
cipher = encryption(text)
print(f"text: {text}\nciphertext : {cipher}")
plaintext = decryption(cipher)
print(f"plaintext : {plaintext}")
