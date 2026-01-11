import networkx as nx
import matplotlib.pyplot as plt
import random
import heapq

def dijkstra(start_node = 0, end_node = 19):
    dist = {node: 1e8 for node in G.nodes()}
    dist[start_node] = 0

    pq = [(0, start_node)]
    parents = {node: None for node in G.nodes()}
    # for n, nbrs in G.adj.items():
    while pq:
        curr_dist, curr = heapq.heappop(pq)

        if curr == end_node: break
        if curr_dist > dist[curr]: continue

        for nbr, eattr in G[curr].items(): #itera nos vizinhos do nó atual
            weight = eattr['weight']
            if(dist[nbr] > (dist[curr] + weight)):
                dist[nbr] = dist[curr] + weight
                heapq.heappush(pq, (dist[nbr], nbr))
                parents[nbr] = curr
    path = []
    curr = end_node
    while curr is not None:
        path.append(curr)
        curr = parents[curr]
    return path[::-1]

G = nx.generalized_petersen_graph(10, 2)

for u, v in G.edges():
    G[u][v]['weight'] = random.randint(1, 100)

path = dijkstra(0, 4)
node_colors = ["lightblue" for _ in range(len(G.nodes()))]
node_list = list(G.nodes())
for i in path:
    pos_i = node_list.index(i) # isso é feito pois G.nodes pode estar com o numero do nó e seu index desincronizados
    node_colors[pos_i] = "red"

pos = nx.spring_layout(G, seed=7)

nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=200)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=3)
nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")

edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels)

ax = plt.gca()
ax.margins(0.08)
plt.axis("off")
plt.tight_layout()
plt.show()