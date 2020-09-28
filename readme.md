# RootDigger Experiment Files

This is the repository for the experiments used in the RootDigger paper. There
are two kinds of experiments: simulation and empirical. 

# Simulation Experiments

To run the simulation experiments, use the `scripts/make_exp.py` script. The
command line options are

```
usage: make_exp.py [-h] --path PATH --msa MSA [MSA ...] --trees TREES [TREES ...]
                   [--partition-rd PARTITION_RD] [--partition-iq PARTITION_IQ] --iters ITERS
                   [--procs PROCS] [--run-rd] [--run-iq-tree] [--no-run-rd] [--no-run-iq-tree]
                   [--rd-exhaustive] [--rd RD] [--iq IQ] [--indelible INDELIBLE] [--profile]

optional arguments:
  -h, --help            show this help message and exit
  --path PATH           Path to store the exp
  --msa MSA [MSA ...]
  --trees TREES [TREES ...]
  --partition-rd PARTITION_RD
  --partition-iq PARTITION_IQ
  --iters ITERS
  --procs PROCS
  --run-rd
  --run-iq-tree
  --no-run-rd
  --no-run-iq-tree
  --rd-exhaustive
  --rd RD
  --iq IQ
  --indelible INDELIBLE
  --profile
```

`--trees` and `--msa` take either a path to a file, or a number. In the case of
a file, the contents of the file is used for the experiment. In the case of a
number, a random dataset is generated with the given size. For example, if
`--trees 10 40 --msa 1000 2000` is used, then 4 datasets are generated, one for
each combination of trees and lengths provided. For this specific example, the
simulated data would be:

- 10 taxa, 1000 sites,
- 10 taxa, 2000 sites,
- 40 taxa, 1000 sites and,
- 40 taxa, 2000 sites.

## Requirements

Indelible is needed to generate random alignments.

# Empirical experiments

The `scripts/run_emp.py` will run the experiments for empirical datasets. In
order to do this, `empirical_data_2020-09-28.tar.xz` needs to be extracted. The
command line arguments for this script are 

```
usage: run_emp.py [-h] --prefix PREFIX --datasets DATASETS [--datasets-prefix DATASETS_PREFIX]
                  --rd RD --procs PROCS [--exhaustive] [--no-run-iq] [--no-run-rd]

optional arguments:
  -h, --help            show this help message and exit
  --prefix PREFIX
  --datasets DATASETS
  --datasets-prefix DATASETS_PREFIX
  --rd RD
  --procs PROCS
  --exhaustive
  --no-run-iq
  --no-run-rd
```

Here, `--prefix` is the directory that will be created and experiments will be
run in. `--datasets` is the path to the `datasets.yaml` file, which is included
in the archive. `--datasets-prefix` is the root of the directory where the
datafiles are (from the archive).
