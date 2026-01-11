import networkx as nx
import matplotlib.pyplot as plt
import random

def dijkstra(start_node = 0, end_node = 14):
    dist = {node: 1e8 for node in G.nodes()}
    dist[start_node] = 0

    for n, nbrs in G.adj.items():
        ordered_nbrs= list(nbrs).sort()
        print(ordered_nbrs)
        curr_dist = dist[n]
        for nbr, eattr in nbrs.items(): #itera nos vizinhos do nó atual
            if(dist[nbr] > (curr_dist + eattr['weight'])):
                dist[nbr] = curr_dist + eattr['weight']
    return best_path(dist, start_node, end_node)

def find_closest_nbr(dist, node, previous):
    curr_dist = 1e7
    curr_idx = 0
    for nbr, eattr in G[node].items():
        if(dist[nbr] < curr_dist and previous != nbr):
            curr_dist = dist[nbr]
            curr_idx = nbr
    # print(curr_idx)
    return curr_idx

def best_path(dist, start, end):
    path = []
    pnode = end
    path.append(pnode)

    while(pnode != start):
        previous = pnode
        pnode = find_closest_nbr(dist, pnode, previous)
        path.append(pnode)
    path.reverse()
    return path

G = nx.generalized_petersen_graph(10, 2)

for u, v in G.edges():
    G[u][v]['weight'] = random.randint(1, 100)

best_path = dijkstra()
print(best_path)
node_colors = ["blue" for _ in range(len(G.nodes()))]
node_list = list(G.nodes())
for i in best_path:
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