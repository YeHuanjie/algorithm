# coding=utf-8
# bfs=breadth first search
# find shortest path(path has no weight)
from collections import deque

graph = dict()
graph['i'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy']
graph['alice'] = ['peggy']
graph['claire'] = ['thom', 'jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []


def judge_seller(name):
    # assume the seller's name ended with "m"
    return name[-1] == 'm'


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if judge_seller(person):
                searched.append(person)
                print(person, "is a seller")
                return True
            else:
                searched.append(person)
                search_queue += graph[person]
    print("no seller")
    return False


search('i')
