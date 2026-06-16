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

# Test 2: smiles_node() - Convert molecule names to SMILES
print("=" * 60)
print("TEST 2: smiles_node() - Names to SMILES")
print("=" * 60)
try:
    names_input = ['ethanol', 'ammonia']
    smiles_list, smiles_string, _ = smiles_node(names_input)
    print("Input Names:", names_input)
    print("Output SMILES:", smiles_list)
    print(smiles_string)
    print("✓ smiles_node test passed\n")
except Exception as e:
    print(f"✗ smiles_node test failed: {e}\n")

# Test 3: related_node() - Find similar molecules
print("=" * 60)
print("TEST 3: related_node() - Find Similar Molecules")
print("=" * 60)
try:
    smiles_input = ['CCO']
    similar_list, related_string, images = related_node(smiles_input)
    print("Input SMILES:", smiles_input)
    print("Number of similar molecules found:", len(similar_list[0]) if similar_list[0] else 0)
    print(related_string[:500], "...")  # Print first 500 chars
    print("✓ related_node test passed\n")
except Exception as e:
    print(f"✗ related_node test failed: {e}\n")

# Test 4: structure_node() - Generate 3D structures
print("=" * 60)
print("TEST 4: structure_node() - Generate 3D Structures")
print("=" * 60)
try:
    smiles_input = ['CCO', 'CC']
    structures, output_string, images = structure_node(smiles_input)
    print("Input SMILES:", smiles_input)
    print("Number of structures generated:", len(structures))
    print(output_string)
    if images and images[0]:
        images[0].save("../outputs/structure_output.png")
        print("Saved structure image as 'structure_output.png'")
    print("✓ structure_node test passed\n")
except Exception as e:
    print(f"✗ structure_node test failed: {e}\n")

# Test 5: canonical_node() - Convert to canonical SMILES
print("=" * 60)
print("TEST 5: canonical_node() - Canonical SMILES")
print("=" * 60)
try:
    smiles_input = 'C1=CC=CC=C1CCO' 
    canonical_smiles = canonical_node(smiles_input)
    print("Input SMILES:", smiles_input)
    print("Canonical SMILES:", canonical_smiles)
    print("✓ canonical_node test passed\n")
except Exception as e:
    print(f"✗ canonical_node test failed: {e}\n")

# Test 6: substitution_node() - Molecular substitution
print("=" * 60)
print("TEST 6: substitution_node() - Molecular Substitution")
print("=" * 60)
try:
    smiles_input = ['c1ccc(O)cc1']  # Benzene
    sub_smiles_list, sub_string, sub_images = substitution_node(smiles_input)
    print("Input SMILES:", smiles_input)
    print("Number of novel molecules generated:", len(sub_smiles_list[0]) if sub_smiles_list[0] else 0)
    print(sub_string[:500], "...")  # Print first 500 chars
    if sub_images and sub_images[0]:
        sub_images[0].save("../outputs/substitution_output.png")
        print("Saved substitution image as 'substitution_output.png'")
    print("✓ substitution_node test passed\n")
except Exception as e:
    print(f"✗ substitution_node test failed: {e}\n")

# Test 7: lipinski_node() - Lipinski properties
print("=" * 60)
print("TEST 7: lipinski_node() - Lipinski Properties")
print("=" * 60)
try:
    smiles_input = ['CCO', 'c1ccccc1']  # Ethanol, Benzene
    lipinski_list, lipinski_string, _ = lipinski_node(smiles_input)
    print("Input SMILES:", smiles_input)
    print("Number of molecules analyzed:", len(lipinski_list))
    print(lipinski_string)
    print("✓ lipinski_node test passed\n")
except Exception as e:
    print(f"✗ lipinski_node test failed: {e}\n")

# Test 8: pharmfeature_node() - Pharmacophore features
print("=" * 60)
print("TEST 8: pharmfeature_node() - Pharmacophore Features")
print("=" * 60)
try:
    test_smiles = ['CC(OC(=O)c1c[nH]c2ccccc12)C1CCCCN1C']  # Benzene as reference
    known_smiles = 'CN1CCOc2c(C(=O)NC3CC4CCC(C3)N4C)cc(Cl)cc21'  # test molecules
    feat_scores, feat_string, _ = pharmfeature_node(known_smiles, test_smiles)
    print("Reference SMILES:", known_smiles)
    print("Test SMILES:", test_smiles)
    print("Feature overlap scores:", feat_scores)
    print(feat_string[:800], "...")  # Print first 500 chars
    print("✓ pharmfeature_node test passed\n")
except Exception as e:
    print(f"✗ pharmfeature_node test failed: {e}\n")