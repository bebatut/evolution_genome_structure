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
- Create the conda environment:

    ```
    $ conda env create -f environment.yaml
    ```

For Ubuntu (on a new VM)

- Run dedicated script

    ```
    $ bash src/prepare_ubuntu.sh
    ```

- Log out
- Create the conda environment:

    ```
    $ conda env create -f environment.yaml
    ```

## Prepare and launch the WT

- Prepare and launch a WT

    ```
    $ source activate aevol_scenario
    $ python \
        src/launch_simulation.py \
        --simu wt \
        --seed <0...9>
    ```

## Launch the scenarios

- Prepare and launch a scenario

    ```
    $ source activate aevol_scenario
    $ python \
        src/launch_simulation.py \
        --simu <simu_to_launch> \
        --seed <0|1|2|3|4>
    ```
   
# Analyses of the scenarios
 
- Launch the conda environment

    ```
    $ source activate aevol_scenarios
    ```

- Launch Jupyter

    ```
    $ jupyter notebook
    ```

- Open [http://localhost:8888](http://localhost:8888)