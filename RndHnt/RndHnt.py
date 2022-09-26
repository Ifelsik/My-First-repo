import random as rnd
file=open("data.txt")
data=file.readlines()
print("Элементов списка:", len(data))
rn=rnd.randint(0, len(data)-1)
print("nhentai.net/g/"+data[rn])