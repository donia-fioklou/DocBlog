from unicodedata import name
from django.urls import path
from blog.views import article, index

 
urlpatterns = [
    path('',index,name="blog-index" ),
    path('article-<str:idArticle>/',article,name="blog-article"),
   
    
]
