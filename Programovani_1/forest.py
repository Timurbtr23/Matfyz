class Tree:

    def __init__(self, x, y, ln, tr):
        self.x = x
        self.y = y
        self.length = ln
        self.trunk = tr
        self.box = [self.x + (self.length*2-1), self.y + (self.length + self.trunk)]
        self.top = [self.x+self.length, self.y]


if __name__ == "__main__":

    _input = input()
    trees = []
    while _input != '':
        trees.append(Tree(*[int(x) for x in _input.split()]))
        _input = input()

    max_x, max_y = 0, 0
    for tree in trees:
        if tree.box[0] > max_x:
            max_x = tree.box[0]
        if tree.box[1] > max_y:
            max_y = tree.box[1]

    field = []
    for j in range(max_y):
        field.append(['.'] * max_x)





# def print_tree(point, width, trunk):
#     def print_line(tree, left_point, right_point):
#         tree[left_point - 1] = "*"
#         tree[right_point - 1] = "*"
#
#         for i in range(len(tree)):
#             print(tree[i], end="")
#         print()
#
#     tree_line = ["."] * width
#     first_line = ["."] * width
#     first_line[point - 1] = '*'
#     left_star = point
#     right_star = point
#
#     while left_star != 0:
#         print_line(tree_line, left_star, right_star)
#         left_star -= 1
#         right_star += 1
#
#     for j in range(trunk):
#         for i in range(len(first_line)):
#             print(first_line[i], end="")
#         if j != trunk - 1:
#             print()
#
#
# if __name__ == "__main__":
#     first_tree = []
#     start_point = int(input())
#     trunk = int(input())
#     width = start_point * 2 - 1
#     print_tree(start_point, width, trunk)
