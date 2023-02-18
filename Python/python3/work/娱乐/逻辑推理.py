import numpy as np


def fun(x):
    x[0] += 1
    if x[0] == 4:
        x[1:] = fun(x[1:])
    return x % 4


answer = np.array([0] * 10)
d2 = np.array([2, 3, 0, 1])
d3 = np.array([[6, 2, 4], [2, 3, 4], [3, 4, 6], [2, 3, 6]])
d4 = np.array([[1, 5], [2, 7], [1, 9], [6, 10]])
d5 = np.array([8, 4, 9, 7])
d6 = np.array([[2, 4], [1, 6], [3, 10], [5, 9]])
d7 = np.array([2, 1, 0, 3])
d8 = np.array([7, 5, 2, 10])
d9 = np.array([6, 10, 2, 9])
d10 = np.array([3, 2, 4, 1])
i = 0
while len(answer[answer == 3]) != 10:
    print(i, end='\r')
    i += 1
    answer = fun(answer)
    if d2[answer[1]] != answer[4]:
        continue
    if len(set(answer[d3[answer[2]] - 1])) != 1:
        continue
    if len(set(answer[d4[answer[3]] - 1])) != 1:
        continue
    if answer[d5[answer[4]] - 1] != answer[4]:
        continue
    if (answer[d6[answer[5]] - 1][0] != answer[7]) or (answer[d6[answer[5]] - 1][1] != answer[7]):
        continue
    if np.argmin(np.bincount(answer)) != d7[answer[6]]:
        continue
    if abs(answer[d8[answer[7]] - 1] - answer[0]) == 1:
        continue
    if (answer[0] == answer[5]) == (answer[d9[answer[8]] - 1] == answer[4]):
        continue
    if max(np.bincount(answer)) - min(np.bincount(answer)) == d10[answer[9]]:
        break

a = ['A', 'B', 'C', 'D']
for i in answer:
    print(a[i], end=',')
