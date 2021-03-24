from django.forms import ModelForm
from .models import Profile

class ProfileCreationForm(ModelForm):
    ## models 를 forms 로 바꿔주는 것 
    class Meta:
        model = Profile
        fields = ['image','nickname','message']

