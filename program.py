import csv
from collections import Counter

with open ('height_weight.csv', newline = '') as f: 
    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(n_num)
data = Counter(new_data)
print(data)


    
