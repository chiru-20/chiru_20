#Python3 Program for the OTP generation.

import random
string1 = ''
   
str1 = ("1","2","4","3","5","6","7","8","9","0")
str2 = ("1","2","4","3","5","6","7","8","9","0")
str3 = ("1","2","4","3","5","6","7","8","9","0")
str4 = ("1","2","4","3","5","6","7","8","9","0")
str5 = ("1","2","4","3","5","6","7","8","9","0")
str6 = ("1","2","4","3","5","6","7","8","9","0")
str7 = ("1","2","4","3","5","6","7","8","9","0")
str8 = ("1","2","4","3","5","6","7","8","9","0")

a1 = random.choice(str1)
b2 = random.choice(str2)
c1= random.choice(str3)
d1 = random.choice(str4)
e1 = random.choice(str5)
f1 = random.choice(str6)
g = random.choice(str7)
h = random.choice(str8)

string1 = a1 + b2 + c1 + d1 + e1 + f1 + g + h
print("\nYour One-Time Password is : ",end="")

print(string1)





