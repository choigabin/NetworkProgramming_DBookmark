from django.db import models
from django.shortcuts import resolve_url


class Bookmark(models.Model):
    name = models.CharField('Site name', max_length=30)
    url = models.URLField('Site URL')

    def __str__(self):
        return f'{self.name} | {self.url}'

    def get_absolute_url(self): #views.py UpdateView의 success_url = reverse_lazy('bookmark:list')를 주석처리해주면, 수정을 완료하고 detail 화면으로 넘거암
        return resolve_url('bookmark:detail', pk=self.pk)
