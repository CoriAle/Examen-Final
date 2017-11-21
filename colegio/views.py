from django.shortcuts import render, redirect
from .models import Grado, Materia
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import GradoForm

# Create your views here.

def grado_nuevo(request):
    if request.method == 'POST':
        form = GradoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = GradoForm()
    return render(request, 'colegio/grado_form.html', {'form': form})
