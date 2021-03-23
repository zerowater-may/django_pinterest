from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.
from django.urls import reverse , reverse_lazy
from accountapp.models import HelloWorld
from django.views.generic import CreateView ,DetailView, UpdateView,DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import AccountUpdateForm

def hello_world(request):  
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()
        
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
        # return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})
    else:
        hello_world_list = HelloWorld.objects.all()

        return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #클래스에서는 reverse_lazy를 씀 . 함수에서는 reverse
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world') #클래스에서는 reverse_lazy를 씀 . 함수에서는 reverse
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url =reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'