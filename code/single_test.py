from modrag_molecule_functions import *
from modrag_property_functions import *

# Test 1: name_node() - Convert SMILES to molecule names
print("=" * 60)
print("TEST 1: name_node() - SMILES to Names")
print("=" * 60)
try:
    smiles_input = ['CCO', 'CCN', 'CCC']
    names, name_string, _ = name_node(smiles_input)
    print("Input SMILES:", smiles_input)
    print("Output Names:", names)
    print(name_string)
    print("✓ name_node test passed\n")
except Exception as e:
    print(f"✗ name_node test failed: {e}\n")