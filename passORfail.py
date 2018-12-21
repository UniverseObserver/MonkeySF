import csv

fileIn = open('D:\\Desktop\\x.csv', mode='r')
reader = csv.reader(fileIn, delimiter=',')
data = list(reader)

count = 0

for line in data:
    for x in line:
        if int(x) >= 3:
            count += 1
        
print(count)