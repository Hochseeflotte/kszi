import cvxpy
import pandas as pd
import numpy as np


def task2(experts):
    a = []
    print("Experts: ", experts)
    for i in range(1, experts + 1):
        a.append(i)
    df = pd.DataFrame(columns=a, index=a)
    m = np.random.randint(low=1, high=10, size=(experts, experts)) / np.random.randint(low=1, high=10, size=(experts, experts))
    for i in range(0, experts):
        for j in range(0, experts):
            m[i, i] = 1
            m[i, j] = 1 / m[j, i]
    df[a] = m
    df['sum'] = df.sum(axis=1)
    print("Sum of sum: ", sum(df['sum']))
    df['weight'] = df['sum']/sum(df['sum'])
    weight = []
    for i in range(1, experts+1):
        weight.append(df['sum'][i]/sum(df['sum']))
        i += 1
    print("Sum of weight: ", sum(df['weight']))
    print("Weight arr: ", weight)
    return df

def task3(experts):
    a = []
    print("Experts: ", experts)
    for i in range(1, experts + 1):
        a.append(i)
    df = pd.DataFrame(columns=a, index=a)
    m = np.random.randint(low=1, high=10, size=(experts, experts)) / np.random.randint(low=1, high=10, size=(experts, experts))
    for i in range(0, experts):
        for j in range(0, experts):
            m[i, i] = 1
            m[i, j] = 1 / m[j, i]
    df[a] = m
    df['sum'] = df.sum(axis=1)
    print("Sum of sum: ", sum(df['sum']))
    df['weight'] = df['sum']/sum(df['sum'])
    weight = []
    for i in range(1, experts+1):
        weight.append(df['sum'][i]/sum(df['sum']))
        i += 1
    print("Sum of weight: ", sum(df['weight']))
    print("Weight arr: ", weight)
    H = 1000
    df['hi'] = np.random.randint(200, 700, (experts, 1))
    b = list(df['hi'])
    selection = cvxpy.Variable(df['weight'].shape, boolean=True)
    w_constraint = [cvxpy.matmul(b, selection) <= H]
    total = cvxpy.sum(selection, axis=0)
    proglem = cvxpy.Problem(cvxpy.Maximize(total), w_constraint)
    proglem.solve(solver=cvxpy.ECOS_BB)
    selection.value.round()
    df['x'] = selection.value.round()
    return df


if __name__ == "__main__":
    print("Task №2: ")
    print(task2(3))
    print("Task №3: ")
    print(task3(3))
