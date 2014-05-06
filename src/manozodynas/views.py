from django.shortcuts import render

from .models import Terminai

def index_view(request):
    return render(request, 'manozodynas/index.html', {})

def terminu_ivedimas_view(request):
    return render(request, 'manozodynas/naujo_termino_ivedimas.html', {})
    
def patikrinti_prideti_termina(request):
    
    # Gauna ivestus terminus, patikrina ar ivesta teisingai.
    if request.method == 'GET':
        if 'input' in request.GET and request.GET['input']:
            terminai = request.GET['input']
        else: return render(request, 'manozodynas/naujo_termino_ivedimas.html', {})
    else: return render(request, 'manozodynas/naujo_termino_ivedimas.html', {})
    
    if terminai == '' or len(terminai.split(',')) != 2:
        return render(request, 'manozodynas/naujo_termino_ivedimas.html', {})
    en_terminas,lt_terminas = terminai.split(',')
    if en_terminas == '' or lt_terminas == '':
        return render(request, 'manozodynas/naujo_termino_ivedimas.html', {})

    # Prideda termina
    terminai_ = Terminai(en_term=en_terminas,lt_term=lt_terminas)
    terminai_.save()    
    
    return render(request,
    'manozodynas/terminas_isvestas_sekmingai.html', {})