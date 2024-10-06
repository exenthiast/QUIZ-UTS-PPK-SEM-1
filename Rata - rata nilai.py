total_latihan = 1
n1 = 0
n2 = 0
target = 70

while True:
    nilai = int(input(f"Masukkan nilai latihan ke-{total_latihan} :"))
    total_latihan += 1   
    if nilai > n1:
        n2 = n1
        n1 = nilai
    elif nilai > n2:
        n2 = nilai
    if n2 > 0:
        rata_rata = float(n1 + n2)/2
        
        if rata_rata >= target:
            print("Adik Tuan Kil berhasil mencapai target dengan rata-rata", rata_rata)
            break
            