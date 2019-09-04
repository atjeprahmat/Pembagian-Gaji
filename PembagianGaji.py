#ATJEP RAHMAT

print("Menghitung Penghasilan Budi  oleh @atjeprahmat")
print("*"*40)

gaji_per_jam = float(input("Gaji Perjam yang diinginkan : "))
jumlah_jam = float(input("Jumlah jam kerja selama seminggu : "))

gaji_bersih = gaji_per_jam * jumlah_jam
pajak = gaji_bersih-(gaji_bersih*0.14)
baju_aksesoris = (gaji_bersih-(gaji_bersih*0.14)-(pajak*10/100))
alat_tulis = (baju_aksesoris - (baju_aksesoris*0.01))
sedekah = (alat_tulis - (alat_tulis*0.25))
yatim = (sedekah*0.30)
dhuafa = (sedekah*0.70)

print("-"*20)
print("# Gaji yang diterima:", gaji_bersih)
print("-"*20)
print("# Gaji setelah bayar pajak:", pajak)
print("-"*20)
print("# Gaji setelah beli baju dan aksesoris:", baju_aksesoris)
print("-"*20)
print("# Gaji setelah beli ATK:", alat_tulis)
print("-"*20)
print("# Gaji setelah sedekah:", sedekah)
print("-"*20)
print("# Gaji setelah yatim:", yatim)
print("-"*20)
print("# Gaji setelah dhuafa:", dhuafa)

print("*"*40)