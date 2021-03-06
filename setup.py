#!/usr/bin/env python
# Licensed under a 3-clause BSD style license - see LICENSE.rst

# NOTE: The configuration for the package, including the name, version, and
# other information are set in the setup.cfg file. Here we mainly set up
# setup_requires and install_requires since these are determined
# programmatically.

import os

import ah_bootstrap  # noqa

from astropy_helpers.distutils_helpers import is_distutils_display_option
from astropy_helpers.setup_helpers import setup

import astropy  # noqa
min_numpy_version = 'numpy>=' + astropy.__minimum_numpy_version__

if is_distutils_display_option():
    # Avoid installing setup_requires dependencies if the user just
    # queries for information
    setup_requires = []
else:
    setup_requires = [min_numpy_version]

    # Make sure we have the packages needed for building astropy, but do not
    # require them when installing from an sdist as the c files are included
    # there.
    if not os.path.exists(os.path.join(os.path.dirname(__file__), 'PKG-INFO')):
        setup_requires.extend(['cython>=0.21', 'jinja2>=2.7'])

install_requires = [min_numpy_version]

setup(setup_requires=setup_requires,
      install_requires=install_requires)
