# vector의 계산
u = [2, 2]
v = [2, 3]
z = [3, 5]

result = [sum(t) for t in zip(u, v, z)]
print(result)
print("-------------------")

# Scalar- Vector 계산
u = [1, 2, 3]
v = [4, 5, 6]
a = 5

print([a * sum(z) for z in zip(u, v)])
print("-------------------")

# 이차원 행렬 계산
matrix_a = [[3, 6], [4, 5]]
matrix_b = [[5, 8], [6, 7]]

result2 = [[sum(row) for row in zip(*t)]
           for t in zip(matrix_a, matrix_b)]

print(result2)
print(2 + 4 / 2 * 4)
