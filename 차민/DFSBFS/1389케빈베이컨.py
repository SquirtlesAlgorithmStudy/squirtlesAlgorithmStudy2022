#입력
user_num, rel_num = map(int,input().split())

relation = []
for i in range(rel_num):
  relation.append(list(map(int,input().split())))

#그물망 만들기
relation.sort()
Net = [[]]
for i in range(user_num):
  Net.append([])

for i in range(rel_num):
  for j in range(1,user_num+1):
    if relation[i][0] == j:
      Net[j].append(relation[i][1])

relation.sort(key = lambda x:x[1])
for i in range(rel_num):
  for j in range(1,user_num+1):
    if relation[i][1] ==j:
      Net[j].append(relation[i][0])

print(Net)


#bfs
cnt = []
def bfs(arr, i, j):
  if visited[i-1]:
    return
  if j in arr[i]:
    visited[i-1]=0
    cnt.append(1)
    num = len(cnt)
    return num
  else:
      visited[i-1] = 0
      cnt.append(1)
      for k in arr[i]:
        bfs(arr,k,j)

  return 

