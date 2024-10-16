from AbsPodhod import LinearRegression
with open("FileToProstPodhod") as f:
    a = f.read().strip()
a = a.split("\n")
coord = [list(map(float, [a[i].split()[0], a[i].split()[1]])) for i in range(len(a))]
print(LinearRegression(coord, epochs=700000))