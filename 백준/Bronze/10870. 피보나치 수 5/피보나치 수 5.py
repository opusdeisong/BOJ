# n번째 피보나치 수를 리턴
def fib(n):
    if n == 0:
    	return 0
    if n == 1 or n == 2:
    	return 1
    else:
    	return fib(n - 1) + fib(n-2)

N = int(input())
print(fib(N))