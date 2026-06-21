from modrag_molecule_functions import *
from modrag_property_functions import *
from modrag_protein_functions import *

# Test 6: substitution_node() - Molecular substitution
print("=" * 60)
print("TEST 6: substitution_node() - Molecular Substitution")
print("=" * 60)
try:
    smiles_input = ['[NH3+]C(O)CCc1ccc(O)cc1']  # Benzene
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

# Test predict_node with CHEMBL217
# print("=" * 60)
# print("TEST: predict_node() - Predict IC50 with CHEMBL217")
# print("=" * 60)
# try:
#     # Test SMILES - using some common drug-like molecules
#     smiles_input = ['CC(=O)Oc1ccccc1C(=O)O', 'CN1C=NC2=C1C(=O)N(C(=O)N2C)C', 'CCO']
#     chembl_id = 'CHEMBL217'
    
#     print("Input SMILES:", smiles_input)
#     print("ChEMBL ID:", chembl_id)
#     print()
    
#     preds, preds_string, preds_images = predict_node(smiles_input, chembl_id)
    
#     print("Predicted IC50 values:", preds)
#     print("\nPrediction results:")
#     print(preds_string[:600] if len(preds_string) > 600 else preds_string)
#     print("\n✓ predict_node test passed\n")
# except Exception as e:
#     print(f"✗ predict_node test failed: {e}\n")
