inputuser = input("Masukkan nama lengkap anda: ")
prodi= input ("masukan prodi anda: ")
huruf = input("masukan nilai (dalam huruf) yang anda dapat: ")

try:
     if huruf == 'A' :
          print("4.0, tbl tbl serem banget loh")
     elif huruf == 'A-':
          print("3.75, kamu keren!")
     elif huruf == 'B+':
          print("3.25, kamu keren!")
     elif huruf == 'B':
          print("3.0, wow")
     elif huruf == 'B-':
          print("2.75, kurang semangat belajar nih!!")
     elif huruf == 'C+':
          print("2.25, belajar lagi yaa")
     elif huruf == 'C':
          print("2.0, yok bisa yok")
     elif huruf == 'D':
          print("1.0, udah ada niat pindah jurusan?")
     elif huruf == 'E':
          print("0, niat kuliah ga sih???")
     else:
        0
except:
     print("Inputan nilai yang anda masukan tidak valid")


