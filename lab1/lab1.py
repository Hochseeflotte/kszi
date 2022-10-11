import random
from tabulate import tabulate
import pandas as pd
import numpy as np


def gen_matrix():
    matrix1 = [[[random.uniform(0,1) for p in range(7)] for p in range(5)] for p in range(4)]
    matrix2 =[]
    matrix3 =[]
    for i in matrix1:
        for j in i:
            for k in j:
                matrix2.append(round(k))
                if k <=0.3:
                    matrix3.append(1)
                elif k > 0.3 and k <= 0.5:
                    matrix3.append(2)
                elif k > 0.5 and k <= 0.7:
                    matrix3.append(3)
                elif k >0.7 and k <=0.9:
                    matrix3.append(4)
                else:
                    matrix3.append(5)
    matrix2 = np.array(matrix2).reshape(4,5,7)
    matrix3 = np.array(matrix3).reshape(4,5,7)
    return matrix1, matrix2, matrix3

def find_Q(matrix):
    Q=0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                Q += matrix[i][j][k]
    return Q/140

def find_q(matrix):
    q=0
    Wi = [0.4, 0.2, 0.2, 0.2]
    Wj = [0.2, 0.3, 0.1, 0.2, 0.2]
    Wk = [0.3, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(len(matrix[i][j])):
                q += (matrix[i][j][k] * Wi[i] * Wj[j] * Wk[k])
    return q

def min_sum(matrix):
    sum_x=sum(sum(sum(np.cumsum(matrix, axis=0))))
    sum_y = sum(sum(sum(np.cumsum(matrix, axis=1))))
    sum_z = sum(sum(sum(np.cumsum(matrix, axis=2))))
    print("sum in Block 0 = ",sum_x)
    print("sum in Block 1 = ",sum_y)
    print("sum in Block 2 = ",sum_z)
    minimal_sum = min(sum_x,sum_y,sum_z)
    if minimal_sum==sum_x: Block = 0
    elif minimal_sum == sum_y: Block=1
    else: Block = 2
    return minimal_sum, Block

#131, 446, 447, 331, 222.
def answers(matrix):
    return matrix[0][2][0], matrix[3][3][5], matrix[3][3][6], matrix[2][2][0], matrix[1][1][1]

def check_security(matrix_Q):
    if matrix_Q > 0.75:
        return True
    else: return False

A,B,C= gen_matrix()

def first_task():
    with open("lab1_results.txt", "w", encoding="utf-8") as out:
        for i in [A,B,C]:
            out.write('\n'.join(str(line) for line in i))
            out.write('\n')
            out.write('\n')
    print("Matrix A: \n")
    print(A)
    print("\nMatrix B: \n")
    print(B)
    print("\nMatrix C: \n")
    print(C)

def second_task():
    # print("Quality without weights")
    print("Quality without weights for matrix A: ", find_Q(A))
    print("Quality without weights for matrix B: ", find_Q(B))
    print("Quality without weights for matrix C: ", find_Q(C))
    print("Quality with weights for matrix A: ",find_q(A))
    print("Quality with weights for matrix B: ",find_q(B))
    print("Quality with weights for matrix C: ",find_q(C))

def third_task():
    print("Results for matrix A:", answers(A))
    print("Results  for matrix B: ", answers(B))
    print("Results for matrix C: ", answers(C))

def fourth_task():
    print("Security test without weights: ", check_security(find_Q(A)))
    print("Security test with weights: ", check_security(find_q(A)))

def fifth_task():
    labels = ["Matrix A", "Matrix B", "Matrix C"]
    results = [A, B, C]
    for i, j in zip(labels,results):
        # j=results.index(i)
        min_Sum, Block = min_sum(j)
        print(i, f" minimal sum: {min_Sum}  in block {Block}")

def main():
    print("Task №1")
    first_task()
    print("Task №2")
    second_task()
    print("Task №3")
    third_task()
    print("Task №4")
    fourth_task()
    print("Task №5")
    fifth_task()

main()