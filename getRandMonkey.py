import random


#fileIn = open('/mnt/d/Documents/OneDrive/MLIS-ZJ/2-Psy/MonkeySF/data/Student.Export.csv', mode='r')
fileIn = open('D:\Desktop\Student.Export.csv', mode='r')

lineNum = 1
selectedList = []
input = []
out = ''


for line in fileIn.readlines():
    input.append(line)


fileIn.close()


while len(selectedList) <= 100:
    r = random.randint(0,149)
    if not r in selectedList:
        selectedList.append(r)

for x in selectedList:
    out += input[x]


#fileOut = open('/mnt/d/Documents/OneDrive/MLIS-ZJ/2-Psy/MonkeySF/data/out.csv', mode='w')
fileOut = open('D:\Desktop\out.csv', mode='w')
fileOut.write(out)
fileOut.close()
