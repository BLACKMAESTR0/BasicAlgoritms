import Deigstra
graph = {"Книга":{"Пластинка":5,"Постер":0},"Пластинка":{"Постер":-7},"Постер":{"Барабан":35},"Барабан":{}}
parents = {x:"name" for x in graph}
costs = {x:float("inf") for x in graph}
costs["Книга"] = 0

Deigstra.RecDeigsrta(graph,costs,parents,"Книга","Барабан")
Deigstra.Out(graph,costs,parents,"Книга","Барабан")