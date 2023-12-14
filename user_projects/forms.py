from django.forms import ModelForm
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'description', 'source_link', 'demo_link']
        widgets ={
            'tag' : forms.CheckboxSelectMultiple(),
        }
        
    def __init__(self, *args, **kwargs):
        super(ProjectForm , self).__init__(*args ,**kwargs)
            
            
        # Way # 1 
        for name , field in self.fields.items():
            field.widget.attrs.update({'class':'input'})    
        '''
        # Way # 2    
        self.fields['title'].widget.attrs.update(
                {'class':'input' , 'placeholder':'Add Title'}
            )
            
        self.fields['description'].widget.attrs.update(
                {'class':'input' , 'placeholder':'Add Description'}
            )
            
        self.fields['source_link'].widget.attrs.update(
                {'class':'input' , 'placeholder':'Add Source Link'}
            )
            
        self.fields['demo_link'].widget.attrs.update(
                {'class':'input' , 'placeholder':'Add Demo Link'}
            )
            '''