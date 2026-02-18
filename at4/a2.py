N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * (N+1)
room = []

dp[1] = 0
dp[2] = A[0]
