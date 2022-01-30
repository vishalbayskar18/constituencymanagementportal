from django.contrib import admin

# Register your models here.

from .models import MP, Constituency, Work, Feedback

admin.site.register(MP)

admin.site.register(Constituency)

admin.site.register(Work)

admin.site.register(Feedback)