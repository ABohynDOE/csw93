Usage
=====
The pakage provides three functions to get

- The design matrix,
- The word length pattern,
- The number of clear two-factor interactions,

using only the number of runs and the index of the design.
This index corresponds to the first column in all tables of all tables from the paper.

.. code-block:: python

    import csw93

    # Design matrix of the 16-run design with index 8-4.1
    csw93.get_design(16, "8-4.1")

    # Word length pattern of the 32-run design with index 15-10.2
    csw93.get_wlp(32, "8-4.1")

    # Number of clear two-factor interactions for the 64-run design 11-5.10
    csw93.get_cfi(64, "11-5.10")
