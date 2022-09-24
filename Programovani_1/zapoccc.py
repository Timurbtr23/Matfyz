class posit:
    def __init__(self, x=0, y=0, dist=0):
        self.x = x
        self.y = y
        self.dist = dist


def is_in(x, y, N):
    if 1 <= x <= N and 1 <= y <= N:
        return True
    return False


def calculate_steps(horse, finish, N=8):
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    arr = [posit(horse[0], horse[1], 0)]
    visited = [[False for i in range(N + 1)] for j in range(N + 1)]
    visited[horse[0]][horse[1]] = True
    while len(arr) > 0:
        t = arr[0]
        arr.pop(0)
        if (t.x == finish[0] and
                t.y == finish[1]):
            return t.dist
        for i in range(8):
            x = t.x + dx[i]
            y = t.y + dy[i]
            if is_in(x, y, N) and not visited[x][y]:
                visited[x][y] = True
                arr.append(posit(x, y, t.dist + 1))


def input_data():
    field = []
    with open("input.txt", "r", encoding="utf-8") as file:
        for line in file:
            field += [line[:-1]]
    return field


def find_pos(field):
    x, y = 1, 8
    for line in field:
        for point in line:
            if point == "S":
                position = [x, y]
            x += 1
        x = 1
        y -= 1
    return position


def find_finish(field):
    x, y = 1, 8
    for line in field:
        for point in line:
            if point == "C":
                finish = [x, y]
            x += 1
        x = 1
        y -= 1
    return finish


if __name__ == '__main__':
    board = input_data()
    horse = find_pos(board)
    finish = find_finish(board)
    print(calculate_steps(horse, finish))
