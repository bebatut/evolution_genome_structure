#!/usr/bin/env python

import argparse
import subprocess

from os import chdir
from pathlib import Path

params = {
    'STRAIN_NAME': 'basic_example',
    'SEED': 587549,
    'INIT_POP_SIZE': 1024,
    'WORLD_SIZE': '32 32',
    'MIN_GENOME_LENGTH': 1,
    'FUZZY_FLAVOR': 0,
    'SELECTION_SCHEME': 'fitness_proportionate 1000',
    'POINT_MUTATION_RATE': 1e-7,
    'SMALL_INSERTION_RATE': 1e-7,
    'SMALL_DELETION_RATE': 1e-7,
    'MAX_INDEL_SIZE': 6,
    'WITH_ALIGNMENTS': 'false',
    'DUPLICATION_RATE': 1e-6,
    'DELETION_RATE': 1e-6,
    'TRANSLOCATION_RATE': 1e-6,
    'INVERSION_RATE': 1e-6,
    'ENV_SAMPLING': 300,
    'MAX_TRIANGLE_WIDTH': 0.01,
    'BACKUP_STEP': 10000,
    'RECORD_TREE': 'true',
    'MORE_STATS': 'true',
    'ENV_VARIATION': 'none',
    'ENV_AXIS_FEATURES': 'METABOLISM',
    'ALLOW_PLASMIDS': 'false',
    'WITH_TRANSFER': 'false'
}


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
    input_orga_fp = data / Path('best_last_org.txt')
    aevol_create_fp = '%s/src/aevol_ltisee/src/aevol_create' % str(Path.cwd())

    # create scenario folder
    sc_dir = data / Path(args.scenario) / Path('seed0%s' % args.seed)
    sc_dir.mkdir(parents=True, exist_ok=True)

    # modify params
    params['STRAIN_NAME'] = '%s_seed0%s' % (args.scenario, args.seed)
    if args.scenario == 'mut+':
        params['POINT_MUTATION_RATE'] = 1e-6
        params['SMALL_INSERTION_RATE'] = 1e-6
        params['SMALL_DELETION_RATE'] = 1e-6
    elif args.scenario == 'mut-':
        params['POINT_MUTATION_RATE'] = 1e-8
        params['SMALL_INSERTION_RATE'] = 1e-8
        params['SMALL_DELETION_RATE'] = 1e-8
    elif args.scenario == 'sel+':
        params['SELECTION_SCHEME'] = 'fitness_proportionate 4000'
    elif args.scenario == 'sel-':
        params['SELECTION_SCHEME'] = 'fitness_proportionate 250'
    elif args.scenario == 'pop+':
        params['INIT_POP_SIZE'] = '4096'
    elif args.scenario == 'pop-':
        params['INIT_POP_SIZE'] = '256'

    params['SEED'] = params['SEED'] + int(args.seed)

    # create param.in
    param_fp = sc_dir / Path('param_WT.in')
    with open(param_fp, 'w') as param_f:
        for p in params:
            param_f.write('%s %s\n' % (p, params[p]))
        param_f.write('ENV_ADD_GAUSSIAN 1.2 0.52 0.12\n')
        param_f.write('ENV_ADD_GAUSSIAN -1.4 0.5 0.07\n')
        param_f.write('ENV_ADD_GAUSSIAN 0.3 0.8 0.03\n')

    # copy organism file
    best_orga_fp = sc_dir / Path('best_last_org.txt')
    best_orga_fp.write_text(input_orga_fp.read_text())

    # create population
    chdir(sc_dir)
    subprocess.run([
        aevol_create_fp,
        '-C',
        best_orga_fp.name,
        '-f',
        param_fp.name])