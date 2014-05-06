from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import TerminoForma
from .models import Terminai


def index_view(request):
    return render(request, 'manozodynas/index.html', {})

def terminu_ivedimas_view(request):
    return render(request, 'manozodynas/naujo_termino_ivedimas.html', {'form': TerminoForma()})
    
@csrf_exempt # Nes be sito 403, naudojant POST.
def patikrinti_prideti_termina(request):
    
    if request.method == 'POST':
        form = TerminoForma(request.POST)
        if form.is_valid():
            lt_terminas = form.cleaned_data["lt_term"]
            en_terminas = form.cleaned_data["en_term"]
            
            terminai_ = Terminai(en_term=en_terminas,lt_term=lt_terminas)
            terminai_.save()
            
            return render(request,'manozodynas/terminas_isvestas_sekmingai.html', {})
    
    else:
        form = TerminoForma()
    return render(request, 'manozodynas/naujo_termino_ivedimas.html', {'form': form})  
    
