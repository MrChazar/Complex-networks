from wykop import WykopAPI
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import time
from collections import deque
import keyboard
from pyvis.network import Network

matplotlib.use('TkAgg')
api = WykopAPI("w55988974f3d3194b7dd98c7ab2c6765c2", "05f093e009943e9e9b911f2a8a9f1a00")
api.authenticate()


def handle_data(starting_user):
    temp = []
    iter = 1
    while True:
        max_attempts = 5
        test = []
        time.sleep(0.1)
        for i in range(max_attempts):
            try:
                time.sleep(0.05)
                test = api.make_request(f"profile/users/{starting_user}/observed/users/following?page={iter}")
                time.sleep(0.05)
                break
            except:
                print(f"Fail, attempt {i}")

        try:
            usernames = [x['username'] for x in test['data']]
        except:
            print(f"Saving fail")
            continue

        if len(usernames) <= 0:
            break
        temp += usernames
        iter += 1
    return temp


def build_graph(starting_user, max_repeats=5):
    G = nx.DiGraph()
    queue = deque()
    seen = {}  # Słownik do śledzenia, ile razy dany użytkownik został przetworzony

    # Dodaj początkowego użytkownika do kolejki
    queue.append(starting_user)
    seen[starting_user] = 1

    while queue:
        current_user = queue.popleft()
        usernames = handle_data(current_user)

        for username in usernames:
            G.add_edge(current_user, username)

            # Sprawdź, czy użytkownik nie został już przetworzony zbyt wiele razy
            if username not in seen:
                seen[username] = 1
                queue.append(username)
            else:
                seen[username] += 1
                if seen[username] <= max_repeats:
                    queue.append(username)
            if keyboard.is_pressed('k'):
                break
        if keyboard.is_pressed('k'):
            break
    return G

starting_user = 'freshmanR'
G = build_graph(starting_user, max_repeats=10)
print(G)
nx.write_gml(G, "graph.gml")