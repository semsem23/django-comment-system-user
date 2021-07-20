from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm, CommentForm
from .models import User, Post, Comment, Author

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body',  'post', 'created_on',)
    list_filter = ('created_on',)
    search_fields = ('name', 'body',)


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_date'
    ordering       = ('-published_date',)
    list_display = ('title', 'published_date', )

admin.site.register(Comment, CommentAdmin) 
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)