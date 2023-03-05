n = int(input())
size = 4*n -3

graph = [[' '] * size for _ in range(size)]


def star(n,i):
    if n == 1:
        graph[i][i] = '*'
        return
    size = 4 * n -3

    for _ in range(i,i+size):
        # 위,아래
        graph[i][_] = '*'
        graph[i+size-1][_] = '*'
        # 좌,우
        graph[_][i] = '*'
        graph[_][i+size-1] = '*'
    # 재귀 
    return star(n-1,i+2)
star(n,0)

for i in range(size):
    for j in range(size):
        print(graph[i][j],end="")
    print()
