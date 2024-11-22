import networkx as nx
import matplotlib.pyplot as plt
from pyvis.network import Network


def project_simple(G):
    bipartite_nodes = {n for n, d in G.nodes(data=True) if d.get('bipartite') == 0}
    P = nx.Graph()
    for node in bipartite_nodes:
        neighbors = set(G.neighbors(node))
        for neighbor in neighbors:
            for other in neighbors:
                if neighbor != other:
                    P.add_edge(neighbor, other)
    return P


def project_weighted_jaccard(G):
    bipartite_nodes = {n for n, d in G.nodes(data=True) if d.get('bipartite') == 0}
    P = nx.Graph()
    for node1 in bipartite_nodes:
        neighbors1 = set(G.neighbors(node1))
        for node2 in bipartite_nodes:
            if node1 != node2:
                neighbors2 = set(G.neighbors(node2))
                intersection = neighbors1 & neighbors2
                union = neighbors1 | neighbors2
                if intersection:
                    weight = len(intersection) / len(union)
                    P.add_edge(node1, node2, weight=weight)
    return P


def display_graph_networkx(G, title="Graph"):
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", edge_color="gray")
    nx.draw_networkx_labels(G, pos, font_size=10, font_color="black")
    edge_weights = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_weights, font_size=8)
    plt.title(title)
    plt.show()


def display_graph_networkx_normal(G, title="Graph"):
    plt.figure(figsize=(12, 8))

    nodes = {n for n, d in G.nodes(data=True) if d.get("bipartite") == 0} 
    pos = nx.bipartite_layout(G, nodes)
    nx.draw(G, pos, with_labels=True, node_size=500, node_color="lightblue", edge_color="gray")
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    G = nx.bipartite.random_graph(5, 8, 0.25, seed=42)
    while True:
        action = input("1: Wyświetlenie grafu\n2: Projekcja prosta\n3: Projekcja ważona (Jaccard)\n4: Wyjdź\nWybór:")
        if action == '1':
            display_graph_networkx_normal(G, "Graf dwudzielny")
        elif action == '2':
            P_simple = project_simple(G)
            display_graph_networkx(P_simple, "Projekcja prosta")
        elif action == '3':
            P_weighted = project_weighted_jaccard(G)
            display_graph_networkx(P_weighted, "Projekcja ważona (Jaccard)")
        elif action == '4':
            break
