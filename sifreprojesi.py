import random
import string
numbers=string.digits
symbols=string.punctuation
lower_cases=string.ascii_lowercase
upper_cases=string.ascii_uppercase
all_chars = [numbers,symbols,lower_cases,upper_cases]

password=""


#for i in range(2):
#    password+=numbers[random.randint(0,9)]
#for i in range(2):
#    password+=symbols[random.randint(0,9)]
#for i in range(2):
#    password+=lower_cases[random.randint(0,9)]
#for i in range(2):
#    password+=upper_cases[random.randint(0,9)]

for i in range(4):
    for j in range(2):
        password+=all_chars[i][random.randint(0,len(all_chars[i])-1)]

    
    
#print(password)


password=list(password)
random.shuffle(password)

yeni_sifre =""
for i in password:
    yeni_sifre+=i

print(yeni_sifre)

