# matriks = ([0,0,0,0], [0,0,0,0,0], [0,0,0,0], [0,0,0,0])

# for i in range (4):
#     for j in range (4):
#         if j==j:
#             matriks[i][j] = 1
#         if i<j:
#             matriks[i][j] = 1
#         if i>j:
#             matriks[i] [j] = 0

# for i in range (4):
#     print(matriks[i])

# Soal 1
# matriks = ([0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0])

# for i in range (4):
#     for j in range (4):
#         if i==j:
#             matriks[i][j] = 1
#         if i<=j:
#             matriks[i][j] = j + 1 
#         if i>j:
#             matriks[i][j] = 0

# for i in range (4):
#     print(matriks[i])


# Soal 2
# matriks = ([0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0])

# for i in range (4):
#     for j in range (4):
#         if i==j:
#             matriks[i][j] = j + 1
#         if i<j:
#             matriks[i][j] = 0
#         if i>j:
#             matriks[i][j] = i + 1

# for i in range (4):
#     print(matriks[i])

# Soal 3
# matriks = ([0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0])

# for i in range (4):
#     for j in range (4):
#         if i==j:
#             matriks[i][j] = 19
#         if i<j:
#             matriks[i][j] = 0
#         if i>j:
#             matriks[i][j] = 0

# for i in range (4):
#     print(matriks[i])

# Kelompok
data = [
    ["Galang Davian Pradana", "10240083", "10.1A.05"],
    ["Renata Egian", "10240085", "10.1A.05"],
    ["Alifian Risqi Febriyanto", "10240022", "10.1A.05"],
    ["Nurcahya Fadhillah", "10240045", "10.1A.05"]
]

print("+----------------------------+----------+-----------+")
print("| Nama                       | NIM      | Kelas     |")
print("+----------------------------+----------+-----------+")

for row in data:
    print(f"| {row[0]:<26} | {row[1]:<8} | {row[2]:<9} |")

print("+----------------------------+----------+-----------+")

print ("Soal : \nBilangan 1: \n[5, 0, 2]\n[2, 5, 5]\n[4, 2, 2]\nBilangan 2: \n[2, 6, 4]\n[4, 2, 3]\n[8, 1, 6]")

bilangan1 = [
    [5, 0, 2],
    [2, 5, 5],
    [4, 2, 2]
    ]

bilangan2 = [
    [2, 6, 4],
    [4, 2, 3],
    [8, 1, 6]
]

hasil = [[0 for i in range(3)] for j in range (3)]

for i in range (3) :
    for j in range (3) :
        hasil[i][j] = bilangan1[i][j] + bilangan2[i][j]

print("Hasil Dari Penjumlahan Ordo 3 x 3 dari Bilangan 1 dan Bilangan 2")

for baris in hasil :
    print (baris)