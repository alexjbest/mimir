from mas_evaluator import evaluateAST
from Queue import *
import math
import operator
import copy


#TODO Remove every trace of deepcopy from everywhere
'''Given a root node of an expression tree for an answer this code will traverse the tree and output a list of possible wrong answers with one mistake.'''
def wrong_answer_dict(root):
    wrong_ops = { "+": ["-"],
                "-": ["+"],
                "*": ["+", "/"],
                "/": ["*"], } #TODO: Make more of these, eventually in a db??
    wrong_ans = dict()
    not_looked_at = LifoQueue()
    not_looked_at.put(root)
    while not not_looked_at.empty():
        node = not_looked_at.get()
        node_val = node.value
        if node_val in wrong_ops:
            for wrong_op in wrong_ops[str(node_val)]:
                node.value = wrong_op
                current_wrong_answer = evaluateAST(copy.deepcopy(root)).answer
                wrong_ans[str(current_wrong_answer)] = str.format("Oops, did you do {0} on {1}, when you meant to do {2}?",
                    op_to_str(wrong_op),
                    ", ".join([str(evaluateAST(copy.deepcopy(c)).answer) for c in node.children[:-1]]) + " and " + str(evaluateAST(copy.deepcopy(node.children[-1])).answer),
                    node_val
                )
            node.value = node_val
        for child in node.children:
            not_looked_at.put(child)
    return wrong_ans

'''TODO: expand this code so it actually works properly
    for wrong_ops in ops[str(node.value)]:
        for child in root.children:
            incorrect_exprs.append()
'''

def op_to_str(op):
    ops = { operator.add : "$+$",
            operator.sub : "$-$",
            operator.mul : "$\\times$",
            operator.truediv : "$\\div$",
            operator.pow : "^" }
    if op in ops:
        return ops[op]
    return str(op)

