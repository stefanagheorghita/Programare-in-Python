matrix = [
    ['f', 'i', 'r', 's'],
    ['n', '_', 'l', 't'],
    ['o', 'b', 'a', '_'],
    ['h', 't', 'y', 'p']]

# matrix = [
#     ['a', 'n'],
#     ['e','a'],
#     ['r', '_'],
#     ['e','a'],
#     ['m','r'],
#     ['_','e']
#  ]
# matrix=[
#     ['1','2','3','4'],
#     ['b','c','d','a'],
#     ['a','4','1','b'],
#     ['4','3','2','c'],
#     ['3','2','1','d']
# ]
row = 0
col = 0
res = ""
while row < len(matrix) - 1 and col < len(matrix[0]) - 1:
    for j in range(col, len(matrix[0]) - col):
        res = res + matrix[row][j]
    for i in range(row + 1, len(matrix) - row):
        res = res + matrix[i][len(matrix[0]) - 1 - col]
    for j in range(len(matrix[0]) - 2 - col, col - 1, -1):
        res = res + matrix[len(matrix) - 1 - row][j]
    for i in range(len(matrix) - 2 - row, row, -1):
        res = res + matrix[i][col]
    row = row + 1
    col = col + 1
print(res)
