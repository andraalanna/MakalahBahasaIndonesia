import string

# ======== FUNGSI MEMBACA KAMUS =========
def load_kamus(filepath):
    """
    Membaca file kamus dan menyimpannya sebagai dict:
    key = kata, value = nomor baris (1-based).
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return {
            word.strip().lower(): i + 1
            for i, word in enumerate(f)
        }

# ======== DEKRIPSI DENGAN ATBASH CIPHER =========
def atbash_decrypt(text):
    """
    Mendekripsi teks dengan Atbash cipher (symmetric cipher).
    """
    decrypted = []
    for char in text:
        if char in string.ascii_lowercase:
            index = ord('z') - (ord(char) - ord('a'))
            decrypted.append(chr(index))
        elif char in string.ascii_uppercase:
            index = ord('Z') - (ord(char) - ord('A'))
            decrypted.append(chr(index))
        else:
            decrypted.append(char)
    return ''.join(decrypted)

# ======== EVALUASI HASIL DEKRIPSI =========
def evaluate_decryption(text, kamus, max_kata=10, threshold=5):
    """
    Mengevaluasi hasil dekripsi Atbash cipher:
    - Memeriksa apakah cukup banyak kata yang cocok di kamus.
    - Mengembalikan posisi dan info kecocokan kata dalam kamus.
    """
    decrypted = atbash_decrypt(text)
    words = decrypted.lower().split()
    words_to_check = words[:max_kata]

    match_positions = []
    for i, word in enumerate(words_to_check):
        if word in kamus:
            kamus_line = kamus[word]
            match_positions.append((i + 1, word, kamus_line))  # (pos_in_text, word, line_in_kamus)

    success = len(match_positions) >= threshold
    return success, decrypted, match_positions

# ======== MAIN PROGRAM =========
if __name__ == '__main__':
    kamus = load_kamus('indonesian-words.txt')

    # Contoh ciphertext (Atbash dari "Ini adalah pesan rahasia.")
    encrypted_text = "Yvwz wvmtzm kvmqzdzy ozrmmbz, hzbz kzpzr ormfc fmgfp pvhvszirzm. yfpzm wvevolkvi, yfpzm kiltiznnvi, yvmvi-yvmvi pvhvszirzm. Hfwzs ovyrs wzir 6 gzsfm (hvqzp hnz). Wzm slyr krmwzs-krmwzs wrhgil ormfc (tzmgr-tzmgr LH)."

    # Evaluasi dekripsi Atbash
    success, result, match_positions = evaluate_decryption(
        encrypted_text,
        kamus,
        max_kata=10,
        threshold=3  # bisa disesuaikan
    )

    if success:
        print("Dekripsi valid ditemukan!")
    else:
        print("Dekripsi mungkin tidak valid, hasil dekripsi akan tetap ditampilkan.")

    print(f"\nDekripsi:\n{result}\n")
    print("Kata-kata yang cocok:")

    if match_positions:
        for pos_in_text, word, kamus_line in match_positions:
            print(f"- Kata ke-{pos_in_text} = \"{word}\" ditemukan di baris ke-{kamus_line} di kamus.")
    else:
        print('Tidak ada kata cocok ditemukan dalam batas pengecekan.')
