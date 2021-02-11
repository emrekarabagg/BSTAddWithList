import time

start_time = time.time()


def parent(x):
    while x != 0:
        x = int((x - 1) / 2)


tree = [None] * 10000
f2 = open("test2.txt", "w")


def inorder(current_index):
    if tree[current_index] is not None:
        inorder(2 * current_index + 1)
        parent(current_index)
        f2.write('{}-'.format(tree[current_index]))
        inorder(2 * current_index + 2)


def add_element_tree(x):
    current_index = 0
    while True:
        if tree[current_index] is None:
            tree[current_index] = x
            break
        elif tree[current_index] <= x:
            if tree[current_index] == x:
                break
            else:
                current_index = 2 * current_index + 2
        elif tree[current_index] >= x:
            if tree[current_index] == x:
                break
            else:
                current_index = 2 * current_index + 1


def main():
    f = open("test.txt", "r")

    numbers = f.read().split(" ")

    for i in numbers:
        add_element_tree(int(i))

    inorder(0)
    f2.close()
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
