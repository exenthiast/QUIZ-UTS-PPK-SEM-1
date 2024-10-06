def cek_barisan_geometri(a, b, c):
    """Mengecek apakah tiga bilangan membentuk barisan geometri."""
    return (b / a) == (c / b)

def cari_suku(a, r, x):
    """Mencari suku ke-n dari barisan geometri."""
    n = 1
    while a * r**(n-1) < x:
        n += 1
    if a * r**(n-1) == x:
        return n
    else:
        return -1

bilangan1 = int(input("Masukkan bilangan pertama: "))
bilangan2 = int(input("Masukkan bilangan kedua: "))
bilangan3 = int(input("Masukkan bilangan ketiga: "))
bilangan4 = int(input("Masukkan bilangan keempat: "))

if cek_barisan_geometri(bilangan1, bilangan2, bilangan3):
    rasio = bilangan2 / bilangan1
    suku = cari_suku(bilangan1, rasio, bilangan4)
    if suku != -1:
        print(f"Bilangan {bilangan4} merupakan suku ke-{suku} dari barisan geometri.")
    else:
        print(f"Bilangan {bilangan4} bukan merupakan suku dari barisan geometri.")
else:
    print("Bukan merupakan barisan geometri.")