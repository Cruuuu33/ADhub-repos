#Es un programa que ayuda a hacer un corte de las secuencias. Hasta ahora, el programa actúa sólo sobre archivos fasta. Para poder correrlo debes tener el ID y las posiciones en donde quieres cortar la secuencia. 
#OJO, el ID de cada secuencia en los formatos fasta incluye todas las partes separadas por un "|". Ejemplo: 
#>sp|A9CK16.1|TADA_AGRFC RecName: Full=tRNA-specific adenosine deaminase
#MAERTHFMELALVEARSAGERDEVPIGAVLVLDGRVIARSGNRTRELNDVTAHAEIAVIRMACEALGQER
#LPGADLYVTLEPCTMCAAAISFARIRRLYYGAQDPKGGAVESGVRFFSQPTCHHAPDVYSGLAESESAEI
#LRQFFREKRLDD
#ID = sp|A9CK16.1|TADA_AGRFC
#El programa hace el corte de las secuencias que tu le indicas y las copiará a un nuevo archivo con el nombre: ed_nombredetuarchivo.fasta. El programa te preguntará si quieres seguir editando hasta que 
#contestes no (N). Al contestar que no, el programa te preguntará si quieres copiar los records que no se editaron. Al contestar que sí,el programa copiará los records no editados en el mismo archivo donde 
#están los que sí se editaron. 

import Bio
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

#This function can retreive information of the sequence id (in fasta files) separated by a "|"
#def get_accession(record):
#    parts = record.id.split("|")
#    return parts[2]
#seq_dirct = SeqIO.to_dict(SeqIO.parse("deaminases.fasta", "fasta"), key_function=get_accession)
#seq_identifiers = list(seq_dirct.keys())
#print(f"These are the sequence queries: {seq_identifiers}")

records_list = list(SeqIO.parse("deaminases.fasta", "fasta"))
print(f"Found {len(records_list)} records in this file")

keep_edit = input("Want to edit yor fasta file? (Y for Yes or N for No) ")
ids_list = []

while keep_edit == 'Y' or keep_edit == 'y':
    query_numb = input("Please indicate the sequence id to edit: ")
    seq_start = int(input("Please indicate the position where you want to start the slice of the sequence: "))
    seq_end = int(input("Please indicate the position where you want to end the slice of the sequence: "))
    for seq_record in SeqIO.parse("deaminases.fasta", "fasta"):
        if query_numb == str(seq_record.id):
            ids_list.append(seq_record.id)
            sliced_seq = seq_record.seq[seq_start-1:seq_end]
            new_rec = SeqRecord(Seq(sliced_seq), query_numb)
            with open("ed_deaminases.fasta", "a") as output_handle:
                SeqIO.write(new_rec, output_handle, "fasta")
    keep_edit = input("Want to keep editing your fasta file? (Y for Yes or N for No) ")
else:
    print(f"The records with the following id's have been sliced: {ids_list}")


numb_files = input("Do you want to copy the rest of the files? (Y for Yes or N for No) ")

if numb_files == "Y" or numb_files == "y":
	for seq_record in SeqIO.parse("deaminases.fasta", "fasta"):
		if seq_record.id not in ids_list:
			with open("ed_deaminases.fasta", "a") as output_handle:
				SeqIO.write(seq_record, output_handle, "fasta")
else:
	print("Job is done, exiting...")