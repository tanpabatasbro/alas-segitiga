# mencari alas segitiga

import math

a = int(input("Masukkan tinggi segitiga : "))
b = int(input("Masukkan sisi miring segitiga : "))
c = int(math.sqrt(b**2 - a**2))

print(f"Alas segitiga = {c}")
