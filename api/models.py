from django.db import models


class Text(models.Model):
    string = models.CharField(max_length=255, verbose_name='Текст')
