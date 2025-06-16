def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted = (ord(char) - base + shift) % 26 + base
            result += chr(encrypted)
        else:
            result += char
    return result

def atbash_cipher_encrypt(text):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr(ord('Z') - (ord(char) - ord('A')))
            else:
                result += chr(ord('z') - (ord(char) - ord('a')))
        else:
            result += char
    return result

def affine_cipher_encrypt(text, a, b):
    result = ""
    
    def modinv(a, m):
        for i in range(1, m):
            if (a * i) % m == 1:
                return i
        raise ValueError("a tidak punya invers modulo dengan 26")

    if gcd(a, 26) != 1:
        raise ValueError("a harus relatif prima dengan 26.")

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted = ((a * (ord(char) - base) + b) % 26) + base
            result += chr(encrypted)
        else:
            result += char
    return result

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def encrypt_to_files(input_file, caesar_shift=3, affine_a=5, affine_b=8):
    with open(input_file, 'r', encoding='utf-8') as f:
        text = f.read()

    caesar_result = caesar_cipher_encrypt(text, caesar_shift)
    atbash_result = atbash_cipher_encrypt(text)
    affine_result = affine_cipher_encrypt(text, affine_a, affine_b)

    with open("caesar3.txt", 'w', encoding='utf-8') as f:
        f.write(caesar_result)

    with open("atbash3.txt", 'w', encoding='utf-8') as f:
        f.write(atbash_result)

    with open("affine3.txt", 'w', encoding='utf-8') as f:
        f.write(affine_result)

    print("Enkripsi selesai. Hasil disimpan ke:")
    print("  ✔ caesar.txt")
    print("  ✔ atbash.txt")
    print("  ✔ affine.txt")

# Contoh penggunaan
if __name__ == "__main__":
    encrypt_to_files("/Users/fahd/Documents/Kuliah/Bahasa Indonesia/Hasil Enkripsi/Teks3.txt")
