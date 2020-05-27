Test of different hypotheses for reductive genome evolution
===========================================================

**Input question**: What can cause a reductive genome evolution based on the hypotheses found in literature?

**Methodology**: In silico evolution experiments with [aevol (v6)](https://gitlab.inria.fr/aevol/aevol/-/tree/aevol_6) following the methodology explained in [Batut et al, 2015](https://link.springer.com/article/10.1186/1471-2105-14-S15-S11)
- Creation of wild-type populations (10 seeds?)
- Test of the different hypotheses (called scenarios)
    - Change of 1 parameter on the WT populations
    - Evolution with the new parameter
    - Comparison of genome structure with the WT

# Simulations

## Required resources

- 

## Requirements

- [conda](https://conda.io/miniconda.html)
- Dependencies for aevol: build tools (make, etc), compression library (zlib), Bo ost library, X libraries

    For Ubuntu (on a new VM)

    - Run dedicated script

        ```
        $ bash src/prepare_ubuntu.sh
        ```

    - Log out

- Create the conda environment:

    ```
    $ conda env create -f environment.yml
    ```

## Run WT and scenarios

- Prepare aevol

    ```
    $ bash src/prepare_aevol.sh
    ```

- Prepare and launch a WT

    ```
    $ source activate aevol_scenario
    $ python \
        src/launch_simulation.py \
        --simu wt \
        --seed <0...9>
    ```

- Prepare and launch a scenario

    ```
    $ (source activate aevol_scenario)
    $ python \
        src/launch_simulation.py \
        --simu <scenario to launch> \
        --seed <0...9>
    ```

    Possible scenarios:

    Scenario | Type of scenario | Shortcut for script
    --- | --- | ---
    Increase of the population size | Muller's ratchet | `pop+`
    Reduction of population size | Muller's ratchet | `pop-`
    Increase of selection pressure | Muller's ratchet | `sel+`
    Reduction of population pressure | Muller's ratchet | `sel-`
    Stop of the transfer | Muller's ratchet | `transfer-`
    Increase of local mutation rates | Increase of mutation rates | `mut+`
    Decrease of local mutation rates | Increase of mutation rates | `mut-`
    Increase of rearrangement rates | Increase of mutation rates | `rear+`
    Decrease of rearrangement rates | Increase of mutation rates | `rear-`
    Stabilisation of the environment | Environmental changes | `stab-env`
    Change of the environmental target | Environmental changes | `change-env`
    Neutralization of one part of the environmental target | Environmental changes | `neut-env`
    Removal of one part of the environmental target | Environmental changes | `env-`
   
# Analyses of the scenarios
 
- Launch Jupyter notebooks

    ```
    $ (source activate aevol_scenarios)
    $ jupyter notebook
    ```

- Open [http://localhost:8888](http://localhost:8888)