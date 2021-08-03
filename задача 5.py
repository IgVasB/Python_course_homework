f=open("задача 5.txt",'w', encoding='utf-8')
f.write("1 0 2 -1 -7")
f.close()
f=open("задача 5.txt",'r', encoding='utf-8')
s=0
data=f.read().split()
for el in data:
    s=s+float(el)
f.close()
print(s)