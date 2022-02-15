# csw93 - Chen, Sun and Wu (1993)
[![PyPI](https://img.shields.io/pypi/v/csw93)](https://pypi.org/project/csw93/)
[![Documentation Status](https://readthedocs.org/projects/csw93/badge/?version=latest)](https://csw93.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://app.travis-ci.com/ABohynDOE/csw93.svg?branch=main)](https://app.travis-ci.com/ABohynDOE/csw93)

CSW93 is a Python package that makes availalble the design matrices of all regular fractional factorial two-level designs from the 1993 paper of Chen, Sun and Wu: ["A catalogue of two-level and three-level fractional factorial designs with small runs"][1].

[1]: <https://www.jstor.org/stable/1403599>

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install csw93.

```bash
pip install csw93
```

## Usage

The pakage provides three functions to get

- The design matrix,
- The word length pattern,
- The number of clear two-factor interactions,

using only the number of runs and the index of the design.
This index corresponds to the first column in all tables of all tables from the paper.

```python
import csw93

# Design matrix of the 16-run design with index 8-4.1
csw93.get_design(16, "8-4.1")

# Word length pattern of the 32-run design with index 15-10.2
csw93.get_wlp(32, "8-4.1")

# Number of clear two-factor interactions for the 64-run design 11-5.10
csw93.get_cfi(64, "11-5.10")
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Roadmap

List of the changes that will be implemented later on:

- Write detailled README for readthedocs
- Include designs from Xu (2009) and reformat the filenames of the code files

## Changelog

- 0.3: Integration to readthedocs.io
- 0.2: Correct WLP
- 0.1: initial version
