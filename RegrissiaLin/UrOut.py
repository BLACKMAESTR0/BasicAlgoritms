def Out(tg,b):
    answer = ''
    c = 0
    for i in range(len(tg)-1,-1,-1):
        if tg[i] != 0:
            if c == 0:
                    answer += str(tg[i])[:5] + f"x^{i+1}"
                    c+=1
            else:
                c+=1
                if tg[i] < 0:
                    answer += str(tg[i])[:5] + f"x^{i+1}"
                else:
                    answer += "+" + str(tg[i])[:5] + f"x^{i+1}"
    if b>0:
        answer += f"+{str(b)[:5]}"
    else:
        answer += f"{str(b)[:5]}"
    return answer