from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Bugs, Features
from django.utils import timezone
from .forms import AddBugsForm, AddFeaturesForm


def tickets(request):   # Render the ticket main page. 
    return render(request, 'tickets.html')
    
    
def bugs(request):  # Render the bugs ticket page. 
    bugs = Bugs.objects.all()
    return render(request, 'bugs.html', {'bugs': bugs})
    
    
def bug_detail(request, pk):
    bugs = get_object_or_404(Bugs, pk=pk)   # Returns the bug based on its ID. 
    bugs.views += 1 # Increments the number of views by 1.
    bugs.save()
    return render(request, 'bug_detail.html', {'bugs': bugs})
    
    
def features(request):  # Render the features ticket page. 
    features = Features.objects.all()
    return render(request, 'features.html', {'features': features})
    
    
def features_detail(request, pk):
    features = get_object_or_404(Features, pk=pk)   
    features.views += 1 
    features.save()
    return render(request, 'features_detail.html', {'features': features})
    
    
def add_bug(request, pk=None):
    bug = get_object_or_404(Bugs, pk=pk) if pk else None
    form = AddBugsForm(request.POST, instance=bug)
    if form.is_valid():
        bugs = form.save()
        return redirect(bugs, bug.pk)
    else:
        form = AddBugsForm(instance= bug)
    return render(request, 'add_bug.html', {'form': form})
        
    
def add_feature(request, pk=None):
    feature = get_object_or_404(Features, pk=pk) if pk else None
    form = AddFeaturesForm(request.POST, instance=feature)
    if form.is_valid():
        feature = form.save()
        return redirect(features, feature.pk)
    else:
        form = AddFeaturesForm(instance=feature)
    return render(request, 'add_feature.html')