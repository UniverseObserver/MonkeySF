import csv

fileIn = open('D:\\Desktop\\FS.csv', mode='r')
reader = csv.reader(fileIn, delimiter=',')
data = list(reader)

out = []

for x in data:
    
    grade = 0
    if x[0] == 'cd':
        grade += 1
    if x[1] == 'a':
        grade += 1
    if x[2] == 'c':
        grade += 1        
    if x[3] == 'bd':
        grade += 1
    if ('a' in x[4]) or ('c' in x[4]) :
        grade += 1
    out.append(grade)

#print(out)

count = 0
for o in out:
    if o >= 3:
        count += 1
    
print(count)