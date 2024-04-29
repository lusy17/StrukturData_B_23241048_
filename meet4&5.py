# inputan dari user
# aritmatika 

# belajar inputan 
LY = input ("masukan kata : ")
print ("isi dari LY : ", LY, "bertype data: ", type (LY) )

#belajar aritmatika dasar
x = 3
y = 4 

# penjumlahan +
hasil = x + y
print ("x + y : ", hasil)

# pengurangan -
hasil = x - y
print ("x - y :", hasil) 

# perkalian *
hasil = x * y 
print ("x * y :", hasil) 

# pembagian /
hasil = x / y
print ("x / y :", hasil) 

#perpangkatan **/^
hasil = x ** y
print ("x ^ y :", hasil) 

# modulus %
hasil = x % y
print ("x mod y :", hasil) 

#float division (pembulatan kebawah) //
hasil = x // y
print ("x // y :", hasil)

# aritmatika prioritas 
#(), exponen,  perkalian, pembagian,  penjumlahan, pengurangan 
x = 3
y = 4
z = 5

hasil = (x ** y  * (z + x) / y - z % x // y) 
print (hasil) 