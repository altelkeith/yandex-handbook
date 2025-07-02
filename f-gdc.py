a = int(input())
b = int(input())
nod = 0
mins = min(a, b)
maxs = max(a, b)
while mins != 0:
    prom = mins
    mins = maxs % mins
    maxs = prom
nod = max(mins, maxs)
print(nod)