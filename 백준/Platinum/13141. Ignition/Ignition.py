INF = 1e9


def burn_graph(vertex_num, adj, dist):
    shortest_time = INF

    for start in range(1, vertex_num + 1):
        longest_time = 0

        for from_vertex in range(1, vertex_num + 1):
            for to_vertex in range(1, vertex_num + 1):
                edge_len = adj[from_vertex][to_vertex]

                if edge_len != -1:
                    remain_len = edge_len - (dist[start][to_vertex] - dist[start][from_vertex])

                    if remain_len > 0:
                        spent_time = (remain_len / 2) + dist[start][to_vertex]
                        longest_time = max(spent_time, longest_time)

        shortest_time = min(longest_time, shortest_time)

    return shortest_time


def floyd(vertex_num, dist):
    for k in range(1, vertex_num + 1):
        for i in range(1, vertex_num + 1):
            for j in range(1, vertex_num + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


vertex_num, edge_num = map(int, input().split())

adj = [[-1] * (vertex_num + 1) for _ in range(vertex_num + 1)]
dist = [[INF] * (vertex_num + 1) for _ in range(vertex_num + 1)]

for i in range(1, vertex_num + 1):
    dist[i][i] = 0

for _ in range(edge_num):
    S, E, L = map(int, input().split())
    adj[S][E] = max(adj[S][E], L)
    adj[E][S] = max(adj[E][S], L)
    dist[S][E] = min(dist[S][E], L)
    dist[E][S] = min(dist[E][S], L)

floyd(vertex_num, dist)

print("{:.1f}".format(burn_graph(vertex_num, adj, dist)))

