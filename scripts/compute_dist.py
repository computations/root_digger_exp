#!/usr/bin/env python3

import ete3
import argparse
import importlib

make_exp = importlib.import_module('make_exp')

parser = argparse.ArgumentParser()
parser.add_argument("--tree", required=True)
parser.add_argument("--root", required=True)
args = parser.parse_args()


def get_idx_clade_list(tree, idx):
    return sorted([
        n.name for n in tree.get_tree_root().children[idx].traverse()
        if n.name != ''
    ])


def get_right_clade_list(tree):
    return get_idx_clade_list(tree, 1)


def get_left_clade_list(tree):
    return get_idx_clade_list(tree, 0)


def reroot_tree_by_true_root(true_tree, inferred_tree):
    clade_pair = (get_left_clade_list(true_tree),
                  get_right_clade_list(true_tree))
    try:
        inferred_tree.set_outgroup(inferred_tree.get_common_ancestor(clade_pair[0]))
    except:
        inferred_tree.set_outgroup(inferred_tree.get_common_ancestor(clade_pair[1]))
    return inferred_tree


lwr_tree = ete3.Tree(args.tree)
true_tree = ete3.Tree(args.root)
rooted_tree = reroot_tree_by_true_root(true_tree, lwr_tree)
tree_root = rooted_tree.get_tree_root()
distance = 0.0
taxa = 0
for node in rooted_tree.traverse():
    if node.is_leaf():
        taxa += 1
    if not hasattr(node, "LWR"):
        continue
    lwr = float(node.LWR)
    raw_distance = tree_root.get_distance(node, topology_only=True)
    print(raw_distance, lwr)
    distance += raw_distance * lwr

print(distance)
print(distance/taxa)
