from django.shortcuts import render

# Create your views here.
from .models import Project
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView ,DetailView ,ListView
from .decorators import project_ownership_required
from django.utils.decorators import method_decorator
from .forms import ProjectCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.list import MultipleObjectMixin
from articleapp.models import Article
from subscribeapp.models import Subscription
@method_decorator(login_required , 'get')
@method_decorator(login_required , 'post')
class ProjectCreateView(CreateView):
    model = Project
    context_object_name = 'target_project'
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'
    
    # def form_valid(self, form):
    #     temp_project = form.save(commit=False)
    #     temp_project.writer = self.request.user
    #     temp_article.save()
    #     return super().form_valid(form)
    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk})

class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

class ProjectDetailView(DetailView, MultipleObjectMixin):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        project = self.object
        user = self.request.user 

        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user, project=project)

        object_list = Article.objects.filter(project=self.get_object())
        return super(ProjectDetailView, self).get_context_data(object_list=object_list,
                                                                subscription=subscription,
                                                                 **kwargs)


class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 25

