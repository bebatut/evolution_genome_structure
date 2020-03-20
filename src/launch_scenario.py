#!/usr/bin/env python

import argparse
import subprocess

from os import chdir
from pathlib import Path


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--scenario',
        help='scenario to launch',
        required=True,
        choices=['control', 'mut+', 'mut-', 'sel+', 'sel-', 'pop+', 'pop-'])
    parser.add_argument(
        '--seed',
        help='seed to launch',
        required=True,
        choices=['0', '1', '2', '3', '4'])
    args = parser.parse_args()

    data = Path('data')
    aevol_run_fp = '%s/src/aevol_ltisee/src/aevol_run' % str(Path.cwd())

    # get scenario folder
    sc_dir = data / Path(args.scenario) / Path('seed0%s' % args.seed)
    if not sc_dir.is_dir():
        raise ValueError('Need to prepare scenario first')

    # launch simulation
    chdir(sc_dir)
    subprocess.run([
        aevol_run_fp,
        '-n',
        '500000',
        '-p',
        '-1'])#,
        #'--noX'])