# import fungsi math untuk mengoperasikan matematika
import math
print("--------- Menghitung Persamaan Linear ---------")
a = float(input("Masukan Bilangan a ="))
b = float(input("Masukan Bilangan b ="))
c = float(input("Masukan Bilangan c ="))

# rumus dan kondisi
rumus = (b * b) - (4*a*c)
print("Hasil Persamaan Linear =", rumus ,"\n")
if float(rumus <= 0):
  print("x1 dan x2 bilangan tidak real \n")
elif (rumus == 0):
  print("x1 dan x2 bilangan real dan sama \n")
elif (rumus >= 0):
  print("x1 dan x2 yang berbeda")
  x1 = float((-b) + math.sqrt(rumus)) / (2*a)
  x2 = float((-b) - math.sqrt(rumus)) / (2*a)
# Menampilkan data
print("Hasil nilai x1 :", x1)
print("Hasil nilai x2 :", x2)


