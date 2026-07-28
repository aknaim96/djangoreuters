from django.contrib import admin
from .models import Category, Article, MarketTicker

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'status', 'is_lead_story', 'created_at')
    list_filter = ('status', 'category', 'is_lead_story', 'created_at')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'

@admin.register(MarketTicker)
class MarketTickerAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'price', 'change_percentage', 'updated_at')