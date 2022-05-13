from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, ArticleSubjectRelation, Subject


class ArticleRelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):
        main_cnt = 0
        for form in self.forms:
            print(form.cleaned_data)
            main_cnt = main_cnt + form.cleaned_data.get('is_main', False)
            if main_cnt > 1:
                raise ValidationError('Основным может быть только один раздел')
        if not main_cnt:
            raise ValidationError('Укажите основной раздел')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleRelationshipInline(admin.TabularInline):
    model = ArticleSubjectRelation
    formset = ArticleRelationshipInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleRelationshipInline]


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    pass
