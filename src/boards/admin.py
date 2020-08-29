from django.contrib import admin
from .models import Boards, Picture

class BoardDisp(admin.ModelAdmin):
    list_display = ('idx','title','user','extras','picture')

# Register your models here.
admin.site.register(Boards, BoardDisp)

admin.site.register(Picture)