lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())
    for line in lines:
        line = line.split(' ')
        name = line[0][5:]
        print(name)

