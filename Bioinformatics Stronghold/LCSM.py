f1 = open('input.INP','r')
f2 = open('output.OUT','w')
key =''
d = {}
count = {}
a = []
k = -1
for line in f1:
    if line[0] == '>':
        k+=1
        a.append("")
    else:
        a[k] += line.strip()

shortest_seq = min(a,key = len)
a.remove(shortest_seq)
short_len = len(shortest_seq)
left = 0
right = short_len
ans = [-1,""]
while left <= right:
    length = int((left + right)/2)
    for start in range (0, short_len - length + 1):
        substr = shortest_seq[start:start+length]
        flag = True
        for other_seq in a:
            if substr not in other_seq:
                flag = False
                break
        if flag:
            if ans[0] < length:
                ans = [length, substr]
            left = length + 1
        else:
            right = length - 1
f2.write(ans[1])
        
          
