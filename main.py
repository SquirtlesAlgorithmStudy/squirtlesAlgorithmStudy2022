<<<<<<< HEAD
from collections import deque

a = [deque(), deque()]

a[0].append(1)
a[0].append(2)
while a[0] or a[1]:
    a[0].pop()
=======
# dp = [0 for _ in range(N+1)]


#카드팩 가짓수 
N = int(input())
p = list(map(int,input().split()))
P = [0] + p

#dp 생성
dp = []
for i in range(N+1):
  dp.append(i)

#최댓값 구하기 
for i in range(1,N+1):
  for j in range(1,i+1):
    dp[i] = max(dp[i], dp[i-j]+P[j])

print(dp[i])

>>>>>>> dd42fc570161282e78979d411e60df1f3141c19a
