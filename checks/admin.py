from django.contrib import admin

# Register your models here.
from .models import Whitelist, Blacklist

class WhitelistAdmin(admin.ModelAdmin):
    list_display = ['id', 'md5', 'sha256', 'cert_sha1']  # 미리보기 기능
    search_fields = ['md5', 'sha256', 'cert_sha1']       # search 기능

class BlacklistAdmin(admin.ModelAdmin):
    list_display = ['id', 'md5', 'sha256', 'cert_sha1']  # 미리보기 기능
    search_fields = ['md5', 'sha256', 'cert_sha1']       # search 기능

admin.site.register(Whitelist, WhitelistAdmin)
admin.site.register(Blacklist, BlacklistAdmin)

