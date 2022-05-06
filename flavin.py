#from Bio.PDB import *
from Bio.PDB import MMCIFParser
#from Bio.PDB.MMCIFParser import MMCIFParser
# pdb = PDBList()
# pdb.retrieve_pdb_file(" ",pdir=".",file_format=".cif")

parser = MMCIFParser()
structure = parser.get_structure("6s6t","6s6t.cif")
# print(structure.header.keys())
# print(structure.header["deposition_date"])
# print(structure.header["release_date"])
model = structure.get_models()
models = list(model)
# print(models)
#
chain = models[0].get_chains()
chains = list(chain)
# print(chains)
#
residue = chains[0].get_residues()
residues = list(residue)
#print(residues)
mylist = []
for model in structure:
  for chain in model:
    residues = model.get_residues()
    for residue in residues:
     #if residue.resname()== "GLY":
     name = residue.resname
     if name == "FMN":
      mylist.append(residue)

#print(mylist)
p1 = mylist.__getitem__(0)
p2 = mylist.__getitem__(1)
print(p1)
#distance = p1-p2
#print(distance)
   # if name == "TYR":
   #  print(residue)

# atom = residues[0].get_atoms()
# atoms = list(atom)
# print(atoms)