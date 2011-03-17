Documentation
=============

This buildout is meant to be a basis for all future Jarn buildouts.
Anyone, also people not working on Jarn is free to use this buildout.
It is provided as is without any support or warranty.

Before using this buildout you should read through this document and get
to know the practices it encourages.

Tests
-----

You can run tests for all packages at once using::

  bin/test

In order to run coverage tests, use::

  bin/coverage
  bin/report-html

You can view the coverage results in the htmlcov directory via::

  open htmlcov/index.html
