from FuncOfOshibok import RMSE
def AmounTznakov(value):
    value = str(value)
    if '.' in value:
        return len(value.split(".")[0])
    return len(value)
def LineTickQuadr(q, xArr, y, tg, b, learningRate = 0.001):
    y2 = b
    for i in range(len(xArr)):
        y2 += tg[i] * xArr[i]
    b += learningRate * (y - y2)
    tg[q] += learningRate * xArr[q] * (y - y2)
    return (b, tg)
def LineTickAbs(q, xArr, y, tg, b, learningRate = 0.0001):
    ot = ''
    y2 = b
    for i in range(len(xArr)):
        y2 += tg[i] * xArr[i]
    ot += f"Было y = {1}"
    if y >= y2:
        tg[q] += xArr[q]*learningRate
        b += learningRate
    else:
        tg[q] -= xArr[q]*learningRate
        b-= learningRate
    return (b, tg)
def LinRegQuadr(yArr, xArr, learningRate = 0.0001, epochs = 100000):
    nachTg = [0 for _ in range(len(xArr[0]))]
    nachOtkl = 0
    funcOshibok = []
    for i in range(epochs):
        for z in range(len(xArr)):
            for q in range(len(nachTg)):
                nachOtkl, nachTg = LineTickQuadr(q, xArr[z], yArr[z], nachTg, nachOtkl)
        s = RMSE([sum([xArr[z][k] * nachTg[k] + nachOtkl for k in range(len(xArr[0]))]) for z in range(len(xArr))],
                 yArr)
        if s < 0.01*len(yArr):
            print(i, ' ---')
            break
    return (nachOtkl, nachTg)


def LinRegAbs(yArr, xArr, learningRate = 0.01, epochs = 700000):
    nachTg = [0 for _ in range(len(xArr[0]))]
    nachOtkl = 0
    funcOshibok = []
    for i in range(epochs):
        for z in range(len(xArr)):
            for q in range(len(nachTg)):
                nachOtkl, nachTg = LineTickAbs(q, xArr[z], yArr[z], nachTg, nachOtkl)
        s = RMSE([sum([xArr[z][k] * nachTg[k] + nachOtkl for k in range(len(xArr[0]))]) for z in range(len(xArr))], yArr)
        if s < 0.001*len(yArr):
            print(i, ' ---')
            break
    return (nachOtkl, nachTg)