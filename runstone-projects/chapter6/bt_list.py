def make_binary_tree(root):
    return [root, [], []]


def insert_left(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, [], t])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root_val(root):
    return root[0]


def set_root_val(root, new_val):
    root[0] = new_val


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]

# my_tree = ["a", ["b", ["d", [], []], ["e", [], []]], ["c", ["f", [], []], []]]
# print(my_tree)
# print("left subtree = ", my_tree[1])
# print("root = ", my_tree[0])
# print("right subtree = ", my_tree[2])
# print("left subtree root = ", my_tree[1][0])

