from django.contrib import admin

from .models import Article, Category


def make_published(modeladmin, request, queryset):
    queryset.update(status='p')


def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')


make_published.short_description = 'انتشار مقالات انتخاب شده'
make_draft.short_description = 'پیش نویس مقالات انتخاب شده'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'thumbnail_tag', 'slug', 'jpublish', 'category_to_str', 'status')
    list_filter = ('publish', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', 'publish']
    actions = [make_published, make_draft]

    def category_to_str(self, obj):
        return "،  ".join([category.title for category in obj.category_published()])

    category_to_str.short_description = 'دسته بندی‌ها'


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
