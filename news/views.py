from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Article, Category, MarketTicker

def home(request):
    category_slug = request.GET.get('category')
    search_query = request.GET.get('q')
    
    articles = Article.objects.filter(status='published').order_by('-created_at')
    
    if category_slug:
        articles = articles.filter(category__slug=category_slug)
        
    if search_query:
        articles = articles.filter(
            Q(title__icontains=search_query) | Q(content__icontains=search_query)
        )

    lead_story = articles.filter(is_lead_story=True).first() or articles.first()
    categories = Category.objects.all()
    tickers = MarketTicker.objects.all()
    
    context = {
        "lead_story": lead_story,
        "articles": articles[1:] if lead_story else articles,
        "categories": categories,
        "tickers": tickers,
        "current_category": category_slug,
        "search_query": search_query or "",
    }
    return render(request, "news/home.html", context)

def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug, status='published')
    context = {"article": article}
    return render(request, "news/article_detail.html", context)