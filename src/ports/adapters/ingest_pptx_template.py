import collections 
import collections.abc
from pptx import Presentation


# Opens the pptx file specified by `path`
# `path` can be either relative or
# absolute filepath and must be a string
# returns a Presentation object
def create_presentation(path):
    return Presentation(path)