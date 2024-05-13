# Tabel Kebenaran (logika bolean)
# not And or xor

# NOT

print(">>>>>Logika NOT<<<<<")
x = False
y = not x
print('value dari x =', x)
print('^^^^^^^^NOT^^^^^^^')
print('value dari y =', y)

# Logika OR (Semua Bernilai True Asalkan ada true-nya)
# berlaku untuk wanita
print("<<<<<Logika OR>>>>>")
x = False
y = False
z = x or y
print(x, 'OR', y, 'Adl', z)
x = False
y = True
z = x or y
print(x, 'OR', y, 'Adl', z)
x = True
y = False
z = x or y
print(x, 'OR', y, 'Adl', z)
x = True
y = True
z = x or y
print(x, 'OR', y, 'Adl', z)

# Logika AND (Hanya Bernilai True, ketika keduanya true)
# berlaku untuk Laki-laki
print("<<<<<Logika AND>>>>>")
x = False
y = False
z = x and y
print(x, 'and', y, 'Adl', z)
x = False
y = True
z = x and y
print(x, 'and', y, 'Adl', z)
x = True
y = False
z = x and y
print(x, 'and', y, 'Adl', z)
x = True
y = True
z = x and y
print(x, 'and', y, 'Adl', z)

# Logika XOR (Jika keduanya Sama hasilnya False, sisanya bernilai True)
# 
print("<<<<<Logika XOR>>>>>")
x = False
y = False
z = x ^ y
print(x, 'XOR', y, 'Adl', z)
x = False
y = True
z = x ^ y
print(x, 'XOR', y, 'Adl', z)
x = True
y = False
z = x ^ y
print(x, 'XOR', y, 'Adl', z)
x = True
y = True
z = x ^ y
print(x, 'XOR', y, 'Adl', z)