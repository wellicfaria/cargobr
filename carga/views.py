from django.shortcuts import render
from .models import Carga
from .forms import FormCarga
from django.shortcuts import redirect

# Create your views here.

def cadastrar_carga(request):
	cargas_cadastradas = Carga.objects.all()
	

	if request.method == "POST":
		form = FormCarga(request.POST)
		if form.is_valid():
			carga = form.save(commit=False)
			carga.cadastro()
			return redirect('carga.views.cadastrar_carga')
	else:
		form = FormCarga()



	return render(request, 'carga/cadastrar_carga.html', {'cargas_cadastradas':cargas_cadastradas,'form':form})
