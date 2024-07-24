from django.contrib import admin
from .models import User, App, Group

admin.site.register(User)
admin.site.register(App)
admin.site.register(Group)

# Register your models here.
