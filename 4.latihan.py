
##latihan logika komparasi
# +++++3 --------------10 +++++++
inputUser = float(input("masukan angka yang bernilai\n kurang dari 3\n atau\n lebih dari besar dari 10\n:"))

# ++++++ 3 ---------------------
# memeriksa angka kurang dari 3
isKurangDari = (inputUser < 3)
print("Apakah",inputUser, "kurang dari 3 ? =",isKurangDari) 

# ----------10 +++++++++++++
isLebihDari = (inputUser > 10)
print("Apakah",inputUser, "lebih dari 10 ? =",isLebihDari)

# -------3 ++++++++++ 10 -------
isCorrect = isKurangDari or isLebihDari
print("Angka",inputUser, " =", isCorrect)
print("\n")


#irisan 

inputUser = float(input("masukan angka yang bernilai\n lebih dari sama dengan 3\n atau\n kurang dari sama dengan 10\n:"))

isKurangDari = (inputUser > 3)
print("Apakah",inputUser, "lebih dari 3 ? =",isKurangDari) 

# ----------10 +++++++++++++
isLebihDari = (inputUser < 10)
print("Apakah",inputUser, "kurang dari 10 ? =",isLebihDari)

# -------3 ++++++++++ 10 -------
isCorrect = isKurangDari and isLebihDari
print("Angka",inputUser, " =", isCorrect)
print("\n")

inputUser = float(input("masukan angka yang bernilai\n lebih dari sama dengan 3\n atau\n kurang dari sama dengan 10\n:"))
isKurleb = (inputUser >= 3 <= 10)
print("Angka", inputUser, "=", isKurleb)