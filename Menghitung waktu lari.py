print("Masukkan waktu mulai!")
jam_mulai = int(input("Jam   : "))
menit_mulai = int(input("Menit : "))
detik_mulai = int(input("Detik : "))

print("Masukkan waktu selesai!")
jam_selesai = int(input("Jam   : "))
menit_selesai = int(input("Menit : "))
detik_selesai = int(input("Detik : "))

detik = detik_selesai - detik_mulai
menit = menit_selesai - menit_mulai
jam = jam_selesai - jam_mulai

if detik < 0:
    detik += 60
    menit -= 1

if menit < 0:
    menit += 60
    jam -= 1

if jam > 0:
    print(f"Tuan Riz berlari selama {jam} jam {menit} menit {detik} detik.")
else:
    print(f"Tuan Riz berlari selama {menit} menit {detik} detik.")
