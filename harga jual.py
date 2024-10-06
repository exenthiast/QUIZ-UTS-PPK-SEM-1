harga_dasar_A = int(input("Masukkan harga dasar A: "))
harga_jual_A = int(input("Masukkan harga jual A: "))

harga_dasar_B = int(input("Masukkan harga dasar B: "))
harga_jual_B = int(input("Masukkan harga jual B: "))

harga_dasar_C = int(input("Masukkan harga dasar C: "))
harga_jual_C = int(input("Masukkan harga jual C: "))

keuntungan_A = harga_jual_A - harga_dasar_A
keuntungan_B = harga_jual_B - harga_dasar_B
keuntungan_C = harga_jual_C - harga_dasar_B

if keuntungan_A > keuntungan_B and keuntungan_A > keuntungan_C:
    barang_ditawarkan = "barang A"
elif keuntungan_B > keuntungan_A and keuntungan_B > keuntungan_C:
    barang_ditawarkan = "barang B"
else:
    barang_ditawarkan = "barang C"
    
print(f"Barang yang harus ditawarkan adalah {barang_ditawarkan}")