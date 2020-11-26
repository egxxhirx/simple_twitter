# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone #追加

# Create your models here.
class Tag(models.Model):
 tag = models.CharField('タグ名', max_length=50)
 def __str__(self):
   return self.tag
   
class Post(models.Model):
   title = models.CharField('タイトル', max_length=35)
   text = models.TextField('本文',max_length=140)
   image = models.ImageField('画像', upload_to = 'images', blank=True)
   created_at = models.DateTimeField('投稿日', default=timezone.now)

   def __str__(self):
       return self.title
