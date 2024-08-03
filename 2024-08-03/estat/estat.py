f = open("estat.csv")
lines = f.readlines()
f.close()

lines.pop(0)
_94_03 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
_04_13 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
_14_23 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
_94_23 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for line in lines:
    line = line.split(',')
    if line[5] != "LT" or line[4][0] != "M":
        continue
    
    year = int(line[6])
    month = int(line[4][1:])
    count = int(line[7])
    print(f'{year} - {month}, {count}')
    if year <= 2003:
        _94_03[month - 1] += count
    elif year <= 2013:
        _04_13[month - 1] += count
    else:
        _14_23[month - 1] += count
    _94_23[month - 1] += count
    
f = open("birthrateByMonth94_03.txt", 'w')
for count in _94_03:
    f.write(f'{count}, ')
f.close()

f = open("birthrateByMonth04_13.txt", 'w')
for count in _04_13:
    f.write(f'{count}, ')
f.close()

f = open("birthrateByMonth14_23.txt", 'w')
for count in _14_23:
    f.write(f'{count}, ')
f.close()

f = open("birthrateByMonth94_23.txt", 'w')
for count in _94_23:
    f.write(f'{count}, ')
f.close()
     