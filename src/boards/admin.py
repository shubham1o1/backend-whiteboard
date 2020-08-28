from django.contrib import admin
from .models import Boards

class BoardDisp(admin.ModelAdmin):
    list_display = ('idx','title','user','extras','picture')

# Register your models here.
admin.site.register(Boards, BoardDisp)