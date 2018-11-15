import dendropy
import os
"""This type of function is where it cleans up the sequence you are giving it. This sequence also allows for the multiple arguments to go through."""


def sequence_cleanup(sequence_set, out_file, taxon, gene_start, gene_end):
    assert sequence_set[taxon]

    my_taxon_sequence = sequence_set[taxon].symbols_as_string()
    my_taxon_sequence = my_taxon_sequence[gene_start: gene_end]
    ofile = open(out_file, "w")
    ofile.write(">" + taxon + "\n" + my_taxon_sequence + "\n")
    ofile.close()

    assert os.stat(out_file).st_size != 0