# mendeklarasikan variabel serta memberikan fungsi inputan dan tipe data yang di berikan
Detik = int(input("Masukan detik :"))

# rumus konversi
KonvJam = Detik // 3600
KonvMnt = Detik // 60
KonvDtk = Detik
Sisa = Detik % 3600

# menampilkan hasil
print ("Konversi", Detik ,"Detik Ke Jam   : ", KonvJam ,"jam")
print ("Konversi", Detik ,"Detik Ke Menit : ", KonvMnt ,"Menit")
print ("Konversi", Detik ,"Detik Ke detik : ", KonvDtk ,"detik")
print ("Konversi", Detik ,"Detik Ke sisa  : ", Sisa ,"sisa")