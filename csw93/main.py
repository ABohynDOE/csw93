import numpy as np
import pandas as pd
from itertools import chain, repeat


def design_matrix(n_runs: int):
    """
    Generate the design matrix, Table 1 of Chen, Sun and Wu (1993), for a
    specific run size.

    Parameters
    ----------
    n_runs : int
        Number of runs.

    Raises
    ------
    ValueError
        Number of runs must be a power since the design is regular.

    Returns
    -------
    mat : np.array
        Design matrix.

    """
    # Test if nbr of runs is a power of two
    if np.log2(n_runs) % 1 != 0:
        raise ValueError("Number of runs must be a power of 2")

    # Init the matrix
    n_bf = int(np.log2(n_runs))
    mat = np.zeros((n_bf, n_runs - 1))
    cols = list(range(n_runs - 1))

    # Fill the matrix
    for i in cols:
        col_num = i + 1
        # Power of 2 case
        if np.log2(col_num) % 1 == 0:
            k = int(np.log2(col_num))
            mat[k, i] = 1
        # Alternative case
        s = np.binary_repr(col_num, width=n_bf)
        mat[:, i] = list(map(int, s[::-1]))
    return mat


def load_tables():
    """
    Return a dataframe with all designs from the Chen, Sun and Wu (1993) paper.

    Contains the following fields:
        n.runs          Number of runs
        index              ID representing the design, corresponding to the CSW 1993 paper
        n.cols          Number of columns
        n.added         Number of added factors among the columns
        design.rank     Rank of the design in term of the aberration criterion
        cols            Numbers of the added columns
        wlp             Word length pattern, starting at A3 (or A4 for 64-run designs)
        clear.2fi       Number of clear two-factor-interactions


    Returns
    -------
    pd.DataFrame
        Table of all designs.

    """
    # filepath = pkg_resources.resource_stream(__name__, 'data/tables.csv')
    filepath = "data/tables.csv"
    df = pd.read_csv(filepath, header=0, sep=",")
    df["u_id"] = df["n.runs"].astype(str) + "." + df["index"]
    return df.set_index("u_id")


def basic_factor_matrix(n_bf: int):
    """
    Generate a full design matrix that only contains basic factors.

    Parameters
    ----------
    n_bf : int
        Number of basic factors.

    Returns
    -------
    mat : np.array
        Basic factors matrix.

    """
    mat = np.zeros((2 ** n_bf, n_bf))
    for i in range(n_bf):
        a = 2 ** n_bf // (2 ** (i + 1))
        b = 2 ** n_bf // (2 * a)
        col_list = repeat([0] * a + [1] * a, b)
        col = list(chain(*col_list))
        mat[:, i] = col
    return mat


def get_design(n_runs: int, index: str):
    """
    Generate the full design matrix given the number of runs and the specific
    index of the design.

    Parameters
    ----------
    n_runs : int
        Number of runs.
    index : str
        Index of the design. Equivalent to the first column in the tables of
        Chen, Sun and Wu (1993)

    Raises
    ------
    ValueError
        Number of runs must be a power of 2.
        Index must correspond to a design in the paper.

    Returns
    -------
    mat: np.array
        Full design matrix.

    """
    # Test if nbr of runs is a power of two
    log2_runsize = np.log2(n_runs)
    if log2_runsize % 1 != 0:
        raise ValueError("Number of runs must be a power of 2")
    else:
        n_bf = int(log2_runsize)
    # Load the tables
    table = load_tables()
    # Build index
    design_index = str(n_runs) + "." + index
    # Retrieve information
    try:
        design_info = table.loc[design_index]
    except KeyError:
        print(index, "is not a valid design index")
        return None
    # Extract column numbers
    basic_factors = [2 ** i for i in range(n_bf)]
    added_factors = list(map(int, design_info["cols"].split(",")))
    columns = [i - 1 for i in basic_factors + added_factors]
    columns.sort()
    # Build basic factor matrix
    bf_mat = basic_factor_matrix(n_bf)
    # Build design matrix
    design_mat = design_matrix(n_runs)
    specific_design_mat = design_mat[:, columns]
    # Matrix multiplication
    mat = (np.matmul(bf_mat, specific_design_mat) % 2).astype(int)
    return mat


if __name__ == "__main__":
    print(get_design(16, "9-5.1"))
