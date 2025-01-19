import math

def encryption(plaintext):
        text = plaintext.replace(" ", "")
        cipherlist = [""]*6

        for i in range(0,len(text),6):
                for s in range(len(cipherlist)):
                        try:
                                cipherlist[s] += text[i:i+6][s]
                        except:
                                break

        ciphertext = "".join([i for i in cipherlist])
        return ciphertext

def decryption(ciphertext):
        rows = math.ceil(len(ciphertext) / 6)
        padding = ciphertext + " " * ((rows * 6) - len(ciphertext))
        plainlist = [""] * rows
        index = 0

        for col in range(6):
                for row in range(rows):
                        if 0 < len(padding):
                                plainlist[row] += padding[index]
                        index += 1

        plaintext = "".join([i for i in plainlist])

        return plaintext


text = "i am hurt very badly help paradise."
cipher = encryption(text)

print(f"text: {text}\nciphertext : {cipher}\n")
plaintext = decryption(cipher)
print(f"plaintext : {plaintext}")
