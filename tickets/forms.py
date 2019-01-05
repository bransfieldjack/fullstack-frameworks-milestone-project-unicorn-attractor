from django import forms
from .models import Bugs, Features, Comments


class AddBugsForm(forms.ModelForm):
    class Meta:
        model = Bugs
        fields = ('title', 'description')
        
        
class AddFeaturesForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = ('title', 'description')


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('message', )
        
        
        
        