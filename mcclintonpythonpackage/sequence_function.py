import pandas as pd
import dendropy
"""This function reads the json salamander file. The output of this function is that it creates a newick tree for the salamanders"""

def sequence_function(filepath):
    pd.options.display.max_colwidth = 1000000
    salamanders = pd.read_json(filepath)
    salamanders

    pd.options.display.max_colwidth = 1000000
    newick_tree = salamanders.newick.to_string(index=False)
#View our Tree
    newick_tree