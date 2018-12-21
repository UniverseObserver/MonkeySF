def recAns():
    ans = []
    for i in range (1,6):
        ans.append(str(input('Your answer for question ' + str(i) + ' is: ')))
    out = ''
    for x in ans:
        out += x + ','
    fileOut = open('/mnt/d/Desktop/t480s.csv', mode='a')
    out += '\n'
    fileOut.write(out)
    fileOut.close()
    print()
    print()


while True: 
    recAns()

