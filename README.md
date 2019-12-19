Impact of parameter changes on genome structure
===============================================

Purpose: identification of the impact of population, mutation and selection changes on genome structure.
Outcome:
Process:

# Data

Input: clonal population of 1,024 organisms built using the best individual from a population of 1,024 organisms that evolved during 10 million generations

Simulations:
- Evolution during 500,000 generations after one parameter change
- 7 conditions
    - control (control)
    - increase of spontaneous small mutation rates (mut+)
    - decrease of spontaneous small mutation rates (mut-)
    - increase of selection pressure (sel+)
    - decrease of selection pressure (sel-)
    - increase of population size (pop+)
    - decrease of population size (pop-)
- 5 seeds for each conditions

Parameter | control | mut+ | mut- | sel+ | sel- | pop+ | pop-
--- | --- | --- | --- | --- | --- | --- | ---
Population size | 1,024 |  |  |  | 4,096 | 256
Spontaneous small mutation rates | 1e-07 | 4e-07 | 2.5e-08 | | | |
Selection pressure | 1,000 | | | 4,000 | 250 | |

# Usage

## Requirements

- [conda](https://conda.io/miniconda.html)
- Create the conda environment:

    ```
    $ conda env create -f environment.yaml
    ```

## Analysis of the scenarios

- Launch the conda environment

    ```
    $ source activate aevol_scenarios
    ```
 
- Launch Jupyter

    ```
    $ jupyter notebook
    ```

- Open [http://localhost:8888](http://localhost:8888)