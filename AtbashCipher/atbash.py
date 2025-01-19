char_table = {
        "A":"Z",
        "B":"Y",
        "C":"X",
        "D":"W",
        "E":"V",
        "F":"U",
        "G":"T",
        "H":"S",
        "I":"R",
        "J":"Q",
        "K":"P",
        "L":"O",
        "M":"N",
        "N":"M",
        "O":"L",
        "P":"K",
        "Q":"J",
        "R":"I",
        "S":"H",
        "T":"G",
        "U":"F",
        "V":"E",
        "W":"D",
        "X":"C",
        "Y":"B",
        "Z":"A"
}

def encryption(plaintext):
        text = [i for i in plaintext.upper().replace(" ","")]
        ciphertext = str()
        for i in text:
                try:
                        ciphertext += char_table[i]
                except:
                        ciphertext += i
        return ciphertext

def decryption(ciphertext):
        plaintext = str()
        for i in ciphertext:
                try:
                        char = {v: k for k, v in char_table.items()}
                        plaintext += char.get(i)
                except:
                        plaintext += i
        return plaintext

text = "i love you so much, but why"
cipher = encryption(text)
print(f"text: {text}\nciphertext : {cipher}\n")
plaintext = decryption(cipher)
print(f"plaintext : {plaintext}")
