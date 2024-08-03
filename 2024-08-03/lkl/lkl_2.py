f = open("lkl.txt", 'r')
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for line in f.readlines():
    count[int(line[5:7]) - 1] += 1
    
print(count)