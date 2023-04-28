from math import factorial 
def nCr(n, r): 
	if r > n: 
		return 0 
	else: 
		return factorial(n)//factorial(r)//factorial(n-r)
n, k, m = map(int, input().split()) 
ans = 1 
while n > 0: 
	ans = ans*nCr(n % m, k % m) % m
	n //= m 
	k //= m 
print(ans) 
