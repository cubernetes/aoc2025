lines = open(0).read().splitlines()

paths = {}
for line in lines:
    line = line.replace(":", "")
    device, *outputs = line.split()
    paths[device] = outputs

all_paths = []
def dfs(node, path):
    global paths

    if node == 'out':
        all_paths.append(path)
        return

    for a in paths[node]:
        dfs(a, path + [a])

dfs('you', ['you'])
print(all_paths)
print(len(all_paths))
