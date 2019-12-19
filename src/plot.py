#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt


def plot_evolution_over_generation(df, ylabel, colors):
    '''Evolution over generation for control and condition

    - One line per seed
    - One point: sliding window over 10,000 generations

    :param df: pandas df with first control columns and then condition columns
    :param ylabel: string with ylabel
    :param colors: list with the colors for the different lines

    '''
    sw_df = df.rolling(10000).mean()
    plt.figure()
    sw_df.plot(color=colors, legend=False)
    plt.xlabel('Generation')
    plt.ylabel(ylabel)
    plt.show()


def plot_mean_values_barplot(df, ylabel, colors):
    '''Barplot with the mean values for the last n generations
    with 2 bars side-by-side per seed: control, condition

    :param df: pandas df with first control column and then condition column
    and the rows being the seeds
    :param ylabel: string with ylabel
    :param colors: list with the colors for the different lines
    '''
    plt.figure()
    df.plot.bar(color=colors)
    plt.ylabel(ylabel)
    plt.show()


def plot_prop_barplot(df, ylabel, color):
    '''Barplot with the proportion of change between control and condition
    with 1 bar per seed

    :param df: pandas df with first control column and then condition column
    and the rows being the seeds
    :param ylabel: string with ylabel
    :param color: string with the color for the condition
    '''
    prop_s = df.iloc[:,1] / df.iloc[:,0]
    plt.figure()
    prop_s.plot.bar(color=color)
    plt.ylabel(ylabel)
    plt.show()
