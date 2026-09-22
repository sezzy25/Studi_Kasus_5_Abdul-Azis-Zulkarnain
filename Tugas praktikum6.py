def hitung_biaya(jenis_kamar, lama_menginap):
    if jenis_kamar == "Standard":
        tarif = 200000
    elif jenis_kamar == "Deluxe":
        tarif = 350000

    total = tarif * lama_menginap
    return total

jenis_kamar = input("Masukkan jenis kamar (Standard/Deluxe): ")
check_in = input("Masukkan tanggal check-in: ")
check_out = input("Masukkan tanggal check-out: ")
lama_menginap = int(input("Masukkan lama menginap(malam): "))

total = hitung_biaya(jenis_kamar, lama_menginap)

print("DATA PEMESANAN KAMAR HOTEL")
print("Jenis kamar:", jenis_kamar)
print("Check-in:", check_in)
print("Check-out:", check_out)
print("Lama menginap:", lama_menginap, "malam")
print("Total biaya:", total)