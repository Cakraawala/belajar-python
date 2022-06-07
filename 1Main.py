import time
start_time = time.time()

a = 230/2
b = 8+(a*23 + (4))
c = 132
d = "cm"

print(a * c / b * (a+b) , d) 

print(time.time() - start_time, "s")

#python ke bytecode (compile)
#mencompile python : py -m py_compile (namafile).py
#jika file asli mengalami update, file compile harus di compile ulang


### type data -----------------#
data_integer = 1
# print(type(data_integer))
print("data :", data_integer, "type data :", type(data_integer))

# tipe data float (koma)
data_float = 3.14159265358979
print("phi : ", data_float)

# tipe data string (karakter)
data_string = "besok libur"
print("info :", data_string)

#tipe data biner (boolean)
data_bool = False or True
print("status :", data_bool)


##tipe data khusus 

# bilangan kompleks
data_complex = complex(5,6)
print("data :", data_complex, type(data_complex))

# tipe data dari bahasa c
from ctypes import c_double 
c_double = c_double(10.5)
print('data c : ', c_double, type(c_double) )



### casting tipe data ke data lain -------------------
print("=========INT==========")
int = 9
print("data int = ", int, type(int))

float = float(int)
str = str(int)
bool = bool(int) #0 = false,1/-1+ = true
print("data float = ", float, type(float))
print("data str = ", str, type(str))
print("data bool = ", bool, type(bool))

print("=========Float==========")
float = 9.9
print("data float = ", float, type(float))

int = int(float)
str = str(float)
bool = bool(float) #0 = false,1/-1+ = true
print("data int = ", int, type(int))
print("data str = ", str, type(str))
print("data bool = ", bool, type(bool))

