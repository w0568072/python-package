from Bio.Blast import NCBIWWW
from Bio import SeqIO
import os
"""this type of function does a blast with the sequence. The output for this function will give a fasfa file, because when inputted it must be in fa format."""


def sequence_blaster(fasta_path, results_path):
  #check that the file is in fasta format
    record = SeqIO.read(fasta_path, format="fasta")
    result_handle = NCBIWWW.qblast("blastn", "nt", record.format("fasta"))
    save_file = open(results_path, "w")
    save_file.write(result_handle.read())
    save_file.close()
  #check results file is not size zero
    assert os.stat(results_path).st_size != 0