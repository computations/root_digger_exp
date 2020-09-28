#!/bin/bash

iqtree_prog=~/wrk/hits/IQ-TREE/build/iqtree
rd_prog=~/wrk/hits/root_digger/bin/rd
indelible_prog=~/wrk/indelible/INDELibleV1.03/src/indelible

./scripts/make_exp.py \
    --iq ${iqtree_prog} \
    --rd ${rd_prog} \
    --indelible ${indelible_prog} \
    --procs 40\
    --iters 100\
    --msa ./angiosperms/cds_outgroup_removed.fasta\
    --tree ./angiosperms/cds_outgroup_removed_opt_brlen.tree\
    --path ./results/emperical_search/angiosperms/cds_outgroup_removed

./scripts/make_exp.py \
    --iq ${iqtree_prog} \
    --rd ${rd_prog} \
    --indelible ${indelible_prog} \
    --procs 40\
    --iters 100\
    --msa ./angiosperms/cds12_outgroup_removed.fasta\
    --tree ./angiosperms/cds12_outgroup_removed_opt_brlen.tree\
    --path ./results/emperical_search/angiosperms/cds12_outgroup_removed

./scripts/make_exp.py \
    --iq ${iqtree_prog} \
    --rd ${rd_prog} \
    --indelible ${indelible_prog} \
    --procs 40\
    --iters 100\
    --msa ./angiosperms/cds.fasta\
    --tree ./angiosperms/cds_brlen_opt.tree\
    --path ./results/emperical_search/angiosperms/cds_with_outgroup

./scripts/make_exp.py \
    --iq ${iqtree_prog} \
    --rd ${rd_prog} \
    --indelible ${indelible_prog} \
    --procs 40\
    --iters 100\
    --msa ./angiosperms/cds12.fasta\
    --tree ./angiosperms/cds12_opt_brlen.tree\
    --path ./results/emperical_search/angiosperms/cds12_with_outgroup

./scripts/make_exp.py \
    --iq ${iqtree_prog} \
    --rd ${rd_prog} \
    --indelible ${indelible_prog} \
    --procs 40\
    --iters 100\
    --msa ./ficus/ficus.fasta\
    --tree ./ficus/ficus_rooted_removed_outgroup_opt.nwk\
    --path ./results/emperical_search/ficus/ficus_no_outgroup

./scripts/make_exp.py \
    --iq ${iqtree_prog} \
    --rd ${rd_prog} \
    --indelible ${indelible_prog} \
    --procs 40\
    --iters 100\
    --msa ./ficus/ficus_outgroup.fasta\
    --tree ./ficus/ficus_outgroup_opt_brlen.tree\
    --path ./results/emperical_search/ficus/ficus_with_outgroup

./scripts/make_exp.py \
    --iq ${iqtree_prog} \
    --rd ${rd_prog} \
    --indelible ${indelible_prog} \
    --procs 40\
    --iters 100\
    --msa ./grasses/plastid245.fasta\
    --tree ./grasses/plastid245_brlen_opt.nwk\
    --path ./results/emperical_search/grasses/grasses_with_outgroup

./scripts/make_exp.py \
    --iq ${iqtree_prog} \
    --rd ${rd_prog} \
    --indelible ${indelible_prog} \
    --procs 40\
    --iters 100\
    --msa ./spiders/missing_species.fasta\
    --tree ./spiders/ml_missing_species_opt_brlen.tree\
    --path ./results/emperical_search/spiders/missing_species_no_outgroup

./scripts/make_exp.py \
    --iq ${iqtree_prog} \
    --rd ${rd_prog} \
    --indelible ${indelible_prog} \
    --procs 40\
    --iters 100\
    --msa ./spiders/missing_species_outgroup.fasta\
    --tree ./spiders/missing_species_brlen_opt.nwk\
    --path ./results/emperical_search/spiders/missing_species_with_outgroup

./scripts/make_exp.py \
    --iq ${iqtree_prog} \
    --rd ${rd_prog} \
    --indelible ${indelible_prog} \
    --procs 40\
    --iters 100\
    --msa ./spiders/mitocondrial.fasta\
    --tree ./spiders/mitocondrial_opt_brlen.tree\
    --path ./results/emperical_search/spiders/mitocondrial_no_outgroup

./scripts/make_exp.py \
    --iq ${iqtree_prog} \
    --rd ${rd_prog} \
    --indelible ${indelible_prog} \
    --procs 40\
    --iters 100\
    --msa ./spiders/mitocondrial_outgroup.fasta\
    --tree ./spiders/mitocondrial_outgroup_brlen_opt.nwk\
    --path ./results/emperical_search/spiders/mitocondrial_with_outgroup

/scripts/make_exp.py \
    --iq ${iqtree_prog} \
    --rd ${rd_prog} \
    --indelible ${indelible_prog} \
    --procs 40\
    --iters 100\
    --msa ./beetles/nucleotide_supermatrices/supermatrix_nt.A/supermatrix_nt.A.fas\
    --tree ./beetles/supermatrix_nt.A_best_tree.brlen_opt.rooted.tree\
    --partition-rd ./beetles/nucleotide_supermatrices/supermatrix_nt.A/partitions.txt\
    --partition-iq ./beetles/nucleotide_supermatrices/supermatrix_nt.A/partitions.nex\
    --path ./results/emperical_search/beetles/nt_a_with_outgroup

./scripts/make_exp.py \
    --iq ${iqtree_prog} \
    --rd ${rd_prog} \
    --indelible ${indelible_prog} \
    --procs 40\
    --iters 100\
    --msa ./beetles/nucleotide_supermatrices/supermatrix_nt.A/supermatrix_nt.A.no_outgroup.fas\
    --tree ./beetles/supermatrix_nt.A_best_tree.rooted.no_outgroup.brlen_opt.rooted.tree\
    --partition-rd ./beetles/nucleotide_supermatrices/supermatrix_nt.A/partitions.txt\
    --partition-iq ./beetles/nucleotide_supermatrices/supermatrix_nt.A/partitions.nex\
    --path ./results/emperical_search/beetles/nt_a_without_outgroup

./scripts/make_exp.py \
    --iq ${iqtree_prog} \
    --rd ${rd_prog} \
    --indelible ${indelible_prog} \
    --procs 40\
    --iters 100\
    --msa ./beetles/nucleotide_supermatrices/supermatrix_nt.A.homogeneous2/supermatrix_nt.A.homogeneous2.fas\
    --tree ./beetles/supermatrix_nt.A_homogeneous_2_best_tree.brlen_opt.rooted.tree\
    --partition-rd ./beetles/nucleotide_supermatrices/supermatrix_nt.A.homogeneous2/raxml_partitions.txt\
    --partition-iq ./beetles/nucleotide_supermatrices/supermatrix_nt.A.homogeneous2/partitions.nex\
    --path ./results/emperical_search/beetles/nt_homo_with_outgroup

./scripts/make_exp.py \
    --iq ${iqtree_prog} \
    --rd ${rd_prog} \
    --indelible ${indelible_prog} \
    --procs 40\
    --iters 100\
    --msa ./beetles/nucleotide_supermatrices/supermatrix_nt.A.homogeneous2/supermatrix_nt.A.homogeneous2.no_outgroup.fas\
    --tree ./beetles/supermatrix_nt.A_homogeneous_2_best_tree.no_outgroup.brlen_opt.rooted.tree\
    --partition-rd ./beetles/nucleotide_supermatrices/supermatrix_nt.A.homogeneous2/raxml_partitions.txt\
    --partition-iq ./beetles/nucleotide_supermatrices/supermatrix_nt.A.homogeneous2/partitions.nex\
    --path ./results/emperical_search/beetles/nt_homo_without_outgroup

