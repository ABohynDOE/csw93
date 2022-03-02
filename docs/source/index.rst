.. csw93 documentation master file, created by
   sphinx-quickstart on Fri Feb 11 15:21:35 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to csw93's documentation!
=================================
CSW93 is a Python package that makes availalble the design matrices of all regular
fractional factorial two-level designs from :cite:t:`chen1993catalogue`.
Recently, all designs from the catalog of :cite:t:`xu2009algorithmic` were also added
to the package.

Here under you will find an installation guide, and a brief description of the basic
usage of the package.
In the following sections are presented a detailled documentation, a contributing
guide and a bibliography.

.. toctree::
   :maxdepth: 1
   :caption: Contents:

   documentation
   contributing
   tools
   bibliography

Installation
------------

Use the package manager `pip <https://pip.pypa.io/en/stable/>`_ to install csw93.

.. code-block:: bash

    pip install csw93

Usage
-----
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


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
