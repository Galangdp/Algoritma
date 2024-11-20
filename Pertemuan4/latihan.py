jumlah_jam = int(input("Masukkan Jumlah Jam : "))
harga = 6000

if jumlah_jam > 3 :
    total_harga = (jumlah_jam - 3) * 5000
elif jumlah_jam <= 3:
    total_harga = jumlah_jam*harga
else :
    total_harga = 0

print ("Total Yang Harus Di Bayar : ", total_harga)