# Perbandingan 

x = 4
y = 5

# Lebih Besar >
hasil = x > y 
print ( x, '>', y,  'adalah', hasil)

# Lebih kecil <
hasil = x < y 
print ( x, '>', y,  'adalah', hasil)

# Lebih besar sama dengan >=
hasil = x >= 2 
print ( x, '>=', 2,  'adalah', hasil)
hasil = x >= 4 
print ( x, '>=', 4,  'adalah', hasil)

# Lebih kecil sama dengan <= 
hasil = x <= 2
print ( x, '<=', 2,  'adalah', hasil)
hasil = x <= 4
print ( x, '<=', 4,  'adalah', hasil)

# Sama dengan ==
hasil = x == 7 
print ( x, '==', 7,  'adalah', hasil)

# Tidak sama dengan !=
hasil = x != 7
print ( x, '!=', 7,  'adalah', hasil)

# sama " is"
hasil = x is 5
print ( x, 'is ', 5,  'adalah', hasil)

# Tidat sama " is not" 
hasil = x is not 5
print ( x, 'is not', 5,  'adalah', hasil)

# > < >= <= == != ini adalah perbandingan literal 
# x = 4, 4 = literal (tidak memakan memory)
# x = objek (memory)

# x = 4 (bisa)
# x is 4 (tidak bisa, karena yang dibandingkan adalah literal)
# x is y (bisa, karena yang dibandingkan adalah objek)


hasil = x is y
print (x, 'is', y, 'adalah', hasil)