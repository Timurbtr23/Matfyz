def print_tree(point, width, trunk):
    def print_line(tree, left_point, right_point):
        tree[left_point-1] = "*"
        tree[right_point-1] = "*"

        for i in range(len(tree)):
            print(tree[i], end="")
        print()

    tree_line = ["."] * width
    first_line = ["."] * width
    first_line[point-1] = '*'
    left_star = point
    right_star = point

    while left_star != 0:
        print_line(tree_line, left_star, right_star)
        left_star -= 1
        right_star += 1

    for j in range(trunk):
        for i in range(len(first_line)):
            print(first_line[i], end="")
        if j != trunk-1:
            print()


if __name__ == "__main__":
    start_point = int(input())
    trunk = int(input())
    width = start_point*2 - 1
    print_tree(start_point, width, trunk)
