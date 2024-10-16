import Deigstra
graph = {"Книга":{"Пластинка": 5, "Постер": 0},"Пластинка": {"Постер": -7}, "Постер": {"Барабан": 35}, "Барабан": {}}
parents = {x:"name" for x in graph}
costs = {x:float("inf") for x in graph}
start = "Книга"
end = "Барабан"
costs[start] = 0
def Alg(start,end):
    if start == "Пластинка":
        return
    if end == start:
        return
    for x in graph[start]:
        newCost = costs[start] + graph[start][x]
        if newCost < costs[x]:
            costs[x] = newCost
            parents[x] = start
            Alg(x,end)
Alg(start,end)
Deigstra.Out(graph,costs,parents,start,end)