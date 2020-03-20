from django.contrib import admin
from .models import Group, GroupMembers, Message, GroupMessage
# Register your models here.

# admin.site.register(User)


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth',)
    fields = ['first_name', 'last_name', ('date_of_birth')]


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'pk',)


@admin.register(GroupMembers)
class GroupMembersAdmin(admin.ModelAdmin):
    list_display = ('group_id',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('from_id', 'to_id',)
    fields = ['from_id', 'to_id']


@admin.register(GroupMessage)
class GroupMessageAdmin(admin.ModelAdmin):
    list_display = ('from_id', 'to_id',)
    fields = ['from_id', 'to_id']
