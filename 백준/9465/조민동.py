n = int(input())
result = []
for i in range(n):
    column = int(input())
    matrix = []
    row1 = list(map(int, input().split()))
    matrix.append(row1)
    row2 = list(map(int, input().split()))
    matrix.append(row2)

    record = [[0] * column, [0] * column]
    for c in range(column):
        if c == 0:
            record[0][c], record[1][c] = matrix[0][c], matrix[1][c]
        elif c == 1:
            record[0][c] = matrix[0][c] + record[1][c - 1]
            record[1][c]=matrix[1][c] + record[0][c - 1]
        else:
            record[0][c] = matrix[0][c] + max(record[1][c - 1],
                                              record[0][c - 2],
                                              record[1][c - 2])
            record[1][c] = matrix[1][c] + max(record[0][c - 1],
                                              record[0][c - 2],
                                              record[1][c - 2])

    result.append(max(record[0][-1], record[1][-1]))

for a in result:
    print(a)
