import matplotlib.pyplot as plt

n = 0.0001


def tickLine(tg, b, x, y):
    global n
    if y > tg * x + b:
        tg += n * x
        b += n
    else:
        tg -= n * x
        b -= n
    return (tg, b)

def LinearRegression(coord, learningRate = 0.01, epochs = 1000000):
    nachTg = 0
    nachOtkl = 0
    for i in range(epochs):
        for z in range(len(coord)):
            nachTg, nachOtkl = tickLine(nachTg, nachOtkl, coord[z][0], coord[z][1])
    return(nachTg,nachOtkl)
with open("FileToProstPodhod") as f:
    a = f.read().strip()
a = a.split("\n")
coord = [list(map(float, [a[i].split()[0], a[i].split()[1]])) for i in range(len(a))]
nachTg = 0.5
nachOtkl = 0
for i in range(1000000):
    for z in range(len(coord)):
        nachTg, nachOtkl = tickLine(nachTg, nachOtkl, coord[z][0], coord[z][1])
print(nachTg * 4 + nachOtkl)
print(f"tg = {nachTg}, b = {nachOtkl}")
print(f"Цена за комнату = {int(nachTg)}, Базовая цена дома = {int(nachOtkl)}")
plt.scatter([4], [nachTg * 4 + nachOtkl])
plt.scatter([coord[x][0] for x in range(len(coord))], [coord[x][1] for x in range(len(coord))])
plt.plot([coord[0][0], coord[-1][0]], [nachTg * coord[0][0] + nachOtkl, nachTg * coord[-1][0] + nachOtkl])
plt.show()
