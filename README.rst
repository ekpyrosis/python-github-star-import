========
Overview
========

Import and merge any Github account's stars.

Version: v0.2.2.

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|

.. |docs| image:: https://readthedocs.org/projects/python-github-star-import/badge/?style=flat
    :target: https://readthedocs.org/projects/python-github-star-import
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/ekpyrosis/python-github-star-import.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ekpyrosis/python-github-star-import

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ekpyrosis/python-github-star-import?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ekpyrosis/python-github-star-import

.. |requires| image:: https://requires.io/github/ekpyrosis/python-github-star-import/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ekpyrosis/python-github-star-import/requirements/?branch=master

.. |codecov| image:: https://codecov.io/github/ekpyrosis/python-github-star-import/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ekpyrosis/python-github-star-import

.. |version| image:: https://img.shields.io/pypi/v/github-star-import.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/github-star-import

.. |wheel| image:: https://img.shields.io/pypi/wheel/github-star-import.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/github-star-import

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/github-star-import.svg
    :alt: Supported versions
    :target: https://pypi.org/project/github-star-import

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/github-star-import.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/github-star-import


.. end-badges

* Free software: BSD 2-Clause License

Installation
============

::

    pip install github-star-import

Usage
============

::

    github-star-import github_username github_access_token import_account_username

    github-star-import ekp 85ab5c9c26a6b1592d0d97f9b61afc34b6230521 github

Documentation
=============

https://python-github-star-import.readthedocs.io/en/latest/

Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
