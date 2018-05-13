import sys
# zero base가 아니야... 충격!
#sqCount = int(sys.stdin.readline())
sqList  = [[[2,3],[6,9]],[[4,2],[9,8]]]
#for _ in range(sqCount):
#    sq = list(map(int, sys.stdin.readline().split(',')))
#    sqList.append([[sq[0],sq[1]],[sq[2],sq[3]]])

board = [[0 for rows in range(10)]for cols in range(10)]


def Set3(c, r):
    board[c][r] = 3
    count = 1
    if(c != 0 and board[c-1][r] == 1):
        count += Set3(c-1,r)
    if(r != 0 and board[c][r-1] == 1):
        count += Set3(c,r-1)
    if(c != 9 and board[c+1][r] == 1):
        count += Set3(c+1,r)
    if(r != 9 and board[c][r+1] == 1):
        count += Set3(c,r+1)
    return count

count = 0
for i in range(len(sqList)):
    A = [sqList[i][0][0],sqList[i][0][1]]
    B = [sqList[i][1][0],sqList[i][1][1]]
    
    for r in range(A[0],B[0]+1):
        for c in range(A[1],B[1]+1):
            
            if(r == A[0] or r == B[0] or c == A[1] or c == B[1]):
                board[c-1][r-1] = 2
            elif(board[c-1][r-1] != 2):
                board[c-1][r-1] = 1
maxValue = 0
for r in range(0, 10):
    for c in range(0, 10):
        if(board[c][r] == 1):
            maxValue=max(maxValue, Set3(c,r))

print(maxValue)

for i in range(len(board)):
    print(board[i])

