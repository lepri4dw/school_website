from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ApplicationForm

def apply(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/thanks/')
    else:
        form = ApplicationForm()

    return render(request, 'application_form.html', {'form': form})

def thanks_view(request):
    return render(request, 'thanks.html')
