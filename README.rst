Documentation
=============

This buildout is meant to be a basis for all future Jarn buildouts.
Anyone, also people not working on Jarn is free to use this buildout.
It is provided as is without any support or warranty.

Before using this buildout you should read through this document and get
to know the practices it encourages.

Ideas
-----

This buildout has a `policy` distribution by that name included, which in turn
contains exactly one Python package by the name `policy`.

All customer / site specific code, templates, CSS, translations and
customizations are done inside that one package.

The buildout and the policy distribution are part of the same Git repository and
tagged and deployed together. There's never any releases of the policy
distribution.

All reusable functionality is developed in standalone projects, wired in via
mr.developer for development. For production these will always get releases to
PyPi or dist.jarn.com.

Setup
-----

The production buildout sets up Varnish, haProxy, two Zope instances and ZEO.
Varnish is running on 127.0.0.1:8080 and the Plone site id should be `Plone`.

The development buildout sets up a Zope instance with a direct file storage
also running on port 8080.

Bootstrap
---------

  python2.6 bootstrap.py -d
  bin/buildout -c development.cfg
  bin/instance fg

Tests
-----

You can run tests for the policy package using::

  bin/test

In order to run coverage tests, use::

  bin/coverage
  bin/report-html

You can view the coverage results in the htmlcov directory via::

  open htmlcov/index.html

I18N
----

To update the translation files, do::

  sh src/policy/policy/rebuild.sh
  sh src/policy/policy/sync.sh
