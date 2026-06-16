import pandas as pd
import requests

def uniprot_node(protein_names: list[str], human_flag: bool = False) -> (list[str], str):
  '''
    This tool takes in the user requested protein and searches UNIPROT for matches.
    It returns a string scontaining the protein ID, gene name, organism, and protein name.
      Args:
        query_protein: the name of the protein to search for.

      Returns:
        total_ids: a list of UNIPROT IDs for the given protein names.
        protein_string: a string containing the protein ID, gene name, organism, and protein name.

  '''
  print("UNIPROT tool")
  print('===================================================')

  total_ids = []
  protein_string = ''

  for protein_name in protein_names:
    try:
      url = f'https://rest.uniprot.org/uniprotkb/search?query={protein_name}&format=tsv'
      response = requests.get(url).text

      f = open(f"../scratch/{protein_name}_uniprot_ids.tsv", "w")
      f.write(response)
      f.close()

      prot_df_raw = pd.read_csv(f'../scratch/{protein_name}_uniprot_ids.tsv', sep='\t')
      if human_flag:
        prot_df = prot_df_raw[prot_df_raw['Organism'] == "Homo sapiens (Human)"]
        print(f"Found {len(prot_df)} Human proteins out of {len(prot_df_raw)} total proteins")
      else:
        prot_df = prot_df_raw

      prot_ids = prot_df['Entry'].tolist()
      genes = prot_df['Gene Names'].tolist()
      organisms = prot_df['Organism'].tolist()
      names = prot_df['Protein names'].tolist()

      sub_ids = []
      for id, gene, organism, name in zip(prot_ids, genes, organisms, names):
        protein_string += f'Protein {protein_name}, ID: {id}, Gene: {gene}, Organism: {organism}, Name: {name}\n'
        sub_ids.append(id)

      protein_string += '==========================================================================================\n'
      total_ids.append(sub_ids)
    except:
      protein_string += f'No proteins found for {protein_name}'
      protein_string += '==========================================================================================\n'
      total_ids.append([])

  return total_ids, protein_string, None