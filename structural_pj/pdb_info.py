import os
import pandas as pd
import Bio
from Bio import PDB
from Bio.PDB import*
from Bio.PDB.MMCIF2Dict import MMCIF2Dict

PDB_structures_direct = r"C:\PruebasProgramas\CIF_Mac_files"
PDB_file_list = os.listdir(PDB_structures_direct)
print(f"Files that will be processed: {PDB_file_list}")
print(f"Total number of files: {len(PDB_file_list)}")

pdb_csv_info = pd.DataFrame(columns = ["PDB ID", "Title", "Enzyme Function", "Method", "Resolution (A)", "Num Residues", "Reference", "Deposit date", "Organism", "Expression Sys"])
for i in PDB_file_list:
	try:
	    mmcif_dict = MMCIF2Dict(PDB_structures_direct + "\\" + i)
	    PDB_ID = mmcif_dict["_entry.id"]
	    Title = mmcif_dict["_struct.title"]
	    Enzyme_function = mmcif_dict["_struct.pdbx_descriptor"]
	    Method = mmcif_dict["_exptl.method"]
	    Resolution = mmcif_dict["_reflns.d_resolution_high"]
	    Num_residues = mmcif_dict["_entity_src_gen.pdbx_end_seq_num"]
	    Reference = mmcif_dict["_citation.pdbx_database_id_DOI"]
	    Deposit_date = mmcif_dict["_pdbx_database_status.recvd_initial_deposition_date"]
	    Organism = mmcif_dict["_entity_src_gen.pdbx_gene_src_scientific_name"]
	    Expression_sys = mmcif_dict["_entity_src_gen.pdbx_host_org_scientific_name"]
	    row_list = [PDB_ID, Title, Enzyme_function, Method, Resolution, Num_residues, Reference, Deposit_date, Organism, Expression_sys]
	    pdb_csv_info.loc[len(pdb_csv_info)] = row_list
	except KeyError:
		pass

pdb_csv_info['PDB ID'] = pdb_csv_info['PDB ID'].str.get(0)
pdb_csv_info['Title'] = pdb_csv_info['Title'].str.get(0)
pdb_csv_info['Enzyme Function'] = pdb_csv_info['Enzyme Function'].str.get(0)
pdb_csv_info['Method'] = pdb_csv_info['Method'].str.get(0)
pdb_csv_info['Resolution (A)'] = pdb_csv_info['Resolution (A)'].str.get(0)
pdb_csv_info['Num Residues'] = pdb_csv_info['Num Residues'].str.get(0)
pdb_csv_info['Reference'] = pdb_csv_info['Reference'].str.get(0)
pdb_csv_info['Deposit date'] = pdb_csv_info['Deposit date'].str.get(0)
pdb_csv_info['Organism'] = pdb_csv_info['Organism'].str.get(0)
pdb_csv_info['Expression Sys'] = pdb_csv_info['Expression Sys'].str.get(0)

pdb_csv_info.to_csv("pdb_info.csv", index = False)
print("The csv with the information is ready. Check the folder where this program is running")