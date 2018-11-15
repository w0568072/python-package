import dendropy
import os
"""This type of function reads in the DnaCharacterMatrix in the package. The input for this function is a file path to get to plethodon.phy.  When you return this function, it should output the sequence set. The only way this will be true is if the file path exists"""

def sequence_reader(filepath):
       # check that the file exists by 
    assert os.path.exists(filepath)
    sequence_set = dendropy.DnaCharacterMatrix.get(
        path=filepath,
        schema="phylip"
)

#check the returned type - should be dendropy character matrix
    assert type(sequence_set) == dendropy.datamodel.charmatrixmodel.DnaCharacterMatrix
    return(sequence_set)
