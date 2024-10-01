def kelas_mahasiswa(nim):
    nim = int(nim)

    if 1 <= nim <= 100:
        kelas_ganjil = 'K1'
        kelas_genap = 'K2'
    elif 101 <= nim <= 200:
        kelas_ganjil = 'K3'
        kelas_genap = 'K4'
    elif 201 <= nim <= 300:
        kelas_ganjil = 'K5'
        kelas_genap = 'K6'
    else:  
        kelas_ganjil = 'K7'
        kelas_genap = 'K8'

    if nim % 2 == 0:
        return f"Mahasiswa masuk ke kelas {kelas_genap}"
    else:
        return f"Mahasiswa masuk ke kelas {kelas_ganjil}"

nim = input("Masukkan akhiran NIM: ")
print(kelas_mahasiswa(nim))
