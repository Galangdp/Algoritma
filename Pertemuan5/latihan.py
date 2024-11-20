pilihan = "y"
bilangan = 0

while pilihan.upper() == "Y" :
    bilangan = int(input("Jumlah Angka Yang Ingin Di Masukkan : "))
    karakter = input("Karakter Yang Ingin Di Masukkan : ")
    if 1 <= bilangan <= 100 :
        for i in range(1 + bilangan) :
            print(" " * (bilangan - i) + (karakter + " ") * i)
        print("=" * 60)
        
    else :
        print("Gagal")
        continue
    
    pilihan = input("Masih Mau Lagi? (y/n) : ")
    if pilihan.upper() == "N" :
        print ("Terima Kasih Sudah Menggunakan Code Ini")
        break
    elif pilihan.upper() != "Y" :
        print("Thank You")
        
    
