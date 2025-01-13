# Register your models here.
# myapp/admin.py

from django.contrib import admin
from .models import Question, Answer

admin.site.register(Question)
admin.site.register(Answer)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_staff') # הוספנו את 'id'

admin.site.unregister(User) # הסרת הרישום הקיים של User
admin.site.register(User, CustomUserAdmin) # רישום מחדש עם התצוגה המותאמת
