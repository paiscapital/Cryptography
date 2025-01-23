import string

def polySquare(alphabet):
        square = dict()
        row, col = 1, 1

        for char in alphabet:
                square[char] = f"{row}{col}"
                col += 1
                if col > 5:
                        row += 1
                        col = 1
        return square

def mapping(poly_square):
        return {v: k for k, v in poly_square.items()}

def encryption(plaintext):
        text = plaintext.upper().replace("J","I")
        ciphertext = str()

        for i in text:
                ciphertext += square.get(i, i) + " "

        return ciphertext

def decryption(ciphertext,square):
        cipher = ciphertext.split(" ")
        plaintext = str()

        for i in cipher:
                plaintext += mapping(square).get(i,i)

        return plaintext

alphabet = string.ascii_uppercase.replace("J","I")
square = polySquare(alphabet)

text = "what is your favourite square"
cipher = encryption(text)
print(f"text: {text}\nciphertext : {cipher}")
plaintext = decryption(cipher,square)
print(f"plaintext : {plaintext}")
