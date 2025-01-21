Z408_table = {
    'A': 'Δ', 'B': '⏀', 'C': '⏂', 'D': '⏃', 'E': '⏄',
    'F': '⏅', 'G': '⏆', 'H': '⏇', 'I': '⏈', 'J': '⏉',
    'K': '⏊', 'L': '⏋', 'M': '⏌', 'N': '⏍', 'O': '⏎',
    'P': '⏏', 'Q': '⏐', 'R': '⏑', 'S': '⏒', 'T': '⏓',
    'U': '⏔', 'V': '⏕', 'W': '⏖', 'X': '⏗', 'Y': '⏘',
    'Z': '⏙', ' ': '/'
}

def mapping():
        backward_table = {v: k for k, v in Z408_table.items()}
        return {**Z408_table,**backward_table}

def encryption(plaintext):
        text = plaintext.upper()
        ciphertext = str()

        for i in text:
                try:
       Z408_table = {
    'A': 'Δ', 'B': '⏀', 'C': '⏂', 'D': '⏃', 'E': '⏄',
    'F': '⏅', 'G': '⏆', 'H': '⏇', 'I': '⏈', 'J': '⏉',
    'K': '⏊', 'L': '⏋', 'M': '⏌', 'N': '⏍', 'O': '⏎',
    'P': '⏏', 'Q': '⏐', 'R': '⏑', 'S': '⏒', 'T': '⏓',
    'U': '⏔', 'V': '⏕', 'W': '⏖', 'X': '⏗', 'Y': '⏘',
    'Z': '⏙', ' ': '/'
}

def mapping():
        backward_table = {v: k for k, v in Z408_table.items()}
        return {**Z408_table,**backward_table}

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

text = "zodiac killer 408"
cipher = encryption(text)
print(f"text: {text}\nciphertext : {cipher}")
plaintext = decryption(cipher)
print(f"plaintext : {plaintext}")
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

text = "zodiac killer 408"
cipher = encryption(text)
print(f"text: {text}\nciphertext : {cipher}")
plaintext = decryption(cipher)
print(f"plaintext : {plaintext}")
