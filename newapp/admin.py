from django.contrib import admin
from .models import Member

class MemberAdmin(admin.ModelAdmin):
    last_display="nombre", "apellido", "ciudad"

admin.site.register(Member, MemberAdmin)