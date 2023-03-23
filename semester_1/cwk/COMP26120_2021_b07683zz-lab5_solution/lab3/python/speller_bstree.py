import speller
import sys
import config

config.set_type = config.SetType.BSTREE
config.prog_name = "speller_bstree.py"

speller.spelling(sys.argv)
