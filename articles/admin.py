from django.contrib import admin

from .models import Article, Tag, Scope
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

class  ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_main_counter = 0
        for form in self.forms:
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            if form.cleaned_data.get('is_main'):
                is_main_counter += 1
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            if is_main_counter > 1:
                raise ValidationError(f'Нужно выбрать один основной тэг! Сейчас выбрано - {is_main_counter}!')
        return super().clean()  # вызываем базовый код переопределяемого метода
    
class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
     inlines = [ScopeInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass