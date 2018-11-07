from django.contrib import admin
from survey.models import Category, SurveyQuestion


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Category._meta.get_fields()]


class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SurveyQuestion._meta.get_fields()]


admin.site.register(Category, CategoryAdmin)
admin.site.register(SurveyQuestion, SurveyQuestionAdmin)