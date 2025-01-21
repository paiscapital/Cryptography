Z340_table = {
        'A': '⊿', 'B': '△', 'C': '▽', 'D': '○',
        'E': '●', 'F': '□', 'G': '■', 'H': '♒',
        'I': '♑', 'J': '♌', 'K': '♍', 'L': '♏',
        'M': '♋', 'N': '☉', 'O': '✶', 'P': '✡', 'Q': '✱',
        'R': '⬤', 'S': '⭘', 'T': '+', 'U': '-',
        'V': '*', 'W': '/', 'X': '▲', 'Y': '◁',
        'Z': '▷', ' ': '/'
}
def mapping():
        backward_table = {v: k for k, v in Z340_table.items()}
        return {**Z340_table,**backward_table}

def encryption(plaintext):
        text = plaintext.upper()
        ciphertext = str()

        for i in text:
                try:
                        ciphertext += mapping()[i]
                except:
                        ciphertext += i

        return ciphertext

def decryption(ciphertext):
        plaintext = str()

        for i in ciphertext:
                try:
                        plaintext += mapping()[i]
                except:
                        plaintext += i

        return plaintext

text = "zodiac killer 340"
cipher = encryption(text)
print(f"text: {text}\nciphertext : {cipher}")
plaintext = decryption(cipher)
print(f"plaintext : {plaintext}")
