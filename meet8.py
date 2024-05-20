# perbandingan lanjutan

# +++++3 10+++++
MasukanUser = float(input("masukkan bilangan \nkurang dari 3 atau \nlebih dari 10 :"))

# cek kurang dari 3
kurdar = (MasukanUser < 3)
print ( "Kurang dari 3 =", kurdar)

# cek lebih dari 10
lebDar = (MasukanUser > 10)
print ( "lebih dari 10 =", lebDar)

# Betul
betul = kurdar or lebDar
print ("pengecekan final :", betul)

# ------4++++++14-----
MasukanUser = float(input("masukkan bilangan antara 4 dan 14 :"))
kurdar = (MasukanUser < 14)
print ( "Kurang dari 14 =", kurdar)

# cek lebih dari 10
lebDar = (MasukanUser > 4)
print ( "lebih dari 4 =", lebDar)

# Betul
betul = kurdar or lebDar
print ("pengecekan final :", betul)
hasil = (4 < MasukanUser < 14)
print (hasil)

# -------5++++++++9------12+++++++30------- pr