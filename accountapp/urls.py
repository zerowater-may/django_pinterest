from django.urls import path
from django.contrib.auth.views import LoginView  , LogoutView
from accountapp.views import hello_world , AccountCreateView , AccountDetailView

app_name = "accountapp"


urlpatterns = [
    path('hello_world/',hello_world,name='hello_world'),
    path('login/',LoginView.as_view(template_name='accountapp/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),

    path('create/',AccountCreateView.as_view(),name='create'), # 클래스뷰는 .as_view() 를써야함 
    path('detail/<int:pk>',AccountDetailView.as_view(),name='detail'), # 클래스뷰는 .as_view() 를써야함 

]