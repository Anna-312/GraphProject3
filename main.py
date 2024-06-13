from graph import Graph
import matplotlib.pyplot as plt
import networkx as nx

def main():
    filename = input("Введите имя файла с графом:\n")
    with open(filename, "r") as file:
        data = file.readlines()
        n = int(data[0])
        edges = [[int(x) for x in line.split()] for line in data[1:]]
    graph = Graph(n, edges)
    v = int(input("Введите вершину:\n"))
    print("Введите ребра:")
    edge1 = (int(x) for x in input().split())
    edge2 = (int(x) for x in input().split())
    res = graph.find_shortest_cycle(v, edge1, edge2)

    #Вывод графа
    G = nx.Graph()
    nodes = [x for x in range(0, graph.get_n())]
    edges = graph.get_edges()
    G.add_nodes_from(nodes)
    pos = nx.shell_layout(G)
    cycle_edges = []
    prev_edge = res[0]
    for edge in res[1:]:
        cycle_edges.append((prev_edge, edge))
        prev_edge = edge
    cycle_edges.append((prev_edge, v))
    nx.draw(G, pos, with_labels=True, node_color='lightblue')
    nx.draw_networkx_edges(G, pos, edges, edge_color='black')
    nx.draw_networkx_edges(G, pos, cycle_edges, edge_color='lightgreen')
    plt.show()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
