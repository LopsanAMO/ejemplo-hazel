from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import EstudianteForm

def casita(request):
    template = 'index.html'
    return render(request, template)

class formi(View):
    def get(self, request):
        template = 'formi.html'
        form = EstudianteForm()
        context = {
            'form': form
        }
        return render(request, template, context)

    def post(self, request):
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/proyecto/casi')
        else:
            return redirect('/proyecto/casi')
