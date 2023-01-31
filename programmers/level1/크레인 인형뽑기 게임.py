from collections import deque

def solution(board,moves):
    answer = 0
    num = 0
    cage = deque()
    moves = deque(moves)
    while len(moves) >0:
        num = moves.popleft() 
        for i in range(len(board[0])):
            if board[i][num-1] != 0:
                cage.append(board[i][num-1])
                board[i][num-1] =0
                if len(cage) >1:
                    if cage[-1] == cage[-2]:
                        cage.pop()
                        cage.pop()
                        answer+=2 
                break
        
    return answer
