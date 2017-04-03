from django.shortcuts import render
from happysvg.forms import SmilesForm
from django.http import HttpResponse
from .image_generator import generate_svg
import uuid
import os

def index(request):
	if request.method == 'POST':
		form = SmilesForm(request.POST)
		if form.is_valid():
			smiles = form.cleaned_data.get('smiles')
			filename = uuid.uuid4().hex[:4]
			file_path = "images/" + filename + ".svg"
			generate_svg(smiles, file_path)
			if os.path.exists(file_path):
				with open(file_path, 'rb') as fh:
					response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
					response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
					return response


	else:
		form = SmilesForm()

	context = {
		'form': form
	}

	return render(request, 'happysvg/index.html', context)
