f1 = open("input.INP", "r")
f2 = open("output.OUT", "w")
n = int(f1.readline().strip())
a = list(map(int,f1.readline().strip().split()))
k = int(f1.readline().strip())

def select(x, k, a):
    left = []
    mid = []
    right = []
    for i in range(len(a)):
        if (a[i] < x): left.append(a[i])
        elif (a[i] == x): mid.append(a[i])
        else: right.append(a[i])
    l1 = len(left)
    m1 = len(mid)
    r1 = len(right)
    #print(left,mid,right)
    if (l1 >= k):
        return select(left[0], k, left)
    elif (l1 < k <= l1 + m1):
        return mid[0]
    else:
        return select(right[0], k - l1 - m1, right)
ans = select(a[0], k, a)
f2.write(f"{ans}")