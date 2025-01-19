import string

char_table = string.ascii_uppercase
shift = 23

def encryption(plaintext):
        text = plaintext.replace(" ","").upper()
        shifted = str()

        for i in text:
                if i not in char_table:
                        shifted += i
                else:
                        shifted += chr(((ord(i) - ord('A') + shift) % 26) + ord('A'))

        return shifted
def decryption(ciphertext):
        unshifted = str()
        for i in ciphertext:
                if i not in char_table:
                        unshifted += i
                else:
                        unshifted += chr(((ord(i) - ord('A') - shift) % 26) + ord('A'))
        return unshifted

text = "see you at marineford arc three x two y:("
cipher = encryption(text)
print(f"text: {text}\nciphertext : {cipher}")
plaintext = decryption(cipher)
print(f"plaintext : {plaintext}")
