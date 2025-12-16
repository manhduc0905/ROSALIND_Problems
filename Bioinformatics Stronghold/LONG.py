f1 = open('input.INP','r')
f2 = open('output.OUT','w')

def max_(a,b):
    if a[0] < b[0]:
        return b
    return a
def merge(s1, s2):
    lens1 = len(s1)
    lens2 = len(s2)
    right = min(lens1,lens2)
    max_len = [-1, ""]
    #prefix s1 and suffix s2
    for i in range(right + 1,1, -1):
        if s1[-i:] == s2[:i]:
            max_len = max_(max_len, [i, s1 + s2[i:]])

    # suffix of s2 matches prefix of s1
    for i in range(right + 1, 1, -1):
        if s2[-i:] == s1[:i]:
            max_len = max_(max_len, [i, s2 + s1[i:]])
            break

    return max_len

key =''
edge = []
num = -1
temp = ""

for line in f1:
    if line[0] == '>':
        if temp != "":
            edge.append(temp)
        temp = ""
    else:
        temp += line.strip()
edge.append(temp)
n = len(edge)
while (n > 1):
    max_len = [-1, "", -1, -1]
    for i in range(n):
        for j in range(i+1,n):
            curr = merge(edge[i], edge[j])
            if (max_len[0] < curr[0]):
                max_len = [curr[0], curr[1], i, j]
    if (max_len[0] == -1):
        break
    i, j = max_len[2], max_len[3]
    new_seq = max_len[1]

    # delete larger index first
    if i > j:
        del edge[i]
        del edge[j]
    else:
        del edge[j]
        del edge[i]

    edge.append(new_seq)
    n = len(edge)

f2.write(edge[0])


        




          
