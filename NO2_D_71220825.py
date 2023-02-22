inputuser = input("Masukkan plat nomor: ")

try:
     jenis = int(inputuser)
     if jenis >=0 and jenis <=3000:
          print("mobil")
     elif jenis >3000 and jenis <= 4000:
          print("motor")
     elif jenis >4000 and jenis <= 5000:
         print("angkutan umum")
     else:
        0
except:
     print("plat nomer tidak terindikasi, setelah kode daerah harus berupa nomer kendaraan")