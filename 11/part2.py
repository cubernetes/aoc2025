lines = open(0).read().splitlines()
import json

paths = {}
for line in lines:
    line = line.replace(":", "")
    device, *outputs = line.split()
    paths[device] = outputs

def dfs(device, path, goal):
    global paths

    if device == goal:
        return 1

    t = 0
    if device in paths: # 'out' is not in paths
        for output in paths[device]:
            if output in memo:
                r = memo[output]
            else:
                r = dfs(output, path + [output], goal)
            t += r
        memo[device] = t
    return t

memo = {}
print('svr -> fft', a:=dfs('svr', ['svr'], 'fft'))
memo = {}
print('svr -> dac', b:=dfs('svr', ['svr'], 'dac'))

memo = {}
print('fft -> dac', c:=dfs('fft', ['fft'], 'dac'))
memo = {}
print('dac -> fft', d:=dfs('dac', ['dac'], 'fft'))

memo = {}
print('fft -> out', e:=dfs('fft', ['fft'], 'out'))
memo = {}
print('dac -> out', f:=dfs('dac', ['dac'], 'out'))
print(a*c*f + b*d*e)
