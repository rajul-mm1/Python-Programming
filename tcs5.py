rows, cols = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(rows)]

max_count = 0
row_index = -1

for i in range(rows):
    count_ones = sum(matrix[i])
    if count_ones > max_count:
        max_count = count_ones
        row_index = i + 1

print(row_index) 