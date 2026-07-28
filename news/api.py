from ninja import NinjaAPI
from typing import List
from ninja import Schema
from .models import Article, MarketTicker

api = NinjaAPI()

class ArticleSchema(Schema):
    id: int
    title: str
    slug: str
    summary: str
    created_at: str

class MarketSchema(Schema):
    symbol: str
    price: float
    change_percentage: float

@api.get("/articles", response=List[ArticleSchema])
def list_articles(request):
    return Article.objects.filter(status='published')

@api.get("/markets", response=List[MarketSchema])
def list_markets(request):
    return MarketTicker.objects.all()