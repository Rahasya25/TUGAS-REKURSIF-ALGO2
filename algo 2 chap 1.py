# LATIHAN 1

# Meminta input jumlah menu yang dibutuhkan.
n = int(input("Masukkan jumlah menu: "))

# Menyimpan data menu dalam bentuk dictionary.
menus = {}
for _ in range(n):
    data = input("Masukkan id, parent, dan label menu: ").split()
    menu_id = int(data[0])
    parent_id = int(data[1])
    label = data[2].replace("_", " ")  # Menghapus karakter "_" dari label.
    menus[menu_id] = {'parent': parent_id, 'label': label}

# Fungsi untuk mencetak menu dengan struktur bertingkat.
def print_menu(menu_id, indent=0):
    print("." * indent + menus[menu_id]['label'])
    for key, value in menus.items():
        if value['parent'] == menu_id:
            print_menu(key, indent + 5)  # Digunkanan agar sub-menu menjorok lebih ke dalam

# Menampilkan menu yang tidak memiliki parent terlebih dahulu (menu utama).
for menu_id, value in menus.items():
    if value['parent'] == 0:
        print_menu(menu_id)

# LATIHAN 2

def ini_palindrom(teks):
    # Membersihkan teks dari spasi, koma, dan titik
    teks = teks.replace(" ", "").replace(",", "").replace(".", "").lower()
    
    # Basis rekursi: jika panjang teks 0 atau 1, pasti palindrom
    if len(teks) <= 1:
        return "Kalimat ini adalah palindrom."
    
    # Jika karakter pertama dan terakhir sama, periksa bagian tengahnya secara rekursif
    if teks[0] == teks[-1]:
        return ini_palindrom(teks[1:-1])
    
    # Jika karakter pertama dan terakhir tidak sama, bukan palindrom
    return "Kalimat ini bukanlah palindrom."

# Contoh penggunaan
print(ini_palindrom("Aku suka rajawali, bapak. Apabila wajar, aku suka."))
print (ini_palindrom("Kasur ini rusak."))
print (ini_palindrom("Kasur Nababan rusak."))
print (ini_palindrom("Kasur Koh Ahok rusak."))
print (ini_palindrom("Ibu Ratna antar ubi."))
print (ini_palindrom("Ria Irawan nawari air"))
print (ini_palindrom("Harum semar kayak rames murah."))
print (ini_palindrom("Ira hamil lima hari."))