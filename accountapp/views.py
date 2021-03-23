from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.
from django.utils.decorators import method_decorator
from django.urls import reverse , reverse_lazy
from accountapp.models import HelloWorld
from django.views.generic import CreateView ,DetailView, UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .forms import AccountUpdateForm
from .decorators import account_ownership_required

has_owner_ship = [account_ownership_required , login_required]

@login_required## 로그인했는지 안했는지를 확인해줌 ( 데코레이터  , decorator )
def hello_world(request):  

    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})



class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #클래스에서는 reverse_lazy를 씀 . 함수에서는 reverse
    template_name = 'accountapp/create.html'

@method_decorator(has_owner_ship, 'get') ## 클래스에서 로그인햇는지 확인하는것 
@method_decorator(has_owner_ship, 'post')
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

@method_decorator(has_owner_ship, 'get') ## 클래스에서 로그인햇는지 확인하는것 
@method_decorator(has_owner_ship, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world') #클래스에서는 reverse_lazy를 씀 . 함수에서는 reverse
    template_name = 'accountapp/update.html'

@method_decorator(has_owner_ship, 'get')
@method_decorator(has_owner_ship, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url =reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'