from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title


class Subject(models.Model):
    name = models.CharField(max_length=30, verbose_name='Тематика')
    articles = models.ManyToManyField(Article, related_name='subjects', through='ArticleSubjectRelation')

    class Meta:
        verbose_name = 'Разделы'
        verbose_name_plural = 'Разделы'

    def __str__(self):
        return self.name


class ArticleSubjectRelation(models.Model):
    tag = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='scopes', verbose_name='Тематика')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes', verbose_name='Статья')
    is_main = models.BooleanField(default=False, verbose_name='Основной')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематика статьи'
        ordering = ['-is_main']
        unique_together = [['article', 'tag']]
