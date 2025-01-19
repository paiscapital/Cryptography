sym_table = {
                "A":"ᒧ",
                "B":"⊔",
                "C":"ᒪ",
                "D":"⊐",
                "E":"☐",
                "F":"⊏",
                "G":"ᒣ",
                "H":"⊓",
                "I":"ᒥ",
                "J":"⟓",
                "K":"⨃",
                "L":"ᒷ",
                "M":"⪾",
                "N":"🝕",
                "O":"⪽",
                "P":"ᒬ",
                "Q":"⩀",
                "R":"⟔",
                "S":"ᐯ",
                "T":"ᐳ",
                "U":"ᐸ",
                "V":"ᐱ",
                "W":"⟇",
                "X":"ᑀ",
                "Y":"ᑅ",
                "Z":"⟑"
}

def encryption(plaintext):
        text = plaintext.replace(" ","").upper()
        ciphertext = str()

        for i in text:
                ciphertext += sym_table[i] + " "

        return ciphertext

def decryption(ciphertext):
        cipher = ciphertext.replace(" ","")
        plaintext = str()

        for i in cipher:
                sym = {v: k for k, v in sym_table.items()}
                plaintext += sym.get(i)

        return plaintext

text = "i love you moron"
cipher = encryption(text)
print(f"text: {text}\nciphertext : {cipher}")
plaintext = decryption(cipher)
print(f"plaintext : {plaintext}")
