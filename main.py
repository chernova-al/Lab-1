RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
BLACK = '\u001b[40m'
# Чернова Александра Сергеевна 409837 R3142
print('Задание 1:')
print(f'{WHITE}{"  " * 16}{END}')
print(f'{WHITE}{"  " * 6}{RED}{"  " * 4}{WHITE}{"  " * 6}{END}')
print(f'{WHITE}{"  " * 5}{RED}{"  " * 6}{WHITE}{"  " * 5}{END}')
print(f'{WHITE}{"  " * 5}{RED}{"  " * 6}{WHITE}{"  " * 5}{END}')
print(f'{WHITE}{"  " * 6}{RED}{"  " * 4}{WHITE}{"  " * 6}{END}')
print(f'{WHITE}{"  " * 16}{END}')

print('\n')
print('Задание 2:')
print('Введите длину узора')
n = int(input())*2
print('Введите ширину узора')
b = int(input())
for i in range(b):
    print(f'{WHITE}{"  " * 1}{END}', f'{WHITE}{"  " * 1}{BLACK}{"  " * 1}{WHITE}{"  " * 2}{END}'*n, sep='')
    print(f'{WHITE}{"  " * 1}{END}', f'{BLACK}{"  " * 1}{WHITE}{"  " * 1}{BLACK}{"  " * 1}{WHITE}{"  " * 1}{END}'*n, sep='')
    print(f'{BLACK}{"  " * 1}{END}', f'{WHITE}{"  " * 3}{BLACK}{"  " * 1}{END}'*n, sep='')
    print(f'{WHITE}{"  " * 1}{END}', f'{BLACK}{"  " * 1}{WHITE}{"  " * 1}{BLACK}{"  " * 1}{WHITE}{"  " * 1}{END}'*n, sep='')
print(f'{WHITE}{"  " * 1}{END}', f'{WHITE}{"  " * 1}{BLACK}{"  " * 1}{WHITE}{"  " * 2}{END}'*n, sep='')

print('\n')
print('Задание 3:')
plot_list = [[0 for i in range(10)] for j in range(10)]  # это будущий график
result = [0 for i in range(10)]  # значения, которые нужно будет отметить на графике, сейчас y=0

for i in range(10):
    result[i] = i * 3  # график функции y=x*3

# step = round(abs(result[0] - result[9]) / 9, 2) # это шаг по оси y, можно не высчитывать
step = 3

for i in range(10):
    for j in range(10):
        if j == 0:
            plot_list[i][j] = step * (8-i) + step  # заполняем ось y значениями (отмечаем шаг)

for i in range(9):
    for j in range(10):
        if abs(plot_list[i][0] - result[9 - j]) < step:  # если значение меньше шага на оси y
            for k in range(9):
                if 8 - k == j:
                    plot_list[i][k+1] = 1

for i in range(9):
    line = ''
    for j in range(10):
        if j == 0:
            line += '\t' + str(int(plot_list[i][j])) + '\t'  # выстраиваем ось y
        if plot_list[i][j] == 0:
            line += '--'
        if plot_list[i][j] == 1:
            line += '!!'  # ставим "точку" на графике
    print(line)
print('\t0\t1 2 3 4 5 6 7 8 9')

print('\n')
print('Задание 4:')
data = [float(x[:-1]) for x in open('sequence.txt')]
do5 = []
p5 = []
for i in data:
    if i < 0 and i > -5:
        do5.append(i)
    if i < -5:
        p5.append(i)
kdo5 = len(do5)/len(data)*100
kp5 = len(p5)/len(data)*100
print('Количество чисел до -5:')
print(f'{BLACK}{" " * int(kdo5/len(data)*100)}{WHITE}{" " * int(100-(kdo5/len(data)*100))}{END}', '\n')
print('Количество чисел после -5:')
print(f'{BLACK}{" " * int(kp5/len(data)*100)}{WHITE}{" " * int(100-(kp5/len(data)*100))}{END}', '\n')
