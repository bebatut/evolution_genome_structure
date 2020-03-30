#!/usr/bin/env python

import argparse
import subprocess
import yaml

from os import chdir
from pathlib import Path

SEED_NB = 11
SIMULATIONS = [
    'wt',
    # muller's ratchet scenarios
    'pop+',
    'pop-',
    'sel+',
    'sel-',
    'transfer-',
    # increase of mutation rate
    'mut+',
    'mut-',
    'rear+',
    'rear-',
    # environmental change
    'stab-env',
    'change-env',
    'neut-env',
    'env-']
WT_GENERATION_NB = 1000000
SCENARION_GENERATION_NB = 500000

def load_params(fp):
    '''
    Load yaml file

    :param fp: path to a yaml file

    :return: content of the yaml file as a dictionary
    '''
    params = {}
    with open(fp, 'r') as stream:
        try:
            params = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return params


def dump_params(params, fp):
    '''
    Write the simulation parameters into a file

    :param params: dictionary with simulation parameters
    :param fp: path to param.in file 
    '''
    with open(fp, 'w') as param_f:
        for p in params:
            if p == 'ENV_ADD_GAUSSIAN':
                for g in params[p]:
                    param_f.write('ENV_ADD_GAUSSIAN %s %s %s\n' % (g.h, g.m, g.s))
            else:
                param_f.write('%s %s\n' % (p, params[p]))


def create_param_fp(params, simu, seed, param_fp):
    '''
    Modify parameter given the simulation and write in param file

    :param params: dictionary with simulation parameters
    :param simu: string with simulation to modify
    :param seed: seed to use
    '''
    # modify params
    params['STRAIN_NAME'] = '%s_seed0%s' % (simu, seed)
    params['SEED'] = params['SEED'] + int(seed)

    # muller's ratchet scenarios
    if simu == 'pop+':
        params['INIT_POP_SIZE'] = '4096'
    elif simu == 'pop-':
        params['INIT_POP_SIZE'] = '256'
    elif simu == 'sel+':
        params['SELECTION_SCHEME'] = 'fitness_proportionate 1250'
    elif simu == 'sel-':
        params['SELECTION_SCHEME'] = 'fitness_proportionate 250'
    elif simu == 'transfer-':
        params['WITH_TRANSFER'] = False
    # increase of mutation rate
    elif simu == 'mut+':
        params['POINT_MUTATION_RATE'] = 5e-5
        params['SMALL_INSERTION_RATE'] = 5e-5
        params['SMALL_DELETION_RATE'] = 5e-5
    elif simu == 'mut-':
        params['POINT_MUTATION_RATE'] = 5e-7
        params['SMALL_INSERTION_RATE'] = 5e-7
        params['SMALL_DELETION_RATE'] = 5e-7
    elif simu == 'rear+':
        params['DUPLICATION_RATE'] = 5e-4
        params['DELETION_RATE'] = 5e-4
        params['TRANSLOCATION_RATE'] = 5e-4
        params['INVERSION_RATE'] = 5e-4
    elif simu == 'rear-':
        params['DUPLICATION_RATE'] = 5e-6
        params['DELETION_RATE'] = 5e-6
        params['TRANSLOCATION_RATE'] = 5e-6
        params['INVERSION_RATE'] = 5e-6
    # environmental change
    elif simu == 'stab-env':
        params['ENV_VARIATION'] = None
    elif simu == 'change-env':
        params['ENV_ADD_GAUSSIAN'] = [
            {'h': 0.5, 's': 0.05, 'm': 0.2},
            {'h': 0.5, 's': 0.05, 'm': 0.4},
            {'h': 0.5, 's': 0.05, 'm': 0.8}]
    elif simu == 'neut-env':
        params['ENV_ADD_GAUSSIAN'] = [] # to do
    elif simu == 'env-':
        params['ENV_ADD_GAUSSIAN'] = [
            {'h': 0.5, 's': 0.05, 'm': 0.2},
            {'h': 0.5, 's': 0.05, 'm': 0.8}] # to do

    dump_params(params, param_fp)


def prepare_simulation(simu, seed, aevol_bin_dp):
    '''
    :param simu: string with simulation to prepare
    :param seed: seed to prepare
    :param aevol_bin_dp: path to aevol bin directory
    '''
    data = Path('data')
    params = load_params(data / Path('params.yml'))
    cwd = Path.cwd()

    # create scenario folder
    sc_dir = data / Path(simu) / Path('seed0%s' % seed)
    sc_dir.mkdir(parents=True, exist_ok=True)
    param_fp = sc_dir / Path('param.in')

    if simu != 'wt':
        wt_dp = data / Path('wt') / Path('seed0%s' % args.seed)
        chdir(wt_dp)
        aevol_propagate_fp = aevol_bin_dp / Path('aevol_propagate')
        subprocess.run([
            aevol_propagate_fp,
            '-t',
            str(WT_GENERATION_NB),
            '-o',
            sc_dir])
        chdir(cwd)

    # modify params and create param.in
    create_param_fp(params, simu, seed, param_fp)

    # prepare simulation
    chdir(sc_dir)
    if simu == 'wt':
        aevol_create_fp = aevol_bin_dp / Path('aevol_create')
        subprocess.run([
            aevol_create_fp,
            '-f',
            param_fp.name])
    else:
        aevol_modify_fp = aevol_bin_dp / Path('aevol_modify')
        subprocess.run([
            aevol_modify_fp,
            '-f',
            param_fp.name])


def launch_simulation(simu, aevol_bin_dp):
    '''
    :param simu: string with simulation to prepare
    :param aevol_bin_dp: path to aevol bin directory
    '''
    if simu == 'wt':
        gen_nb = str(WT_GENERATION_NB)
    else:
        gen_nb = str(SCENARION_GENERATION_NB)

    # launch simulation
    aevol_run_fp = aevol_bin_dp / Path('aevol_run')
    subprocess.run([
        str(aevol_run_fp),
        '-n',
        gen_nb,
        '-p',
        '-1'])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--simu',
        help='simulation to prepare and launch',
        required=True,
        choices=SIMULATIONS)
    parser.add_argument(
        '--seed',
        help='seed to launch',
        required=True,
        choices=[str(i) for i in range(SEED_NB)])
    args = parser.parse_args()

    aevol_bin_dp = Path.cwd() / Path('src/aevol/bin/')
    if not aevol_bin_dp.is_dir():
        raise ValueError('Need to compile aevol first')

    prepare_simulation(args.simu, args.seed, aevol_bin_dp)
    launch_simulation(args.simu, aevol_bin_dp)
