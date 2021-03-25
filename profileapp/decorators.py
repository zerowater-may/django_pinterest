
from django.http import HttpResponseForbidden
from .models import Profile

# 클래스안에서 ㅇ로그인 인증 
def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user == request.user:
            return HttpResponseForbidden()
        return func(request, *args , **kwargs)
    return decorated