from importlib.metadata import version

__version__ = version("npoapi")

# would this make pyxb work with python 3.10
import collections
if not(hasattr(collections, "MutableSequence")):
    from collections.abc import MutableSequence
    collections.MutableSequence = collections.abc.MutableSequence
