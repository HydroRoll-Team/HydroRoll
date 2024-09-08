from . import diceast as ast
from . import utils
from .dice import *
from .errors import *
from .expression import *
from .stringifiers import *

# useful top-level functions to get started quickly
_roller = Roller()
roll = _roller.roll
parse = _roller.parse


__version__ = '1.0.2'