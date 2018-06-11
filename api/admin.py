from django.contrib import admin
from api.models import *


# Register your models here.
class AdminUserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AdminUser._meta.get_fields()]


class SurveyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Survey._meta.get_fields()]


class SurveyCategoryAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SurveyCategory._meta.get_fields()]


class SurveyQuestionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SurveyQuestion._meta.get_fields()]


class SurveyResponseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SurveyResponse._meta.get_fields()]


class SurveyResponseChoiceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SurveyResponseChoice._meta.get_fields()]


class SurveyRespondentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SurveyRespondent._meta.get_fields()]


class UserActionTypeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserActionType._meta.get_fields()]


class AuditVaultAdmin(admin.ModelAdmin):
    list_display = [field.name for field in AuditVault._meta.get_fields()]


admin.site.register(AdminUser, AdminUserAdmin)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(SurveyCategory, SurveyCategoryAdmin)
admin.site.register(SurveyQuestion, SurveyQuestionAdmin)
admin.site.register(SurveyResponse, SurveyResponseAdmin)
admin.site.register(SurveyResponseChoice, SurveyResponseChoiceAdmin)
admin.site.register(SurveyRespondent, SurveyRespondentAdmin)
admin.site.register(UserActionType, UserActionTypeAdmin)
admin.site.register(AuditVault, AuditVaultAdmin)