import requests

link = "https://lkl.lt/zaidejai"
row = "<tr>"
endRow = "</tr>"
beforeBirthDate = '<td class="hidden-xs" valign="middle">'
playerName = "player-title"

def isLithuanian(item):
    if item.find("LTU") != -1:
        return True
    
    print(item[item.find(playerName) + len(playerName):item.find(playerName)+50])
    print("Is lithuanian?")
    x = input()
    if x[0] == 'y':
        return True
    
    return False

r = requests.get(link).text

r = r[r.find(endRow)+1:]

blocks = []
p = r.find(row)
while p != -1:
    blocks.append(r[r.find(row) + len(row):r.find(endRow)])
    r = r[r.find(endRow) + 1:]
    p = r.find(row)

print(f'{len(blocks)} players')

f = open("lkl.txt", "w")
for player in blocks:
    if not isLithuanian(player):
        continue
    
    bDay = player[player.find(beforeBirthDate) + len(beforeBirthDate):].strip()[:10]
    f.write(bDay + '\n')
f.close()