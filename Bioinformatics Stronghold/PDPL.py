
from collections import Counter
input_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\input.INP"
output_path  = r"C:\Users\admin\College\College\Coding\Bioinformatics Learning\ROSALIND\Bioinformatics Stronghold\output.OUT"
f1 = open(input_path, 'r')
f2 = open(output_path,'w')

def quad_math(a,b,c):
    if (a == 0):
        return -1
    dis = b**2 - 4*a*c
    sol1 = (-b + dis**(1/2))//(2*a)
    sol2 = (-b - dis**(1/2))//(2*a)
    return max(sol1,sol2)


a = list(map(int, f1.readline().split()))
a = sorted(a)
vis = Counter(a)

n = len(a)
#m = int(quad_math(1,-1,-2*n))
max_num = a[-1]
sol_set = [0, max_num]
del vis[max_num]


 
def gen(point, distt):
    #print(point, dist)
    if sum(distt.values()) == 0:
        point = sorted(point)
        f2.write(" ".join(map(str, point)) + "\n")
        return
    cur_dist = {k:v for k, v in distt.items() if v > 0}
    y = max(cur_dist.keys())
    points = [y, max_num - y]
    if points[0] == points[1]: points.pop()

    for pos in points:
        dist = []
        flag = True
        for x in point:
            d = abs(pos - x)
            if (d in cur_dist and cur_dist[d] > 0):
                dist.append(d)
                cur_dist[d] -=1
            else:
                flag = False
                break
        if flag:
            #print("YAY")
            point.append(pos)
            gen(point, cur_dist)
            point.pop()
        for x in dist:
            cur_dist[x] += 1

gen(sol_set, vis)

