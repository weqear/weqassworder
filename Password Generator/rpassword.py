import random
import string

def connect(arg):
    ranc=""
    for char in arg:
        ranc=ranc+char
    return ranc

ranlist=[]
num=string.digits
letters=string.ascii_lowercase
up_letters=string.ascii_uppercase
punc=string.punctuation
count = int(input("Kaç tane parola oluşturulmasını istersiniz? : \n"))
max = int(input("Parola kaç haneli olmalı ? : \n"))
q_n=input("oluşturulacak parolalarda sayı bulunmalı mı? [y/n] \n").lower()
q_l=input("oluşturulacak parolalarda küçük harfler bulunmalı mı? [y/n] \n").lower()
q_ul=input("oluşturulacak parolalarda büyük harfler bulunmalı mı? [y/n] \n").lower()
q_p=input("oluşturulacak parolalarda özel karakter bulunmalı mı? [y/n] \n").lower()
if q_n=="y":
    ranlist.append(num)
if q_l=="y":
    ranlist.append(letters)
if q_ul=="y":
    ranlist.append(up_letters)
if q_p=="y":
    ranlist.append(punc)
connect(tuple(ranlist))

file=open("rpassword"+str(count)+".txt","w")

chranlist=[]

for num in range(count+1):
    for x in range(max):
        rnpass=random.choice(connect(tuple(ranlist)))
        chranlist.append(rnpass)
    random_password=connect(tuple(chranlist))
    file.write(random_password+"\n") 