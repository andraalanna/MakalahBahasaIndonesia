import string

# ======== FUNGSI MEMBACA KAMUS =========
def load_kamus(filepath):
    """
    Membaca file kamus dan menyimpannya dalam bentuk set untuk lookup cepat.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return set(word.strip().lower() for word in f.readlines())

# ======== DEKRIPSI DENGAN CAESAR CIPHER =========
def caesar_decrypt(text, shift):
    """
    Mendekripsi teks dengan Caesar cipher berdasarkan shift tertentu.
    """
    decrypted = []
    for char in text:
        if char in string.ascii_lowercase:
            index = (ord(char) - ord('a') - shift) % 26
            decrypted.append(chr(ord('a') + index))
        elif char in string.ascii_uppercase:
            index = (ord(char) - ord('A') - shift) % 26
            decrypted.append(chr(ord('A') + index))
        else:
            decrypted.append(char)
    return ''.join(decrypted)

# ======== BRUTE FORCE DENGAN OPTIMALISASI =========
def brute_force_caesar(text, kamus, max_kata=10, early_stop_threshold=5):
    """
    Melakukan brute-force Caesar cipher:
    - Mengecek hanya max_kata pertama dari hasil dekripsi.
    - Jika minimal early_stop_threshold kata cocok, proses dihentikan (early exit).
    """
    best_match = 0
    best_shift = 0
    best_decryption = ""

    for shift in range(1, 26):
        decrypted = caesar_decrypt(text, shift)
        words = decrypted.lower().split()
        words_to_check = words[:max_kata]  # hanya cek beberapa kata pertama

        matches = sum(1 for word in words_to_check if word in kamus)

        # Early exit jika match tinggi
        if matches >= early_stop_threshold:
            return shift, decrypted

        # Simpan hasil terbaik jika belum ada yang lolos threshold
        if matches > best_match:
            best_match = matches
            best_shift = shift
            best_decryption = decrypted

    return best_shift, best_decryption

# ======== MAIN PROGRAM =========
if __name__ == '__main__':
    kamus = load_kamus('indonesian-words.txt')

    # Contoh ciphertext (ubah ini sesuai data kamu)
    encrypted_text = "Wklv lv d whvw phvvdjh hqfubswhg xvlqj d fdhvdu flskhu."

    # Brute force dengan optimisasi
    shift, result = brute_force_caesar(
        encrypted_text,
        kamus,
        max_kata=10,               # maksimal kata awal yang dicek
        early_stop_threshold=5     # kalau 5 dari 10 cocok langsung berhenti
    )

    print(f'Shift terbaik: {shift}')
    print(f'Dekripsi: {result}')
