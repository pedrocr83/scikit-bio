r"""
Experimental APIs (:mod:`skbio.experimental`)
=============================================

.. currentmodule:: skbio.experimental

This module provides experimental functionality.

Classes
-------

.. autosummary::
   :toctree: generated/

   TreeNode
   nj

"""

# ----------------------------------------------------------------------------
# Copyright (c) 2013--, scikit-bio development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ----------------------------------------------------------------------------

from __future__ import absolute_import, division, print_function
import warnings

from skbio.util import UnstableAPIWarning
from skbio.experimental.tree import TreeNode, nj

## TODO: This currently gets executed on ``import skbio``. We'd need to fix that,
## and ideally add more detail to this message to mention what was imported.
## Finally, we probably want to warn about the import of every specific
## unstable API that was imported (this warning will print one time only as-is).
warnings.warn("You are importing code that has an unstable API. See our "
              "[API guide](https://github.com/biocore/scikit-bio/wiki) "
              "to learn what this means for you.", UnstableAPIWarning)

__all__ = ['TreeNode', 'nj']
