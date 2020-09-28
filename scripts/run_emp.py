#!/usr/bin/env python3

import multiprocessing.pool
import subprocess
import yaml
import os
import datetime
import importlib
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument('--prefix', type=str, required=True)
parser.add_argument('--datasets', type=str, required=True)
parser.add_argument('--datasets-prefix', type=str)
parser.add_argument('--rd', type=str, required=True)
parser.add_argument('--procs', type=int, required=True)
parser.add_argument('--exhaustive', action='store_true', default=False)
parser.add_argument('--no-run-iq',
                    action='store_false',
                    default=True,
                    dest='runiq')
parser.add_argument('--no-run-rd',
                    action='store_false',
                    default=True,
                    dest='runrd')
args = parser.parse_args()

drawlh = importlib.import_module('drawlh')

RD = os.path.abspath(
    args.rd
) + " --msa {msa} --tree {tree} --exhaustive --prefix {prefix} {options} --threads 1"

if args.exhaustive:
    RD += " --exhaustive"


class dataset:
    def __init__(self, cwd, dataset_root, dataset_path, working_dir_prefix,
                 dataset_dict):
        self._msa = dataset_dict['msa']
        self._tree = dataset_dict['tree']
        self._results_prefix = dataset_dict['results_prefix']
        self._image = dataset_dict['image']
        self._log = dataset_dict['log']
        self._options = dataset_dict['options']
        self._dataset_root = os.path.abspath(dataset_root)
        self._dataset_path = dataset_path
        self._working_dir_prefix = os.path.abspath(working_dir_prefix)
        self._current_working_directory = os.path.abspath(cwd)

    @property
    def working_dir(self):
        return os.path.join(os.path.abspath(self._working_dir_prefix),
                            self._dataset_path)

    @property
    def msa_path(self):
        return os.path.join(self._dataset_root, self._dataset_path, self._msa)

    @property
    def tree_path(self):
        return os.path.join(self._dataset_root, self._dataset_path, self._tree)

    @property
    def data_path(self):
        return os.path.join(self._dataset_root, self._dataset_path)

    @property
    def rooted_tree_path(self):
        return os.path.join(self._path_prefix,
                            self._results_prefix + ".rooted.tree")

    @property
    def lwr_tree_path(self):
        return os.path.join(self._path_prefix,
                            self._results_prefix + ".lwr.tree")

    @property
    def _results_path(self):
        return os.path.join(self.working_dir, self._results_prefix)

    @property
    def rd_results_prefix(self):
        os.path.join(self.working_dir, self._results)

    @property
    def log_path(self):
        return os.path.join(self.working_dir, self._log)

    @property
    def image_path(self):
        return os.path.join(self.working_dir, self._image)

    @property
    def rd_options(self):
        opts = []
        if 'early-stop' in self._options and self._options['early-stop']:
            opts.append('--early-stop')
        if 'invariant-sites' in self._options and self._options[
                'invariant-sites']:
            opts.append('--invariant-sites')
        if 'partition' in self._options:
            opts.append('--partition')
            opts.append(
                os.path.join(self.data_path, self._options['partition']))
        if 'rate-cats' in self._options:
            opts.append('--rate-cats')
            opts.append(self._options['rate-cats'])

        return ' '.join([str(o) for o in opts])

    @property
    def _done_file(self):
        return os.path.join(self.working_dir,
                            "." + self._results_prefix + ".done")

    @property
    def rd_command(self):
        return RD.format(msa=self.msa_path,
                         tree=self.tree_path,
                         prefix=self._results_path,
                         options=self.rd_options).split(' ')

    def make_dirs(self):
        if not os.path.exists(self.working_dir):
            os.makedirs(self.working_dir, exist_ok=True)

    def check_data_exists(self):
        return {
            self.msa_path: os.path.exists(self.msa_path),
            self.tree_path: os.path.exists(self.tree_path)
        }

    def check_done(self):
        return os.path.exists(self._done_file)

    def set_done(self):
        if self.check_done():
            raise Exception("Dataset {} was already finished".format(
                self._results_prefix))
        with open(self._done_file, 'w') as df:
            df.write(datetime.datetime.now().isoformat())

    def __str__(self):
        return self._results_path


def run_rd(ds):
    if ds.check_done():
        return
    ds.make_dirs()
    print("Running rd on : ", ds)
    with open(ds.log_path, 'a') as logfile:
        subprocess.run(ds.rd_command, stdout=logfile)
    ds.set_done()


dataset_filename = os.path.abspath(args.datasets)
with open(dataset_filename) as infile:
    datasets = yaml.load(infile, Loader=yaml.FullLoader)

datasets_prefix = os.path.split(dataset_filename)[0]

jobs = []
if not os.path.exists(args.prefix):
    os.mkdir(args.prefix)
else:
    if not os.path.isdir(args.prefix):
        raise Exception("Prefix is already a file")

missing_data = []

for k, d in datasets.items():
    dataset_path = d['directory']
    for dataset_dict in d['datasets']:
        ds = dataset(os.getcwd(), datasets_prefix, dataset_path, args.prefix,
                     dataset_dict)
        ret = ds.check_data_exists()
        for k, v in ret.items():
            if not v:
                missing_data.append(k)
        jobs.append(ds)

if len(missing_data) != 0:
    print("Missing data from:")
    print(missing_data)
    sys.exit(1)

tp = multiprocessing.pool.ThreadPool(args.procs)
if args.runrd:
    tp.map(run_rd, jobs)
for k, d in datasets.items():
    directory_root = d['directory']
    for dataset_dict in d['datasets']:
        try:
            ds = dataset(os.getcwd(), dataset_prefix, dataset_path,
                         args.prefix, dataset_dict)
            if args.runrd:
                drawlh.draw_lh(ds.tree_path, ds.image_path, ds.lwr_tree_path,
                               False)
        except Exception as e:
            print(directory_root, ":", ds['msa'], ":", e)
