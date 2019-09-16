from django.contrib import admin

# Register your models here.
from .models import Article, Comment, Tag

class CommentInline(admin.TabularInline):
  model = Comment
  extra = 3

class TagsInline(admin.TabularInline):
  model = Article.tags.through
  extra = 1

class ArticleAdmin(admin.ModelAdmin):
  inlines = [CommentInline]
  ordering = ['posted_at']
  search_fields = ['title']
  inlines = [TagsInline,]
  exclude = ('tags',)

class ArticleInline(admin.TabularInline):
  model = Article.tags.through

class TagAdmin(admin.ModelAdmin):
  inlines = [ArticleInline]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag, TagAdmin)