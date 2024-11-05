# buatlah sebuah list yang berisi bilangan bulat kurang dari 10

# bilangan_bulat = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(bilangan_bulat)

# tambahkan elemen 'Hello' di akhir list

# bilangan_bulat.append('Hello')
# print(bilangan_bulat)

# hapus elemen ke 3 dari list dan simpan elemenny

# elemen_terhapus = bilangan_bulat.pop(2)
# print(elemen_terhapus)
# print(elemen_terhapus)

# Dictionary
 
# kontak = {"Woohak": "081234", "ibu_Ihaan": "082356", "Ihaan": "089765"}

# print(kontak)
# print(type(kontak))

# # Match case

# warna_warni = input("Masukkan warna lampu")

# match warna_warni:
#     case "ungu":
#         print("Kesukaan woonhak")
#     case "kuning":
#         print("Kesukaan leehan")
        
        

# TUGAAASSS

# 1
kendaraan = ['beat karbu', 'motor', 200, 'pink', 3]
print(kendaraan)

kendaraan.append('10jt')
print(kendaraan)

kendaraan.append('matic')
print(kendaraan)

kendaraan.insert(2, 'honda')
print(kendaraan)


#2
angka_pilihan = int(input("""Masukkan Pilihan:
1. Menghitung Luas Persegi
2. Menghitung Luas Lingkaran
3. Menghitung Luas Segitiga
"""))

match angka_pilihan:
    case 1:
        print("Menghitung Luas Persegi")
        sisi = int(input("Masukkan nilai sisi: "))
        luas_persegi = sisi ** 2
        print(f"Luas Persegi dengan sisi {sisi} cm, adalah {luas_persegi} cm^2")
    case 2:
        print("menghitung luas lingkaran")
        pi = (3.14)
        jari_jari = int(input("masukkan jari-jari"))
        luas_lingkaran=pi*jari_jari*jari_jari
        print(f"luas lingkaran dengan jari_jari {jari_jari} cm, adalah {luas_lingkaran} cm^2")
    case 3:
        print("menghitung luas segitiga")
        alas = int(input("masukkan nilai alas"))
        tinggi = int(input("masukkan nilai tinggi"))
        luas_segitiga=1/2*alas*tinggi
        print("menghitung luas segitiga denga alas{alas} cm dan tinggi{tinggi}, adalah{luas_segitiga} cm^2")