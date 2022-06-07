### operasi aritmatika

a = 10 
b = 3
c = 200
d = 2-5 
e = 2*3*5*2+10
# operasi tambah +
hasil = a + b + c + d + e
print(a,"+", b , "+" ,c, "+" ,d, "+" ,e , "=",hasil)

# operasi kurang -
hasil = c - a - b - d -e 
print(c,"-", a , "-" ,b, "-" ,d, "-" ,e , "=",hasil)

# operasi perkalian * 
hasil = c * a  
print(c,"x", a , "=",hasil)

# operasi pembagian /
hasil = c / a  
print(c,":", a , "=",hasil)

# operasi floor division (pembagian bulatan kebawah) //
hasil = a // b
print(a, "//", b, "=", hasil)

# operasi perpangkatan **
hasil = b ** a 
print(b,"^",a, "=" ,hasil)

#operasi modulus (a dibagi b sisanya = c, lalu a-c) %
a = 2
b = 4
hasil = a % b
print (a, "%", b, "=", hasil)

## prioritas operasi
# ()>**> * , / , % , // >+ , - #
"""
    1. ()
    2. Exponen ** (pangkat)
    3. perkalian, pembagian, modulus, dan floor division
    4. Pertambahan dan pengurangan
"""
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x + (2 * 2 * 2)
print( x , "**" , y ,"*" ,z ,"+", x , "/" , y ,"-", y ,"%", z ,"//", x , "+", "(2 x 2 x 2)"  , "=", hasil)



### Konversi satuan temperature


print("\nPROGRAM KONVERSI TEMPERATUR")
celcius = float(input('Masukan suhu dalam celcius :'))
print("suhu adalah ",celcius, "c")

# #reamur
reamur = (4/5) * celcius
print("Suhu dalam reamur : ", reamur, "R")
# #fahrenheit 
fahrenheit = ((9/5) * celcius) +32
print("Suhu dalam fahrenheit :", fahrenheit, "F")
#kelvin 
kelvin = celcius + 273
print("Suhu dalam Kelvin :", kelvin, "K")

# Suhu dari kelvin 
print("\nPROGRAM KONVERSI TEMPERATUR KELVIN")
kelvin = float(input('Masukan suhu dalam kelvin :'))
print("Suhu adalah ",kelvin, "K")
celcius = kelvin - 273
print("Suhu dalam celcius :", celcius, "c")
fahrenheit = (9/5)*(kelvin - 273) + 32
print("Suhu fahrenheit :", fahrenheit, "f")
reamur = (kelvin-273)*(4/5)
print("Suhu dalam reamur :" , reamur, "r")

