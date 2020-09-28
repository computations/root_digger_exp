#!/usr/bin/env python3

import ete3
import argparse
import numpy


parser = argparse.ArgumentParser()
parser.add_argument("--tree", required=True)
parser.add_argument("--root", required=True)
args = parser.parse_args()

def get_root_distance_toplogical(true_tree, inferred_tree):
    common_node_tt, _ = true_tree.get_closest_leaf()
    common_node_it = inferred_tree & common_node_tt.name
    cn_tt_dist = true_tree.get_distance(common_node_tt,
                                        true_tree.get_tree_root(),
                                        topology_only=True)
    cn_it_dist = inferred_tree.get_distance(common_node_it,
                                            inferred_tree.get_tree_root(),
                                            topology_only=True)
    return numpy.abs(cn_tt_dist - cn_it_dist)

lwr_tree = ete3.Tree(args.tree)
true_tree = ete3.Tree(args.root)

distance = get_root_distance_toplogical(true_tree, lwr_tree)
taxa = 0
for l in true_tree.iter_leaves():
    taxa += 1

print("Raw distance:", distance)
print("Normalized distance:", distance/taxa)
