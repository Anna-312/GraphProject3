class Graph:
    def __init__(self, n, edges):
        self.n = n
        self.matrix = [[0 for x in range(n)] for x in range(n)]
        for edge in edges:
            self.matrix[edge[0]][edge[1]] = 1
            self.matrix[edge[1]][edge[0]] = 1

    def get_n(self):
        return self.n

    def get_edges(self):
        edges = []
        for i in range(self.n):
            for j in range(i):
                if self.matrix[i][j] == 1:
                    edges.append((i, j))
        return edges

    def find_all_cycle(self, v1, edge1, edge2):  #Поиск всех циклов, проходящих через вершину и два ребра
        str_edge1 = ''.join(str(x) for x in edge1)
        str_edge2 = ''.join(str(x) for x in edge2)
        res = []
        len_res = []
        stack = [0 for x in range(self.n)]
        labels = [0 for x in range(self.n)]
        ks = 0
        stack[ks] = v1
        labels[v1] = 1
        k = 0
        j = 0
        while ks >= 0:
            flag = False
            v = stack[ks]
            for i in range(k, self.n):
                if self.matrix[v][i] == 1:
                    if i == v1:
                        str_stack = ''.join(str(x) for x in stack[:ks + 1])
                        if (str_edge1 in str_stack) and (str_edge2 in str_stack):
                            res.append(stack[:ks + 1].copy())
                            len_res.append(ks + 1)
                    elif labels[i] == 0:
                        flag = True
                        j = i
                        break
            if flag:
                ks += 1
                stack[ks] = j
                k = 0
                labels[j] = 1
            else:
                k = v + 1
                labels[v] = 0
                ks -= 1
        return (len_res, res)

    def find_shortest_cycle(self, v1, edge1, edge2):
        len_res, list_res = self.find_all_cycle(v1, edge1, edge2)
        min_len = min(len_res)
        min_cycle = list_res[len_res.index(min_len)]
        return min_cycle

