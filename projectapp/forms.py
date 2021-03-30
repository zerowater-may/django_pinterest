from django.forms import ModelForm
from .models import Project

class ProjectCreationForm(ModelForm):
    ## models 를 forms 로 바꿔주는 것 
    class Meta:
        model = Project
        fields = ['image','title','description']

