from django import forms
from rdkit import Chem

class SmilesForm(forms.Form):
	smiles = forms.CharField(max_length=1000, label='SMILES')

	def clean(self):
		cleaned_data = super(SmilesForm, self).clean()
		smiles = cleaned_data.get('smiles')


		mol = Chem.MolFromSmiles(smiles)
		if not mol:
			self.add_error('smiles', 'Invalid SMILES')
			return

