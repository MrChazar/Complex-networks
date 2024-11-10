from wykop import WykopAPI
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import time
from pyvis.network import Network
import pandas as pd

matplotlib.use('TkAgg')


def load_graph_from_file(file):
    return nx.read_gml(f"{file}")


def display_graph_networkx(G):
    plt.figure(figsize=(15, 10))
    pos = nx.spring_layout(G, k=1.5, iterations=100)

    # Wierzchołki
    nx.draw_networkx_nodes(G, pos, node_size=[150 + v * 40 for v in dict(G.degree).values()])

    # Krawędzie
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=1.5)

    # Podpisy
    nx.draw_networkx_labels(G, pos, font_size=6, font_family='sans-serif', font_color='red')

    plt.show()


def display_graph_pyvis(G):
    net = Network(notebook=True, cdn_resources='remote')
    net.from_nx(G)
    net.show("graph.html")


def display_graph_statistics(G):
    rank = G.number_of_nodes()
    size = G.number_of_edges()
    density = nx.density(G)

    # Długość najdłuższej z najkrótszych ścieżek (średnica)
    try:
        diameter = nx.diameter(G)
    except nx.NetworkXError:
        diameter = "Graf nie jest spójny, brak średnicy"

    # Średnia długość najkrótszych ścieżek (jeśli graf jest spójny)
    try:
        avg_diameter = nx.average_shortest_path_length(G)
    except nx.NetworkXError:
        avg_diameter = "Graf nie jest spójny, brak średniej długości ścieżki"

    print(f"Wielkości charakteryzujące graf:\n"
          f"Rząd: {rank}\n"
          f"Rozmiar: {size}\n"
          f"Gęstość: {density:.4f}\n"
          f"Średnica: {diameter}\n"
          f"Średnia długość ścieżki: {avg_diameter}")
    return True


def display_vertex_statistics(G, vertex):
    # Stopień wierzchołka
    degree = G.degree(vertex)
    # Bliskość wierzchołka (closeness centrality)
    closeness = nx.closeness_centrality(G).get(vertex, "Brak danych")
    # Pośrednictwo (betweenness centrality)
    betweenness = nx.betweenness_centrality(G).get(vertex, "Brak danych")

    print(f"Wielkości charakteryzujące wierzchołek {vertex}:\n"
          f"Stopień: {degree}\n"
          f"Bliskość: {closeness:.4f}\n"
          f"Pośrednictwo: {betweenness:.4f}")


def display_edge_statistics(G, edge):
    # Pośrednictwo dla krawędzi
    betweenness = nx.edge_betweenness_centrality(G).get(edge, "Brak danych")
    # Waga krawędzi (jeśli graf ma wagi)
    weight = G.edges[edge].get('weight', "Brak wag")
    # Centralność wektora własnego (zwykle dla wierzchołków)
    eigenvector_centrality = nx.eigenvector_centrality(G).get(edge[0], "Brak danych")

    print(f"Wielkości charakteryzujące krawędź {edge}:\n"
          f"Pośrednictwo: {betweenness:.4f}\n"
          f"Waga: {weight}\n"
          f"Centralność (eigenvector): {eigenvector_centrality:.4f}")


# Main program loop
if __name__ == "__main__":
    control = True
    file = 'graph.gml'
    while control:
        action = input("Dostępne Akcje:  \n"
                       "1: Wyświetlenie wykresu za pomocą networkX\n"
                       "2: Wyświetlenie wykresu za pomocą pyvis\n"
                       "3: Wyświetlenie statystyk sieci\n"
                       "4: Wyświetlenie statystyk wierzchołka\n"
                       "5: Wyświetlenie statystyk krawędzi\n"
                       "6: Wyjdź\n"
                       "Wybór: ")

        if action == '6':
            control = False
        elif action == '1':
            g = load_graph_from_file(file=file)
            display_graph_networkx(g)
            input("Naciśnij przycisk by przejść dalej:")
        elif action == '2':
            g = load_graph_from_file(file=file)
            display_graph_pyvis(g)
            input("Naciśnij przycisk by przejść dalej:")
        elif action == '3':
            g = load_graph_from_file(file=file)
            display_graph_statistics(g)
        elif action == '4':
            g = load_graph_from_file(file=file)
            vertex = input("Podaj wierzchołek: ")
            display_vertex_statistics(g, vertex)
        elif action == '5':
            g = load_graph_from_file(file=file)
            edge = eval(input("Podaj krawędź jako krotkę (np. ('wierzchołek1', 'wierzchołek2')): "))
            display_edge_statistics(g, edge)
