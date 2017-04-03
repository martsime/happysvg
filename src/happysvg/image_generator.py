
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Draw

def generate_svg(smiles, file_path):
	wrds = smiles.split(" ")
	if len(wrds) == 1:
		mol = Chem.MolFromSmiles(smiles)
	else:
		mol = Chem.MolFromSmiles(wrds[0])
	AllChem.Compute2DCoords(mol)
	Draw.MolToFile(mol, file_path, size=(400, 400), type="svg")
