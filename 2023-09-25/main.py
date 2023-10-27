import requests

link = "https://www.metasrc.com/lol/13.19/stats?ranks=master,grandmaster,challenger"
champFind = '<td class=" _byr3u7 _fs7qiw champ">'
afterRole = '</div>'
percentSeperator = '</td><td class=" _byr3u7 _dbz54g">'

SCORES = {"TOP": 0.0, "JUNGLE": 0.0, "MID": 0.0, "ADC": 0.0, "SUPPORT": 0.0}

html = requests.get(link).text
at = -1
while True:
    at = html.find(champFind, at + 1)

    if at == -1:
        break

    at = html.find(afterRole, at + 1)
    while html[at] != '>':
        at = at - 1
    at = at + 1

    role = ""
    while html[at] != '<':
        role = role + html[at]
        at = at + 1

    at = html.find(percentSeperator, at + 1)
    at = html.find(percentSeperator, at + 1)
    at += len(percentSeperator)

    wr = ""
    while html[at] != '%':
        wr += html[at]
        at += 1
    wr = float(wr)

    at = html.find(percentSeperator, at + 1)
    at = html.find(percentSeperator, at + 1)
    at += len(percentSeperator)

    pr = ""
    while html[at] != '%':
        pr += html[at]
        at += 1
    pr = float(pr)

    at = html.find(percentSeperator, at + 1)
    at += len(percentSeperator)

    br = ""
    while html[at] != '%':
        br += html[at]
        at += 1
    br = float(br)

    print(f"{role}: WR{wr}, PR{pr}, BR{br}")
    SCORES[role] += pow(wr - 50.0, 2) * pr

mx = max(SCORES.values())
for key, value in SCORES.items():
    print("{0}: {1:0.2f}".format(key, value/mx))
