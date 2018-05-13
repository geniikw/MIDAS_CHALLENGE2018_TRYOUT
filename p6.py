import sys

# zero base가 아니야... 충격!




sqCount = int(sys.stdin.readline())
sqList  = [[[2,3],[6,9]],[[4,2],[9,8]]]
#for _ in range(sqCount):
#    sq = list(map(int, sys.stdin.readline().split(',')))
#    sqList.append([[sq[0],sq[1]],[sq[2],sq[3]]])

board = [[0 for rows in range(10)]for cols in range(10)]
count = 0
for i in range(len(sqList)):
    A = [sqList[i][0][0],sqList[i][0][1]]
    B = [sqList[i][1][0],sqList[i][1][1]]
    
    for r in range(A[0],B[0]):
        for c in range(A[1],B[1]):
            board[r-1][c-1] = 1

    

print(board)
