def is_valid(pos, n):
    row = pos[0]
    col = pos[1]
    return 0 <= row < n and 0 <= col < n

def get_killed_knights(row, col, size, board):
    killed_knights = 0
    rows = [-2, -1, 1, 2, 2, 1, -1, -2]
    cols = [1, 2, 2, 1, -1, -2, -2, -1]
    for i in range(8):
        current_pos = [row + rows[i], col + cols[i]]
        if is_valid(current_pos, size) and board[current_pos[0]][current_pos[1]] =='K':
            killed_knights += 1
    return killed_knights

n = int(input())
matrix = []
total_kills = 0

for _ in range(n):
    matrix.append([x for x in input()])

while True:
    most_kills = 0
    to_kill = []

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 'K':
                killed_knights = get_killed_knights(i, j, n, matrix)
                if killed_knights > most_kills:
                    most_kills = killed_knights
                    to_kill = [i, j]

    if most_kills == 0:
        break
    to_kill_row = to_kill[0]
    to_kill_col = to_kill[1]
    matrix[to_kill_row][to_kill_col] = '0'
    total_kills += 1

print(total_kills)
