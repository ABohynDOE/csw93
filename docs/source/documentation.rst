Documentation
=============
The CSW93 package contains three main functions.

Design Matrix
-------------
The :func:`main.get_design` function can be used to retrieve the design matrix from an
index.
The index must correspond to one in the table of :cite:t:`chen1993catalogue` or
:cite:t:`xu2009algorithmic`.
For both papers, the index is composed of three numbers representing:

* the number of factors in the design (:math:`n`)
* the number of added factors (:math:`p`, where :math:`n > p`)
* the rank, in term of abberation, of the design


Word length pattern
-------------------
