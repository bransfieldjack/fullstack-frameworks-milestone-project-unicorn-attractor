from django import forms
from .models import Bugs, Features


class AddBugsForm(forms.ModelForm):
    class Meta:
        model = Bugs
        fields = ('title', 'reported_by', 'description')
        
        
class AddFeaturesForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = ('title', 'requested_by', 'description')


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = ('user', 'comments')