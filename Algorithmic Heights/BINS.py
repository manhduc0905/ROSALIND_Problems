
input_path = input_path = r"C:\Users\admin\OneDrive - Grinnell College\Documents\College\Coding\Bioinformatics Learning\Algorithmic Heights\input.INP"
#print(input_path)
#f1 = open(input_path,'r')
f2 = open('output.OUT','w')

n = int(input())
m = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

def bs(target):
	left = 0
	right = n-1
	ans = -1
	while (left <= right):
		mid = (left + right)//2
		#print(left, mid, right)
		if (target >= a[mid]):
			left = mid + 1
			if (a[mid] == target):
				ans = mid
				break
		else:
			right = mid - 1
	return ans

for val in b:
	#print("HE")
	print(bs(val), end = " ")