import Bio
from Bio import PDB
from Bio.PDB import*

keep_edit = input("Want to edit? (Y for Yes or N for No) ")

while keep_edit == 'Y':
    structure_id = input("Enter the structure id: ")
    structure_filename = input("Enter the structure filename (with the .pdb extension): ")
    parser = PDBParser()
    structure = parser.get_structure(structure_id, structure_filename)
    chain = input("Enter the letter of the chain: ")
    start_res = int(input("Enter the number where the sequence of residues start: "))
    end_res = int(input("Enter the number where the sequence of residues end: "))
    out_str_file = input("Enter the output structure filename (with the .pdb extension): ")

    Bio.PDB.Dice.extract(structure, chain, start_res, end_res, out_str_file)

    print(f" The {out_str_file} structure file is ready!")
    keep_edit = input("Want to keep editing? (Y for Yes or N for No) ")

else:
    print("Quiting program...")
