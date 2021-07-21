print('Введите строку из нескольких слов, разделенных пробелами:','\n')
string=input()
words_list=string.split(' ')
len_words_list=len(words_list)
i=0
while i<len_words_list:
    print(i+1, words_list[i][0:10])
    i+=1