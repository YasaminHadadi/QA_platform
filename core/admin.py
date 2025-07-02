from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Question, Answer, CustomUser

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(CustomUser, UserAdmin)