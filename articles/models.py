from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
        ordering = ['name',]

    def __str__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    tags = models.ManyToManyField(to='Tag', through='Scope')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Scope(models.Model):
    tag = models.ForeignKey(to=Tag, on_delete=models.CASCADE)
    article = models.ForeignKey(to=Article, on_delete=models.CASCADE,related_name='scopes')
    is_main = models.BooleanField()
    class Meta:
        ordering = ['-is_main', 'tag'] 
