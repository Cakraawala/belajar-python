#1 ----- 0 +++++++ 5 -------- 8 ++++++ 11 ------

inputUser = float(input("masukan angka yang bernilai\n lebih dari sama dengan 0 sampai 5\n dan \n lebih dari sama dengan 8 sampai 11\n:"))

iskosonglima = (inputUser >= 0 <=5)
print("Apakah",inputUser, "lebih dari 0 sampai 5 =",iskosonglima) 

islapansebelas = (inputUser >= 8 <= 11)
print("Apakah",inputUser, "lebih dari 8 sampai 5 =",islapansebelas)

isCorrect = iskosonglima or islapansebelas
print("Angka",inputUser, " =", isCorrect)
print("\n")

#2 +++++ 0 ------- 5 ++++++++ 8 ------ 11 ++++++

inputUser = float(input("masukan angka yang bernilai\n kurang dari sama dengan 0\n lebih dari sama dengan 5 sampai 8\n dan lebih dari sama dengan 11 :\n"))

iskosong = (inputUser <= 0)
print("Apakah",inputUser, "kurang dari 0 =",iskosong) 

islimalapan = (inputUser >= 5 <= 8)
print("Apakah",inputUser, "lebih dari 5 sampai 8 =",islimalapan)

issebelas = (inputUser >= 11)
print("Apakah", inputUser, "Lebih dari samadengan sebelas", issebelas)

isCorrect = iskosong or islapansebelas or issebelas
print("Angka",inputUser, " apakah benar =", isCorrect)