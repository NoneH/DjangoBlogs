from django.contrib import admin

from blogs.models import Blog, Comments

# Register your models here.


class BlogsAdmin(admin.ModelAdmin):
    pass


class CommentsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Blog, BlogsAdmin)
admin.site.register(Comments, CommentsAdmin)
