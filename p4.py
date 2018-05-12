import sys

def allindices(string, sub, offset=0):
    listindex = []
    i = string.find(sub, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(sub, i + 1)
    return listindex


def FindKey(n, x, results = []):
    ai = allindices(n, x)
    if(len(ai)==0):
        results.append(n)

    for ii in range(len(ai)):
        idx = ai[ii]
        nn = n[:idx]+ n[idx+len(x):]
        FindKey(nn, x, results)

    return results



n = int(sys.stdin.readline()) # 100 <= n <= 999999999
x = int(sys.stdin.readline()) # 8 <= X <= 128


nb = "{0:b}".format(n)
xb = "{0:b}".format(x)

results = FindKey(nb,xb)
results.sort(key =lambda x:len(x))

print(len(results[0]))


