from itertools import product

max_length = int(input("Kaç karakterli şifre oluşmasını istersin? : \n"))

count = 0

character = input("liste için karakterler giriniz")

file = open("passwordsnum.txt","w")

for i in range(max_length+1):
    for x in product(character,repeat=i):
        password="".join(x)
        file.write(password+"\n")
        count+=1

print("Dosya başarıyla oluşturuldu")

print(f"{max_length} karakterli {count} şifre oluşturuldu")