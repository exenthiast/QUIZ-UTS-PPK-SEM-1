nim = int(input("Masukkan akhiran NIM: "))
kelas = input("K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8")

if 1 <= nim <= 100:
    if nim % 2 == 0:  
        kelas = "K2"
    else:  
        kelas = "K1"
elif 101 <= nim <= 200:
    if nim % 2 == 0:
        kelas = "K4"
    else:
        kelas = "K3"
elif 201 <= nim <= 300:
    if nim % 2 == 0:
        kelas = "K6"
    else:
        kelas = "K5"
else:  
    if nim % 2 == 0:
        kelas = "K8"
    else:
        kelas = "K7"

print("Mahasiswa masuk ke kelas {kelas}")
