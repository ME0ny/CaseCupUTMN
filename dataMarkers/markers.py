f = open('data.txt','r',encoding='utf-8', newline='')
data = []
for i in range(54):
    data.append(open(str(i)+'.txt','w',encoding='utf-8', newline=''))

for line in f:
    try:
        string = line.split(';')
        data[int(string[2])].write(line)
    except:
        print(line)
        break

for i in range(54):
    data[i].close()