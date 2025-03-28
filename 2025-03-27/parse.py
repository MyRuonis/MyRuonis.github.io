import io

f = io.open("file.csv", mode="r", encoding="utf-8")
fout = io.open("data.csv", mode="w", encoding="utf-8")
for line in f.readlines():
    deets = line.split(",", 1)
    second = deets[1].rsplit(",", 1)
    fout.write(f"{deets[0]};{second[0]};{second[1]}")

f.close()
fout.close()