import numpy
import ete3

def compute_root_branch_length(tree):
    length = 0.0
    for c in tree.children:
        length += c.dist
    return length
