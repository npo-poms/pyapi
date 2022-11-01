__version__ = "7.1.0.dev"

# would this make pyxb work with python 3.10
import collections
if not(hasattr(collections, "MutableSequence")):
    from collections.abc import MutableSequence
    collections.MutableSequence = collections.abc.MutableSequence
