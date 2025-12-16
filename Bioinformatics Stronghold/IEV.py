a = list(map (int, input().split()))    
b = [1, 1, 1, .75, .5, 0]
sum = 0
for i in range (0,6):
    sum += 2*a[i]*b[i]
print(sum)
