"""emailkit: author Figma-safe 600px email SVGs from Python.

Modules
  fonts   download Google Fonts, measure text with the real font file
  svg     the Email / Group builder (sections, text, images, paths, buttons)
  shapes  star / check / arrow / chevron path data
"""
from .fonts import FontRegistry, Font
from .svg import Email, Group, WIDTH, MARGIN
from . import shapes
