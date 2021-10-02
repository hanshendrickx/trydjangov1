"""
To render html web pages
"""
import random
from django.http import HttpResponse



def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a respons (We pick to return the respons)
    """
    name = "justin"
    number = random.randint(10, 1233123)

    H1_STRING = f"""
    <h1>Hello {name} - {number}</h1>
    """
    P_STRING = f"""
    <p> {name} - {number}!</p>
    """

    HTML_STRING = H1_STRING + P_STRING

    return HttpResponse(HTML_STRING)