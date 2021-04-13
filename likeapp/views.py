from django.shortcuts import get_object_or_404, render

# Create your views here.

from django.views.generic import RedirectView
from django.urls import reverse
from django.utils.decorators import method_decorator
from articleapp.models import Article
from likeapp.models import LikeRecord
from django.http import HttpResponseRedirect
from random import randint
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db import transaction
# from django.contrib.messages import message

@transaction.atomic
def db_transaction(user, article):

    article.like += randint(1,200)
    article.save()

    if LikeRecord.objects.filter(user=user,article=article).exists():
        raise ValidationError('Like already exists')
    else:
        LikeRecord(user=user,article=article).save()


    
@method_decorator(login_required,'get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail' , kwargs={'pk':kwargs['pk']})
    
    def get(self, *args, **kwargs):
        user = self.request.user
        article = get_object_or_404(Article, pk=kwargs['pk'])

        try:
            db_transaction(user,article)
            messages.add_message(self.request, messages.SUCCESS, '좋아요를 눌렀습니다!!')
        except ValidationError:
            messages.add_message(self.request, messages.ERROR, '좋아요는 한번만 하세여!! ^^ ')
            return HttpResponseRedirect(reverse('articleapp:detail' , kwargs={'pk':kwargs['pk']}))

        return super(LikeArticleView, self).get(self.request , *args, **kwargs)