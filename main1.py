RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
B = '\u001b[40m'
W = WHITE
E = END
BLUE = '\u001b[44m'
ERASE = '\x1B[2K' # erase the line
BEGIN = '\x1B[1G' # return to column 1



# 1 задание
def flag():
    length = 35
    height = length
    cross_width = length // 5  # Ширина перекладин креста
    edge = length // 5  # Отступ от краев
    cross_vertical_start = (length - cross_width) // 2  
    cross_horizontal_start = (length - cross_width) // 2 
    
    for i in range(height):
        if i == 0 or i == height - 1:
            print(f'{RED}{"  " * length}{END}')
        else:
            line = ""
            for j in range(length):
                # Крест - вертикальная и горизонтальная перекладины (укороченные)
                if ((i >= cross_vertical_start and i < cross_vertical_start + cross_width) and 
                      (j >= edge and j < length - edge)) or \
                     ((j >= cross_horizontal_start and j < cross_horizontal_start + cross_width) and 
                      (i >= edge and i < length - edge)):
                    line += f'{WHITE}  {END}'
                # Красный фон
                else:
                    line += f'{RED}  {END}'
            print(line)


flag()



# задание 2
h, w = 13, 60
R = w // 8
r = R - 1
edge = 24


def circle_left(x, y):
    return r**2 <= (x - edge)**2 + (y - (h//2))**2 <= R**2


def circle_right(x, y):
    return r**2 <= (x - (w - edge))**2 + (y - (h//2))**2 <= R**2


while True:
    for y in range(h):
        for x in range(w):
            if circle_left(x, y):
                print(f"{B}  {E}", end="")
            elif circle_right(x, y):
                print(f"{B}  {E}", end="")
            else:
                print(f"{W}  {E}", end="")
        print()


# задание 3
h, w = 15, 60
RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
BLACK = '\u001b[40m'
BLUE = '\u001b[44m'

for y in range(h, -1, -1):
        for x in range(w + 1):
            if x / 3 == y:
                print(f"{RED} {END}", end="")
            elif x == y: # для наглядности оставляю рядом график функции у = х, чтобы сделать акцент на наклоне прямой y = x/3
                print(f"{BLACK} {END}", end="")
            else:
                print(f"{WHITE} {END}", end="")
        print()



# 4 задание
a = [float(x) for x in open('sequence.txt', 'r')]

persentage = sum(-3 <= int(x) <= 3 for x in a)
print(f'{persentage*100/len(a)}% - {BLUE}{" "*persentage}{END}\n{100-(persentage*100/len(a))}% - {WHITE}{" " * (len(a)-persentage)}{END}')
