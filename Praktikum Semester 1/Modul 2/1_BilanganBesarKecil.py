bil1 = int(input("Masukan Bilangan Pertama :"))
bil2 = int(input("Masukan Bilangan Kedua   :"))
bil3 = int(input("Masukan Bilangan Ketiga  :"))

if (bil1 > bil2 > bil3):
  print("Bilangan Terbesar Adalah =", bil1)
elif(bil2 > bil3 > bil1):
  print("Bilangan Terbesar Adalah =", bil2)
elif(bil3 > bil1 > bil2):
  print("Bilangan Terbesar Adalah =", bil3)

if (bil1 < bil2) and (bil1 < bil3):
  print("Bilangan Terkecil Adalah =", bil1)
elif(bil2 < bil1) and (bil2< bil3):
  print("Bilangan Terkecil Adalah =", bil2)
elif(bil3 < bil1) and (bil3 < bil2):
  print("Bilangan Terkecil Adalah =", bil3)