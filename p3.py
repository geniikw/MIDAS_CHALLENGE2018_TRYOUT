import sys

def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if (not start in graph.keys()) :
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


count = int(sys.stdin.readline())
path = []
graph = {}
result = -1
for _ in range(count):
    item = list(sys.stdin.readline()[:-1].split(','))
    path.append(item)
    if(not item[0] in graph.keys()):
        graph.update({ item[0]:list(item[1])})
    else:
        graph[item[0]].append(item[1])
target = sys.stdin.readline()[:-1]

paths = find_all_paths(graph, 'A', 'Z', path=[])

paths = list(filter(lambda x : target in x, paths))

paths.sort(key = lambda x:len(x))

if(len(paths)!=0):
    result = len(paths[0])-1

print(result)


