import time
def Out(Start,End):
    if parents[End] == "name":
        print("No current ways")
    else:
        answer = ''
        x=End
        while x!=Start:
            answer = f" --> ({costs[x]}){x}" + answer
            x = parents[x]
        print(f"{Start}{answer}")
def RecDeigsrta(Start,End):
    for i in graph[Start]:
        if i not in processed:
            newCost = costs[Start]+graph[Start][i]
            if costs[i] > newCost:
                costs[i] = newCost
                parents[i] = Start
                processed.append(i)
                RecDeigsrta(i,End)

graph = {"start":{"A":5,"B":2},"A":{"D":2,"C":4},"B":{"D":7},"C":{"D":6,"End":3},"D":{"End":1},"End":{}}
costs = {x:float("inf") for x in graph}
costs["start"] = 0
parents = {x:"name" for x in graph}
processed = []

RecDeigsrta("start","End")
Out("start","End")
