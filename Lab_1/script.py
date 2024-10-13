from wykop import WykopAPI
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import time
matplotlib.use('TkAgg')


def load_related_tags_from_wykop():
    _api_key = "w55988974f3d3194b7dd98c7ab2c6765c2"
    _secret_key = "05f093e009943e9e9b911f2a8a9f1a00"
    api = WykopAPI("w55988974f3d3194b7dd98c7ab2c6765c2", "05f093e009943e9e9b911f2a8a9f1a00")
    api.authenticate()
    tag_name = "polityka"
    related = api.make_request(f"tags/{tag_name}/related")
    related["data"]
    G = nx.Graph()
    G.add_node(tag_name)
    for related_tag in related["data"]:
        time.sleep(1)
        G.add_edge(tag_name, related_tag["name"])
        second_degree_related = api.make_request(f"tags/{related_tag['name']}/related")
        for second_degree_tag in second_degree_related["data"]:
            G.add_edge(related_tag["name"], second_degree_tag["name"])

            third_degree_related = api.make_request(f"tags/{second_degree_tag['name']}/related")
            for third_degree_tag in third_degree_related["data"]:
                time.sleep(0.01)
                G.add_edge(second_degree_tag["name"], third_degree_tag["name"])
    print(len(G))
    return G


def load_graph_from_file():
    return nx.read_gml("graph.gml")


def display_graph(G):
    plt.figure(figsize=(15, 10))
    pos = nx.spring_layout(G, k=0.4, iterations=500)

    # wierzchołki
    nx.draw_networkx_nodes(G, pos, node_size=[150 + v * 40 for v in dict(G.degree).values()])

    # krawędzie
    nx.draw_networkx_edges(G, pos, edgelist=G.edges(), width=1.5)

    # podpisy
    nx.draw_networkx_labels(G, pos, font_size=6, font_family='sans-serif', font_color='red')

    plt.show()


def find_shortest_path(G):
    node1 = input("Podaj pierwszy wierzchołek: ")
    node2 = input("Podaj drugi wierzchołek: ")

    try:
        path = nx.shortest_path(G, source=node1, target=node2)
        print(f"Najkrótsza ścieżka między {node1} i {node2}: {path}")
    except nx.NetworkXNoPath:
        print(f"Brak ścieżki między {node1} i {node2}")


def is_eulerian(G):
    if nx.is_eulerian(G):
        print("Graf jest eulerowski.")
        eulerian_path = list(nx.eulerian_circuit(G))
        print("Ścieżka eulerowska:", eulerian_path)
    else:
        print("Graf nie jest eulerowski.")


def calculate_flow(G):
    node1 = input("Podaj pierwszy wierzchołek (źródło): ")
    node2 = input("Podaj drugi wierzchołek (ujście): ")

    try:
        flow_value, flow_dict = nx.maximum_flow(G, node1, node2)
        print(f"Przepływ pomiędzy {node1} i {node2}: {flow_value}")
        print(f"Przepływy w sieci: {flow_dict}")
    except nx.NetworkXError as e:
        print(f"Błąd w obliczaniu przepływu: {e}")


# Main program loop
if __name__ == "__main__":
    control = True
    while control:
        action = input("Dostępne Akcje:  \n"
                       "1: Wyświetlenie wykresu\n"
                       "2: Znalezienie najkrótszej ścieżki pomiędzy wierzchołkami\n"
                       "3: Czy eulerowski i wyznaczenie ścieżki eulerowskiej\n"
                       "4: Wyznaczenie przepływów pomiędzy wierzchołkami\n"
                       "5: Wyjdź\n"
                       "Wybór:")

        if action == '5':
            control = False
        elif action == '1':
            g = load_graph_from_file()
            display_graph(g)
            k = input("Naciśnij przycisk by przejść dalej:")
        elif action == '2':
            g = load_graph_from_file()
            find_shortest_path(g)
            k = input("Naciśnij przycisk by przejść dalej:")
        elif action == '3':
            g = load_graph_from_file()
            is_eulerian(g)
            k = input("Naciśnij przycisk by przejść dalej:")
        elif action == '4':
            g = load_graph_from_file()
            calculate_flow(g)
            k = input("Naciśnij przycisk by przejść dalej:")
