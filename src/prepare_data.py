#!/usr/bin/env python

import pandas as pd
from pathlib import Path

files_colnames = {
    'stat_fitness_best.out': [
        'Generation',
        'Population size',
        'Fitness',
        'Genome size',
        'Metabolic error',
        'Parents metabolic error',
        'Metabolic fitness',
        'Secretion error',
        'Parents secretion error',
        'Secretion fitness',
        'Amount of compound present in the grid-cell',
        'Int probe',
        'Double probe'],
    'stat_genes_best.out': [
        'Generation',
        'Nb of coding RNAs',
        'Nb of non-coding RNAs',
        'Average size of coding RNAs',
        'Average size of non-coding RNAs',
        'Nb of functional genes',
        'Nb of non functional genes',
        'Average size of functional genes',
        'Average size of non functional genes',
        'None'],
    'stat_bp_best.out': [
        'Generations',
        'Nb of bp not included in any CDS', 
        'Nb of bp not included in any functional CDS', 
        'Nb of bp not included in any non functional CDS', 
        'Nb of bp not included in any RNA', 
        'Nb of bp not included in any coding RNA', 
        'Nb of bp not included in any non coding RNA', 
        'Nb of non essential bp', 
        'Nb of non essential bp including non fonctional genes']}
columns_to_drop = [
    'Population size',
    'Parents metabolic error',
    'Metabolic fitness',
    'Secretion error',
    'Parents secretion error',
    'Secretion fitness',
    'Amount of compound present in the grid-cell',
    'Int probe',
    'Double probe',
    'None']
interesting_stats = [
    'Genome size',
    'Nb of functional genes',
    'Average size of functional genes',
    'Proportion of functional bp',
    'Metabolic error']


def aggregate_best_ind_stats(cond, seed_nb=5, data_dp=Path('../data/')):
    '''Aggregate stats for the different seeds for a condition
    
    :param cond: condition to consider (directory name)
    :param seed_nb: number of seeds
    :data_dp: Path object to the data

    :return:
    '''
    seed_dfs = {}
    data_dfs = {}
    for s in interesting_stats:
        data_dfs[s] = pd.DataFrame()
    # parse the seeds
    for i in range(1, seed_nb + 1):
        seed = 'seed0%s' % i
        # create a df with the content of the 3 stat files
        seed_df = pd.DataFrame()
        for fn, colnames in files_colnames.items():
            fp = data_dp / cond / seed / fn
            if not fp.exists():
                raise ValueError("%s does not exist" % fp)
            df = pd.read_csv(fp, sep=' ', comment='#', header=None, names=colnames, index_col=0)
            seed_df = pd.concat([seed_df, df], axis=1)
        # remove uninteresting columns
        seed_df = seed_df.drop(columns_to_drop, axis=1)
        # add missing stats
        seed_df['Nb of functional bp'] = seed_df['Genome size'] - seed_df['Nb of bp not included in any functional CDS']
        seed_df['Proportion of functional bp'] = seed_df['Nb of functional bp'] / seed_df['Genome size']
        # save df
        seed_dfs[seed] = seed_df
        # extract interesting stats to df
        for d, df in data_dfs.items():
            name = '%s - %s' % (cond, seed)
            data_dfs[d] = pd.concat([data_dfs[d], seed_df[d].rename(name)], axis=1)
    return seed_dfs, data_dfs


def extract_mean_values(df, cond, nb_generations=10000):
    '''Extract mean values for the last generations
    
    :param df: pandas DataFrame
    :param cond: string with control or scenario data to extract
    :param nb_generations: number of generations on which computing
    the mean

    :return: pandas Series
    '''
    s = (df
        .filter(regex=cond)
        .tail(10000)
        .mean()
        .rename(cond)
        .rename(lambda x: x.replace('%s - ' % cond, '')))
    return s


def extract_mean_values_last_gen(df, cond, nb_generations=10000):
    '''Extract mean values for the last generations
    
    :param df: pandas DataFrame with control and cond columns and generation rows
    :param cond: string with control or scenario data to extract
    :param nb_generations: number of generations on which computing
    the mean

    :return: pandas DataFrame with first control column and then condition column
    and the rows being the seeds
    '''
    control_s = extract_mean_values(df, 'control', nb_generations)
    cond_s = extract_mean_values(df, cond, nb_generations)
    return pd.concat([control_s, cond_s], axis=1)

