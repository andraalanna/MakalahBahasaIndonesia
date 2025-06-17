from math import gcd

#Mencari balikkan dari a (mod m)
def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

#Fungsi dekripsi affine cipher (case-sensitive)
def affine_decrypt(ciphertext, a, b, m=26):
    
    a_inv = mod_inverse(a, m)
    
    if a_inv is None: #jika tidak memiliki invers maka tidak dapat dilakukan enkripsi
        return None

    plaintext = ''
    
    for char in ciphertext:
    
        if char.isupper():
            x = ord(char) - ord('A') #melakukan pergeseran ke kiri
            p = (a_inv * (x - b)) % m
            plaintext += chr(p + ord('A'))
    
        elif char.islower():
            x = ord(char) - ord('a') #melakukan pergeseran ke kiri
            p = (a_inv * (x - b)) % m
            plaintext += chr(p + ord('a'))
    
        else:
            plaintext += char  # karakter non-huruf tetap
    
    return plaintext

# Brute-force semua kemungkinan pasangan (a, b)
def brute_force_affine(ciphertext):
    m = 26
    results = []
    for a in range(1, m):
        if gcd(a, m) == 1:
            for b in range(m):
                decrypted = affine_decrypt(ciphertext, a, b, m)
                if decrypted:
                    results.append((a, b, decrypted))
    return results

# Contoh penggunaan
ciphertext = input("Masukkan ciphertext: ")

hasil = brute_force_affine(ciphertext)

# Tampilkan semua hasil dekripsi
for a, b, text in hasil:
    print(f"[a={a}, b={b}] → {text}")
