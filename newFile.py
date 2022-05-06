#breakpoint()
import pdb
from Bio.PDB import *
pdb = PDBList()
pdb.retrieve_pdb_file("2FAT",pdir=".",file_format="pdb")
parser = PDBParser(PERMISSIVE=True, QUIET=True)
data = parser.get_structure("2FAT","pdb2FAT.ent")
# print(data.header.keys())
# print(data.header["deposition_date"])
# print(data.header["release_date"])
model = data.get_models()
models = list(model)
print(models)

chain = models[0].get_chains()
chains = list(chain)
print(chains)

residue = chains[0].get_residues()
residues = list(residue)
print(residues)

atom = residues[0].get_atoms()
atoms = list(atom)
print(atoms)