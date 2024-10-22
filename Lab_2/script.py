from wykop import WykopAPI
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import time
from pyvis.network import Network
matplotlib.use('TkAgg')


def load_graph_from_file(file):
    return nx.read_gml(f"{file}")


def display_graph_networkx(G):
    plt.figure(figsize=(15, 10))
    pos = nx.spring_layout(G, k=1, iterations=50)

    # wierzchołki
    nx.draw_networkx_nodes(G, pos, node_size=[150 + v * 40 for v in dict(G.degree).values()])

    # krawędzie
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=1.5)

    # podpisy
    nx.draw_networkx_labels(G, pos, font_size=6, font_family='sans-serif', font_color='red')

    plt.show()


def display_graph_pyvis(G):
    net = Network(notebook=True, cdn_resources='remote')
    net.from_nx(G)
    net.show("graph.html")


def display_incidence_matrix(G):
    incidence_matrix = nx.incidence_matrix(G).todense()
    print("Macierz incydencji:")
    print(incidence_matrix)


def display_adjacency_matrix(G):
    adjacency_matrix = nx.adjacency_matrix(G).todense()
    print("Macierz sąsiedztwa:")
    print(adjacency_matrix)


# Main program loop
if __name__ == "__main__":
    control = True
    file = 'graph.gml'
    while control:
        action = input("Dostępne Akcje:  \n"
                       "1: Wyświetlenie wykresu za pomocą networkX\n"
                       "2: Wyświetlenie wykresu za pomocą pyviz\n"
                       "3: Wyświetl macierz incydencji\n"
                       "4: Wyświetl macierz sąsiedztwa\n"
                       "5: Wyjdź\n"
                       "Wybór:")

        if action == '5':
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
            display_incidence_matrix(g)
            input("Naciśnij przycisk by przejść dalej:")
        elif action == '4':
            g = load_graph_from_file(file=file)
            display_adjacency_matrix(g)
            input("Naciśnij przycisk by przejść dalej:")
