from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import Info
from .models import Person


# Create your views here.
def get_info(request):
    if request.method == 'POST':
        form = Info(request.POST)
        if form.is_valid():
            p1 = Person()
            p1.name = form.cleaned_data['name']
            p1.email = form.cleaned_data['email']
            p1.roll = form.cleaned_data['roll']
            p1.hall = form.cleaned_data['hall']
            p1.contact = form.cleaned_data['contact']
            p1.exp = form.cleaned_data['exp']
            p1.save()
            return HttpResponseRedirect('/form/')
    
    else:
        form = Info()
    template = loader.get_template('getinfo/index.html')
    context = {'form': form}
    return HttpResponse(template.render(context, request))