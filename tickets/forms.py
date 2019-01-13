from django import forms
from .models import Bugs, Features, Comments


class AddBugsForm(forms.ModelForm): # Form used for registration of new bugs. 
    class Meta:
        model = Bugs
        fields = ('title', 'description', 'status')
        
        
class AddFeaturesForm(forms.ModelForm): # Form used for requesting feature addition. 
    class Meta:
        model = Features
        fields = ('title', 'description', 'status')


class AddCommentForm(forms.ModelForm):  # Form used to add comments. 
    class Meta:
        model = Comments
        fields = ('message', )
        
        
        
        