from modrag_molecule_functions import *
from modrag_property_functions import *
from modrag_protein_functions import *

# Test: uniprot_node() - Search UNIPROT for proteins
print("=" * 60)
print("TEST: uniprot_node() - UNIPROT Protein Search")
print("=" * 60)
try:
    protein_names = ['insulin', 'hemoglobin']
    protein_ids, protein_string, _ = uniprot_node(protein_names, human_flag=True)
    print("Input Protein Names:", protein_names)
    print("Number of results per query:", [len(ids) for ids in protein_ids])
    print(protein_string[:800], "...")  # Print first 800 chars
    print("✓ uniprot_node test passed\n")
except Exception as e:
    print(f"✗ uniprot_node test failed: {e}\n")
