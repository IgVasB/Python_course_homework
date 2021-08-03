f=open("задача 2.txt",'r', encoding='utf-8')
i=0
for line in f:
    i+=1
    print('номер строки:',i,'количество слов в строке:', len(line.split()))
f.close()