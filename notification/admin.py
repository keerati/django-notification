from django.contrib import admin

from notification.models import NoticeType, NoticeSetting, NoticeQueueBatch, NoticeTemplate


class NoticeTypeAdmin(admin.ModelAdmin):
    list_display = ["label", "display", "description", "default"]


class NoticeSettingAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "notice_type", "medium", "send"]

class NoticeTemplateAdmin(admin.ModelAdmin):
    list_display = ["notice_type", "subject"]

admin.site.register(NoticeQueueBatch)
admin.site.register(NoticeType, NoticeTypeAdmin)
admin.site.register(NoticeSetting, NoticeSettingAdmin)
admin.site.register(NoticeTemplate, NoticeTemplateAdmin)
