import requests

link = "https://alyga.lt/turnyrine-lentele/1"
teamLink = "https://alyga.lt/komanda/"
playerLink = "https://alyga.lt/zaidejas/"
birthDate = "Gimimo data"
preDate = '<span class="fr">'

info = requests.get(link).text
p = info.find(teamLink)
teams = []
while p != -1:
    info = info[info.find(teamLink):]
    team = info[:info.find('"')]
    teams.append(team)
    info = info[1:]
    p = info.find(teamLink)

teams = set(teams)
players = []
for team in teams:
    info = requests.get(team).text
    p = info.find(playerLink)
    while p != -1:
        info = info[info.find(playerLink):]
        player = info[:info.find('"')]
        print(player)
        players.append(player)
        info = info[1:]
        p = info.find(playerLink)
        
players = set(players)
count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
visited = 0
for player in players:
    visited += 1
    print(visited / len(players))
    
    info = requests.get(player).text
    
    if info.find("Lietuva") == -1:
        continue
    
    info = info[info.find(birthDate):]
    info = info[info.find(preDate) + len(preDate):]
    info = info[:10]
    count[int(info[5:7]) - 1] += 1

print(count)