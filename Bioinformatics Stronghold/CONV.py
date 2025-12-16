from collections import Counter
a = list(map(float, input().split()))
b = list(map(float, input().split()))

n = len(a)
m = len(b)
d = {}
for i in a:
    for j in b:
        minus = i - j
        minus = abs(round(minus,5))
        if (minus not in d):
            d[minus] = 1
        else:
            d[minus] += 1
ans = max(d, key = d.get)
print(d[ans])
print(ans)
print(Counter([round(s-t,5) for s in a for t in b]).most_common(1))