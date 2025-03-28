import io
with io.open('data.csv', mode='r', encoding='utf-8') as fileIn, io.open('out.txt', mode='w', encoding='utf-8') as fileOut:
    for line in fileIn:
        fileOut.write("<tr>\n")
        details = line.strip().split(';')
        if (len(details[0]) > 15):
            fileOut.write(f"<td>{details[0][:13]}..</td>\n")
        else:
            fileOut.write(f"<td>{details[0]}</td>\n")
        fileOut.write(f"<td>{details[1].strip()}</td>\n")
        fileOut.write(f"<td>{details[-1].strip()}</td>\n")
        fileOut.write("</tr>\n")