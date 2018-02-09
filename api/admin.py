from django.contrib import admin

from .models import Text


class TextAdmin(admin.ModelAdmin):
    list_display = ('string', )


admin.site.register(Text, TextAdmin)
