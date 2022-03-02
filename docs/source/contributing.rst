Contributing
============

Code style
----------

Try to follow the `PEP 8`_ style guide.
A useful tool for automated formatting is `black`_.

Submitting code
---------------

If you would like to contribute, please submit a pull request.
See the `Github Hello World`_ example, if you are new to Github.
For major changes, please open an issue first to discuss what you would like to change.
By contributing to the repository you state you own the copyright to those contributions and agree to include your contributions as part of this project under the MIT license.

Testing
-------

If you contribute, please make sure to update the tests aproprietly.
Continuous integration is performed on `Travis-CI`_.
To perform tests run `pytest`_ .
To obtain a `coverage`_  report in html, run

.. code-block:: bash

    $ coverage run -m pytest .
    $ coverage html

Contact
-------
For further information please contact Alexandre Bohyn, alexandre.bohyn at kuleuven.be

License
-------

.. include:: ../../LICENSE

.. _PEP 8: https://www.python.org/dev/peps/pep-0008/
.. _black: https://black.readthedocs.io/en/stable/index.html
.. _Github Hello World: https://guides.github.com/activities/hello-world/
.. _Travis-CI: https://app.travis-ci.com/github/ABohynDOE/csw93
.. _`pytest`: https://docs.pytest.org/en/latest/
.. _coverage: https://coverage.readthedocs.io