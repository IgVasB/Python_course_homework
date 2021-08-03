import json

firm=dict()
profit_dict=dict()
count=0
profit_sum=0
with open("задача 7.txt",'r', encoding='utf-8') as f:
    for line in f:
        data = line.split()
        profit = float(data[2])-float(data[3])
        if profit>0:
            count+=1
            profit_sum+=profit
        firm.update({data[0]: profit})
profit_dict.update({'average_profit': profit_sum/count})
firm_list=[firm, profit_dict]

with open("firm_list.json", "w", encoding='utf-8') as write_f:
    json.dump(firm_list, write_f, ensure_ascii = False)
print(firm_list)
