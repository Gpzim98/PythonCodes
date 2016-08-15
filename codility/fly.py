def solution(N, S):
    rows = [[] for i in range(N)]

    line_conf = ['A', 'B', 'C', 'X1', 'D', 'E', 'F', 'G', 'X2', 'H', 'J', 'K']

    rows = [line_conf[::] for i in range(N)]

    for i in S.split(' '):
        rows[int(i[0])-1][line_conf.index(i[1])] = 'Z'

    empty = 0
    tmp = 0
    for j in range(N):
        for i in rows[j]:
            tmp = 0 if i in ['Z', 'X1', 'X2'] else tmp+1 
            if tmp == 3:
                tmp = 0
                empty +=1
    return empty

print(solution(4, '1A 2F 1C'))
