### Machine Learning and Deep Learning Masters - Sudhansu Kumar sir & Krish Naik sir

## Python Core

# 1.
seq = ""
for i in range (2000, 3201):
    if i%7 == 0 and i%5 != 0:
        seq += str(i)
        seq += ", "
seq = seq[:-2]
print (seq)



# 2.
first_name = input()
last_name = input()

first_name = list(first_name)
first_name.append(" ")
last_name = list(last_name)

first_name.extend(last_name)

reverse_name = ""

for i in range(len(first_name)):
    reverse_name += first_name[-i-1]

print (reverse_name)



# 3.       
import math as m
r = 12//2
print ("volume of the sphere with diameter of 12 cm is " + str(4*m.pi*r**3/3) + " cm3")
