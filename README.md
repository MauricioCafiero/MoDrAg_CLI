# MoDrAg - The MOdular DRug design AGent

A command-line interface (CLI) tool for drug discovery and molecular design. MoDrAg is an AI-powered agent that leverages multiple specialized tools to analyze molecules, proteins, and support computational drug design workflows.

**A CafChem project!**

![MoDrAg Logo](modrag.png)

## Features

### Molecular Tools
- **Name Node**: Query PubChem to get IUPAC names and synonyms from SMILES strings
- **SMILES Node**: Convert molecule names to SMILES strings
- **Related Node**: Find similar molecules based on SMILES strings
- **Structure Node**: Generate and visualize 3D molecular structures
- **Canonical Node**: Convert SMILES to canonical form

### Property Tools
- **Substitution Node**: Generate novel molecules through strategic substitution and ring growing
- **Lipinski Node**: Calculate drug-like properties (QED, MW, LogP, HBA, HBD, PSA, etc.)
- **Pharmacophore Feature Node**: Analyze and compare pharmacophore features between molecules

### Protein Tools
- **UNIPROT Node**: Search UNIPROT for protein information and IDs
- **List Bioactives Node**: Find bioactive molecules for specific proteins
- **Get Bioactives Node**: Retrieve bioactive molecules from ChEMBL with IC50 values
- **PDB Node**: Query protein sequences and ligands from PDB IDs
- **Find PDB ID Node**: Search for PDB structures matching protein names
- **Target Node**: Find drug targets associated with diseases (Open Targets)
- **Docking Node**: Perform molecular docking using AutoDock Vina
- **Predict Node**: Predict IC50 values for molecules using LightGBM-trained models

## Installation

### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Dependencies
The project requires the following packages:
- `rdkit` - Molecular informatics
- `pubchempy` - PubChem API access
- `pandas` - Data manipulation
- `requests` - HTTP requests
- `chembl-webresource-client` - ChEMBL API access
- `pillow` - Image processing
- `dockstring` - Molecular docking
- `rcsbapi` - RCSB PDB API access

### Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/MoDrAg_CLI.git
cd MoDrAg_CLI
```

2. Create and activate a virtual environment:
```bash
python3 -m venv code/modrag-env
source code/modrag-env/bin/activate
```

3. Install dependencies:
```bash
pip install rdkit pubchempy pandas requests chembl-webresource-client pillow dockstring rcsbapi
```

## Usage

### Running the CLI

```bash
cd code
python modrag.py
```

The CLI will start with a colorful header and prompt you for commands related to drug discovery tasks.

**Features:**
- Color-coded prompts (light blue for input, purple for responses)
- Response text wrapped to 80 characters per line for readability
- Inference time tracking showing how long each response takes (in minutes)
- Debug output control via `--print` flag

For verbose debugging output:
```bash
python modrag.py --print
```

### Running Tests

Basic test suite for molecular and property tools:
```bash
python tool_tests.py
```

Comprehensive test with all protein tools:
```bash
python single_test.py
```

Test the predict node with CHEMBL217:
```bash
python single_test.py  # Includes predict_node test
```

## Project Structure

```
MoDrAg_CLI/
├── code/
│   ├── modrag.py                      # Main CLI application
│   ├── modrag_molecule_functions.py   # Molecular analysis tools
│   ├── modrag_property_functions.py   # Molecular property tools
│   ├── modrag_protein_functions.py    # Protein and docking tools
│   ├── subs_code.py                   # Substitution helper functions
│   ├── tool_tests.py                  # Basic test suite
│   ├── protein_test.py                # Comprehensive test suite for protein functions
│   └── modrag-env/                    # Python virtual environment
├── data/                              # Data files
├── scratch/                           # Temporary files and outputs
└── README.md                          # This file
```

## Tool Examples

### Getting Started with Molecules
```python
from modrag_molecule_functions import *

# Get molecule names from SMILES
names, name_string, _ = name_node(['CCO', 'c1ccccc1'])
print(name_string)

# Get SMILES from names
smiles, smiles_string, _ = smiles_node(['ethanol', 'benzene'])
print(smiles_string)

# Find similar molecules
similar, related_string, images = related_node(['CCO'])
print(related_string)
```

### Analyzing Molecular Properties
```python
from modrag_property_functions import *

# Calculate Lipinski properties
properties, lipinski_string, _ = lipinski_node(['CCO', 'c1ccccc1'])
print(lipinski_string)

# Generate molecular substitutions
new_mols, sub_string, sub_images = substitution_node(['c1ccccc1'])
print(sub_string)
```

### Working with Proteins
```python
from modrag_protein_functions import *

# Search for proteins
ids, protein_string, _ = uniprot_node(['insulin'], human_flag=True)
print(protein_string)

# Find drug targets
targets, target_string, _ = target_node(['cancer'])
print(target_string)

# Dock molecules
scores, docking_string, _ = docking_node(['CCO'], 'ADRB2')
print(docking_string)

# Predict IC50 values
preds, pred_string = predict_node(['CCO', 'c1ccccc1'], 'CHEMBL217')
print(pred_string)
```

## Data Sources

- **PubChem**: Molecular structures, names, and properties
- **UNIPROT**: Protein sequences and annotations
- **ChEMBL**: Bioactive compounds and drug targets
- **RCSB PDB**: 3D protein structures
- **Open Targets**: Disease-target associations

## Performance Notes

- Network requests to external APIs may take time (PubChem, ChEMBL, UNIPROT)
- Molecular docking calculations are computationally intensive and use all available CPU cores
- 3D structure generation uses RDKit's ETKDG algorithm
- Image generation requires Pillow for molecule grid visualization

## Output Files

The tools generate several types of output files:
- `structure_output.png` - 3D molecular structures
- `substitution_output.png` - Novel substituted molecules
- `bioactives_output.png` - Bioactive molecule structures
- `*_uniprot_ids.tsv` - UNIPROT search results
- `*_bioactives.csv` - Bioactive molecule data with IC50 values

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is provided as-is for research and educational purposes.

## References

- RDKit: https://www.rdkit.org/
- ChEMBL: https://www.ebi.ac.uk/chembl/
- Open Targets: https://www.opentargets.org/
- RCSB PDB: https://www.rcsb.org/
- AutoDock Vina: https://vina.scripps.edu/

## Contact

For questions or issues, please contact the CafChem project team.

---

**MoDrAg** - Enabling modular, intelligent drug design workflows through AI and computational chemistry.
