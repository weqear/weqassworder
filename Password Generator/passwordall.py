from itertools import product
import string

max_length = int(input("Kaç karakterli şifre oluşmasını istersin? : \n"))

count = 0

character = string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation

file = open("passwords"+str(max_length)+".txt","w")

for i in range(max_length+1):
    for x in product(character,repeat=i):
        password="".join(x)
        file.write(password+"\n")
        count+=1

print("Dosya başarıyla oluşturuldu")

print(f"{max_length} karakterli {count} şifre oluşturuldu")