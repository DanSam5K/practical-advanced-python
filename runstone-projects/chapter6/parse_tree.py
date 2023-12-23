from basic import Stack
from trees import BinaryTree

def build_parse_tree(fp_expr):
    fp_list = fp_expr.split()
    p_stack = Stack()
    expr_tree = BinaryTree("")
    p_stack.push(expr_tree)
    current_tree = expr_tree

    for i in fp_list:
        if i == "(":
            current_tree.insert_left("")
            p_stack.push(current_tree)
            current_tree = current_tree.get_left_child
        elif i in ["+", "-", "*", "/"]:
            current_tree.root = i
            current_tree.insert_right("")
            p_stack.push(current_tree)
            current_tree = current_tree.right_child
        elif i.isdigit():
            current_tree.root = int(i)
            parent = p_stack.pop()
            current_tree = parent
        elif i == ")":
            current_tree = p_stack.pop()
        else:
            raise ValueError(f"Unknown operator '{i}'")
        
    return expr_tree

pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
pt.postorder()
