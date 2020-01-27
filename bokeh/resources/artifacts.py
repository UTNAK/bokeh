# -----------------------------------------------------------------------------
# Copyright (c) 2012 - 2020, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
# -----------------------------------------------------------------------------
"""
"""

# -----------------------------------------------------------------------------
# Boilerplate
# -----------------------------------------------------------------------------

import logging  # isort:skip
log = logging.getLogger(__name__)

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

# Standard library imports
from typing import List, Optional

# Bokeh imports

# -----------------------------------------------------------------------------
# Globals and constants
# -----------------------------------------------------------------------------

__all__ = (
    "Artifact",
    "bokeh",
    "widgets",
    "tables",
    "gl",
    "api",
)

# -----------------------------------------------------------------------------
# General API
# -----------------------------------------------------------------------------

class Artifact:

    def __init__(self, name: str, *, depends: Optional[List["Artifact"]] = None) -> None:
        pass

# -----------------------------------------------------------------------------
# Dev API
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Private API
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Code
# -----------------------------------------------------------------------------

bokeh = Artifact("bokeh")
widgets = Artifact("bokeh-widgets", depends=[bokeh])
tables = Artifact("bokeh-tables", depends=[widgets])
gl = Artifact("bokeh-gl", depends=[bokeh])
api = Artifact("bokeh-api", depends=[bokeh])
