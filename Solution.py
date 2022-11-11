u, v, l, C, S = [], [], [], [], []
t=0

import pandas as pd
data=pd.read_csv("input1.txt", sep=" ", header=None)

N, M, K, L, B = [int(data.loc[0,0]), int(data.loc[0,1]), int(data.loc[0,2]), int(data.loc[0,3]), int(data.loc[0,4])]
for i in range(M):
    u.append(int(data.loc[i+1,0]))
    v.append(int(data.loc[i+1,1]))
    l.append(int(data.loc[i+1,2]))
for i in range(K):
    C.append(int(data.loc[i+1+M,0]))
for i in range(int(B)):
    S.append(int(data.loc[i+1+M+K,0]))


#Time untill the end of the race#
for i in range(K-1):
    for j in range(M):
        if ((C[i]==u[j]) and (C[i+1]==v[j])) or ((C[i]==v[j]) and (C[i+1]==u[j])):
            t=t+l[j]

            
            
            
#Dijkstra Algorithm#                                           
from queue import PriorityQueue
class Graph:

    def __init__(self, num_of_vertices):
        self.v = num_of_vertices
        self.edges = [[-1 for i in range(num_of_vertices)] for j in range(num_of_vertices)]
        self.visited = []
        
    def add_edge(self, u, v, weight):
        self.edges[u][v] = weight
        self.edges[v][u] = weight
    
    def dijkstra(self, start_vertex):
        D = {v:float('inf') for v in range(self.v)}
        D[start_vertex] = 0

        pq = PriorityQueue()
        pq.put((0, start_vertex))

        while not pq.empty():
            (dist, current_vertex) = pq.get()
            self.visited.append(current_vertex)

            for neighbor in range(self.v):
                if self.edges[current_vertex][neighbor] != -1:
                    distance = self.edges[current_vertex][neighbor]
                    if neighbor not in self.visited:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.put((new_cost, neighbor))
                            D[neighbor] = new_cost
        return D

    
#Create an array with all the distances of cities of the race to the gas stations (without the first and last city)#
#Add the minimum distance of a specific city and the appropriate gas station in a list#
p=[]
w=[]
for k in range(K-2):
    g=Graph(M)
    for i in range(M):
        g.add_edge(u[i],v[i],l[i])
    d=[]
    d=g.dijkstra(C[k+1])
    for j in range(B):
        w.append(d[S[j]])
    p.append(min(w))
    w=[]



#Sort the distances and take first "L" of the sorted array#
q=sorted(p)
for i in range(L):
    t=t+q[i]
    
    
print("The minimum time of the race is", t , "seconds")