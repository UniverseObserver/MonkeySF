import random

monkeyListI = []
monkeyListII = []
monkeyListIII = []

while len(monkeyListI) <= 32:
    r = random.randint(0,99)
    if not r in monkeyListI:
        monkeyListI.append(r)

while len(monkeyListII) <= 32:
    r = random.randint(0,99)
    if not r in monkeyListI and not r in monkeyListII:
        monkeyListII.append(r)

while len(monkeyListIII) <= 32:
    r = random.randint(0,99)
    if not r in monkeyListI and not r in monkeyListII and not r in monkeyListIII:
        monkeyListIII.append(r)

fileIn = open('D:\Desktop\out.csv', mode='r')

input = []
for line in fileIn.readlines():
    input.append(line)

out = ''
for x in monkeyListI:
    out += input[x]
fileOut = open('D:\Desktop\m1.csv', mode='w')
fileOut.write(out)
fileOut.close()

out = ''
for x in monkeyListII:
    out += input[x]
fileOut = open('D:\Desktop\m2.csv', mode='w')
fileOut.write(out)
fileOut.close()

out = ''
for x in monkeyListIII:
    out += input[x]
fileOut = open('D:\Desktop\m3.csv', mode='w')
fileOut.write(out)
fileOut.close()