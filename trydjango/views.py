"""
To render html web pages
"""
import random
from django.http import HttpResponse

from articles.models import Article


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a respons (We pick to return the respons)
    """
    name = "justin"
    random_id = random.randint(2, 3)
    article_obj = Article.objects.get(id=random_id)

    article_obj = Article.objects.get(id=random_id)

    # Django Templates
    H1_STRING = f"""
    <h1>Hello {article_obj.title} (id: {article_obj.id})</h1>
    """
    P_STRING = f"""
    <p> {article_obj.content}!</p>
    """

    HTML_STRING = H1_STRING + P_STRING

    return HttpResponse(HTML_STRING)