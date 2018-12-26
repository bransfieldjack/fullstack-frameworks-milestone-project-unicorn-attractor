from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .models import Bugs, Features
from django.utils import timezone
from .forms import AddBugsForm, AddFeaturesForm


def tickets(request):   # Render the ticket main page. 
    return render(request, 'tickets.html')
    
    
def bugs(request):  # Render the bugs ticket page. 
    bugs = Bugs.objects.all()
    return render(request, 'bugs.html', {'bugs': bugs})
    
    
def add_bug(request):
    if request.method=="POST":
        form = AddBugsForm(request.POST)  # If POST request received from form, and form is valid, save the form data and redirect back to the detail page with the id of the object. 
        if form.is_valid():
            bug = form.save()
            return redirect(bugs)
    else:
        form = AddBugsForm
    return render(request, 'add_bug.html', {'form': form})
        
    
def edit_bug(request, pk=None):
    bug = get_object_or_404(Bugs, pk=pk) if pk else None    # Instantiate the 'Bugs' object from models, gets the object or returns a 404 error.
    if request.method=="POST":
        form = AddBugsForm(request.POST, instance=bug)  # If POST request received from form, and form is valid, save the form data and redirect back to the detail page with the id of the object. 
        if form.is_valid():
            bug = form.save()
            return redirect(bug_detail, bug.pk)
    else:
        form = AddBugsForm(instance= bug)
    return render(request, 'edit_bug.html', {'form': form})
    
    
def bug_detail(request, pk):
    bugs = get_object_or_404(Bugs, pk=pk)   # Returns the bug based on its ID. 
    bugs.views += 1 # Increments the number of views by 1.
    bugs.save()
    return render(request, 'bug_detail.html', {'bugs': bugs})
    

def features(request):  # Render the features ticket page. 
    features = Features.objects.all()
    return render(request, 'features.html', {'features': features})
    
    
def add_feature(request):
    if request.method=="POST":
        form = AddFeaturesForm(request.POST)  # If POST request received from form, and form is valid, save the form data and redirect back to the detail page with the id of the object. 
        if form.is_valid():
            feature = form.save()
            return redirect(bugs)
    else:
        form = AddFeaturesForm
    return render(request, 'add_feature.html', {'form': form})
    
    
def features_detail(request, pk):
    features = get_object_or_404(Features, pk=pk)   
    features.views += 1 
    features.save()
    return render(request, 'features_detail.html', {'features': features})
    
    
def edit_feature(request, pk=None):
    feature = get_object_or_404(Features, pk=pk) if pk else None    # Instantiate the 'Bugs' object from models, gets the object or returns a 404 error.
    if request.method=="POST":
        form = AddFeaturesForm(request.POST, instance=feature)  # If POST request received from form, and form is valid, save the form data and redirect back to the detail page with the id of the object. 
        if form.is_valid():
            feature = form.save()
            return redirect(features_detail, feature.pk)
    else:
        form = AddFeaturesForm(instance= feature)
    return render(request, 'edit_feature.html', {'form': form})
        
    

    