from modrag_molecule_functions import *
from modrag_property_functions import *
from modrag_protein_functions import *

# Test predict_node with CHEMBL217
print("=" * 60)
print("TEST: predict_node() - Predict IC50 with CHEMBL217")
print("=" * 60)
try:
    # Test SMILES - using some common drug-like molecules
    smiles_input = ['CC(=O)Oc1ccccc1C(=O)O', 'CN1C=NC2=C1C(=O)N(C(=O)N2C)C', 'CCO']
    chembl_id = 'CHEMBL217'
    
    print("Input SMILES:", smiles_input)
    print("ChEMBL ID:", chembl_id)
    print()
    
    preds, preds_string, preds_images = predict_node(smiles_input, chembl_id)
    
    print("Predicted IC50 values:", preds)
    print("\nPrediction results:")
    print(preds_string[:600] if len(preds_string) > 600 else preds_string)
    print("\n✓ predict_node test passed\n")
except Exception as e:
    print(f"✗ predict_node test failed: {e}\n")
