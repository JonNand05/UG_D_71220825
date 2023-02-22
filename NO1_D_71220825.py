curah = int(input("Masukan nilai curah hujan :"))
print ('Cuaca Terang/Berawan') if curah == 0 else 0
print ( 'Curah Hujan Ringan') if curah >= 0.5 and curah <=20 else 0   
print ('Curah Hujan Sedang')  if curah >= 21 and curah <=50 else 0 
print ('Curah Hujan Lebat')  if curah >= 51 and curah <= 100 else 0 
print ( 'Curah Hujan Ekstrem') if curah >100 else 0
  
