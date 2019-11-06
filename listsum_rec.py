

## recurive way of list sum
def somrec(l, start = 0, end = len(l)):
    if len(l) == start:
        return 0
    else:
       return l[start] + somrec(l[start + 1:end+1])
## iterative (without recursive) list sum
def sumlist(l, start = 0, end = len(l)):
    som = 0
    for i in range(start, end + 1):
            som += l[i]
    return som
n = int(input("give the value of n:"))
l = list(range(1, n + 1))
print(somrec(l, 2, 6))
print(sumlist(l, 2, 6))
print(sumlist(l, 4, 10))
