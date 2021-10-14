from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ArticleForm
from .models import Article

# Create your views here.
def article_search_view(request):
    # print(dir(request))  <<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>
    print(request.GET)
    query_dict = request.GET # this is a dictionary
    query = query_dict.get("q") # <input type='text' name='q' />
    try:
        query = int( query_dict.get("q"))
    except:
        query = None    
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/search.html", context=context)

@login_required
# in settings.py ad after ROOT_URLCONF = , LOGIN_URL='/login/'
def article_create_view(request):
    # print(request.POST)
    form = ArticleForm()
    print(dir(form))
    context = {
        "form": form
    } #this needs here to keep viewing the post's text PLUS lines context[..] below in this block
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        print(title, content)
        article_object = Article.objects.create(title=title, 
        content=content)
        context['object'] = article_object # this allows condition of If not created then..
        context['created'] = True      
    return render(request, "articles/create.html",
    context=context) 

def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/details.html",
    context=context)