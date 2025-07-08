a = int(input())
b = int(input())
nok = 1
counter = 2
mins = min(a, b)
while nok % a != 0 or nok % b != 0:
    nok = mins * counter
    counter = counter + 1
print(nok)