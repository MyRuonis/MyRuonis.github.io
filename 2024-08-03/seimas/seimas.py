import requests

link = "https://www.lrs.lt/sip/portal.show?p_r=35299&p_k=1"
lookingFor = "https://www.lrs.lt/sip/portal.show"
asmId = "p_asm_id="
birthDay = "Gimimo data"
noData = '<div class="sn_vidines_vidine" id="sn_vidines_biografija" style="display: block;">Duomenų nėra</div>'

session = requests.Session()
info = session.get(link).text

p = info.find(lookingFor)
people = []
while p != -1:
    info = info[info.find(lookingFor):]
    person = info[:info.find('"')]
    if person.find(asmId) != -1:
        people.append(person.replace("&amp;", "&"))
    info = info[1:]
    p = info.find(lookingFor)

people = set(people)
count = {}
visited = 0
for person in people:
    visited += 1
    print(visited / len(people))
    print(person)
    
    info = session.get(person).text
    if info.find(noData) != -1:
        continue
    info = info[info.find(birthDay):]
    info = info[info.find("m. ") + 3:]
    info = info[:info.find(" ")]
    print(info)
    if info in count:
        count[info] += 1
    else:
        count[info] = 1

print(count)