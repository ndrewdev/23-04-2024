#1
file1 = open(r"students.csv", 'r', encoding='utf-8').readlines()
data = []
for i in file1:
    data.append(i.strip().split(','))

name = input()
for i in data:
    if name in i[1]:
        print(f'Ты получил: {i[-1]}, за проект - {i[0]}')

#2
for i in data:
    if i[-1] == 'None':
        class_ = [int(j[-1]) for j in data if (j[-2] == i[-2] and j[-1] != 'None')]
        i[-1] = str(sum(class_)/len(class_))[:5]

file2 = open(r"students_new.csv", 'w')
for i in data:
    file2.write(';'.join(i)+'\n')
file2.close()
