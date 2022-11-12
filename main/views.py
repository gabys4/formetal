from django.shortcuts import render
from .models import *
from .forms import EtalForm

# Create your views here.

def formetal (request):
    if request.method == 'POST':
        form = EtalForm(request.POST)
        if form.is_valid():
            form.save()
            form = EtalForm()
    else:
        form = EtalForm()

    return render (request, 'form.html', {'form':form})