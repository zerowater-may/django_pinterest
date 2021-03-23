

from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

# 클래스안에서 ㅇ로그인 인증 
def account_ownership_required(func):
    def decorated(request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        if not user == request.user:
            return HttpResponseForbidden()
        return func(request, *args , **kwargs)
    return decorated