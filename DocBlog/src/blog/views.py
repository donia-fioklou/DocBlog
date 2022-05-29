from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"temBlog/index.html")

def article(request,idArticle):
    if idArticle in ["01","02","03"]:
        return render(request,f"temBlog/article_{idArticle}.html")
    return render(request,"temBlog/articleNotFound.html")
