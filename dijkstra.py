# coding=utf-8
# find shortest path(path has weight)
# can not handle "directed cyclic graph"
# only for "directed acyclic graph"
graph = dict()
graph['start'] = dict()
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = dict()
graph['a']['final'] = 1

graph['b'] = dict()
graph['b']['a'] = 3
graph['b']['final'] = 5

graph['final'] = dict()

inf = float("inf")
cost = dict()
cost['a'] = 6
cost['b'] = 2
cost['final'] = inf

parents = dict()
parents['a'] = 'start'
parents['b'] = 'start'
parents['final'] = None
processed = []


def find_lowest_cost_node(nodes):
    lowest = inf
    lowest_node = None
    for node in nodes:
        cost_ = cost[node]
        if cost_ < lowest and node not in processed:
            lowest = cost_
            lowest_node = node
    return lowest_node


def dijkstra():
    node = find_lowest_cost_node(cost)
    while node is not None:
        cost_ = cost[node]
        neighbor = graph[node]
        for n in neighbor.keys():
            new_cost = cost_ + neighbor[n]
            if cost[n] > new_cost:
                cost[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(cost)
    print(processed)


dijkstra()


