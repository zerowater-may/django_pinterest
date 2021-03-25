from django.shortcuts import render
# Create your views here.
from .forms import ProfileCreationForm
from .models import Profile
from django.urls import reverse_lazy
from django.views.generic import CreateView ,UpdateView 
from .decorators import profile_ownership_required
class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'
    
    def form_valid(self, form): # ProfileCreationForm의 data가 2번째 파라미터에 들어 있어요.
        # user id 값이 없기때문에 프로필사진이 누구껀지 알수없어서 하는 작업
        # 유저값을 넣어주는 것 
        temp_profile = form.save(commit=False) # 임시로 저장함.<commit=False> 키워드 인자를 이용해서
        temp_profile.user = self.request.user # self는 view에서 가져온 self임. 또, 웹브라우저에서 입력 받은 값이 우항 좌항이 db에서 가져온값
        temp_profile.save()             
        return super().form_valid(form)
        
@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

