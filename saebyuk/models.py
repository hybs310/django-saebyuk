import uuid
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User


#these goes to real server

class Book(models.Model):
    title = models.CharField('책 제목', max_length=100)
    cover = models.TextField('책 커버 url')
    author = models.CharField('책 저자', max_length=10)
    introduce = models.TextField('책 소개글')
    create_date = models.DateTimeField('책 등록 시간', null=True, blank=True)
    available = models.BooleanField('대출 가능 여부', default=True)
    
    thief = models.ForeignKey(User, on_delete=CASCADE, default=1, null=True, blank=True)
    rental_date = models.DateTimeField(null=True, blank=True)
    return_date = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.title
