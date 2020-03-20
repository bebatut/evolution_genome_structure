Impact of parameter changes on genome structure
===============================================

Purpose: identification of the impact of population, mutation and selection changes on genome structure.
Outcome:
Process:

# Data

**Input**: clonal population of 1,024 organisms built using the best individual from a population of 1,024 organisms that evolved during 10 million generations

**Scenarios**:
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
Population size | 1,024 | 1,024 | 1,024 | 1,024 | 4,096 | 256
Spontaneous mutation rates | 1e-07 | 1e-06 | 1e-08 | 1e-07 | 1e-07 | 1e-07 | 1e-07
Selection pressure | 1,000 | 1,000 | 1,000 | 4,000 | 250 | 1,000 | 1,000

# Usage

## Requirements

- [conda](https://conda.io/miniconda.html)
- Create the conda environment:

    ```
    $ conda env create -f environment.yaml
    ```



## Launch the scenarios

- Get access to [aevol ltisee](https://gitlab.inria.fr/beslon/aevol_ltisee/)
- Prepare aevol executable

    ```
    $ ./src/prepare_aevol.sh
    ```

- Prepare a scenario

    ```
    $ source activate aevol_scenarios
    $ python \
        src/prepare_scenario.py \
        --scenario <'control'|'mut+'|'mut-'|'sel+'|'sel-'|'pop+'|'pop-'> \
        --seed <0|1|2|3|4>
    ```

- Launch a scenario

    ```
    $ python \
        src/launch_scenario.py \
        --scenario <'control'|'mut+'|'mut-'|'sel+'|'sel-'|'pop+'|'pop-'> \
        --seed <0|1|2|3|4> \
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