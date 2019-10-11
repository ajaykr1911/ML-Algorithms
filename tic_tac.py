import numpy as np
from random import randint
zero_mat = np.zeros([3,3], dtype=int)
while True:
    i,j = int(input()), int(input())
    zero_mat[i][j] = 1
    print('matrix after user move: \n',zero_mat)

    while True:
        k,l = randint(0,2), randint(0,2)
        if zero_mat[k][l] == 0 :
            zero_mat[k][l] = 5
            break

    print('matrix after computer move: \n',zero_mat)

    count = 0

    sum = zero_mat[0][0]+zero_mat[1][1]+zero_mat[2][2]
    if sum == 3:
        print("user is winner")
        count = 1
        break
    if sum == 15:
        print('you lose')
        count = 1
        break
    
    sum = zero_mat[0][2]+zero_mat[1][1]+zero_mat[2][0]
    if sum == 3:
        print("user is winner")
        count = 1
        break
    if sum == 15:
        print('you lose')
        count = 1
        break

    for i in range(3):
        sum = 0
        for j in range(3):
            sum += zero_mat[i][j]
            if sum == 3:
                print("user is winner")
                count = 1
                break
            if sum == 15:
                print('you lose')
                count = 1
                break

    for i in range(3):
        sum = 0
        for j in range(3):
            sum += zero_mat[j][i]
            if sum == 3:
                print("user is winner")
                count = 1
                break
            if sum == 15:
                print('you lose')
                count = 1
                break
    if count == 1:
        break       
