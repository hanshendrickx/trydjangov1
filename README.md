# trydjangov1

This course I followed develops code that will be followed in detail. The course source is 
This course I followed develops code that will be followed in detail. The course source is available on YouTube at https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL. the site providing this course is https://www.codingforentrepreneurs.com/. They provide a lot of courses for React, Python, HTML and so on at https://www.codingforentrepreneurs.com/projects and https://www.codingforentrepreneurs.com/courses. The author is Justin Mitchel https://www.codingforentrepreneurs.com/u/jmitchel3.  

Happy coding and follow the video's at https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL

Video 1: Welcome At https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL
Video 2: Demo after xx parts At https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL
Video 3: Requirements. Personally I love to maintain my Python Environments through the free individual Anaconda for Data Scientists. I describe that in the wordfile on my Hard Disk under the name Django-Try-V1_Video_Course. A copy will become available on github.
I use Anaconda-Python, Virtual env python 3.6.x, GitHub, GitHub Desktop, GitKraken, Visual Studio Code. You may follow the course as is. It makes use of another way of creating environments.
Video 4: Python Virtual Environment At https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL
Video 5: setup on windows At https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL

MY WORKFLOW IS PERSONAL: 
Anyway I use the following workflow/code:

In windows search CMD, in terminal type after the rpompt code (opens VSCode). Open the terminal in VSCode and copy/paste this code:
--------------------------------
cd anaconda3\envs\Django-Try-V1\
conda env list
activate Django-Try-V1
dir
code
--------------------------------
Close the windows terminal and use from now on CMD-code to open VSCode. Continue in the VSCode-terminal in the activated env. If I want to change, clone or whatever my environments I open Anaconda navigator.

You may use GitHub Desktop to maintain the GitHub and push the codes you create.

Video 6: At https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL
setup Django Project. I use following codes. I have setup my env in Anaconda Django-Try-V1 and made the connection to the github Repository trydjangov1. In VSCode I open that Folder and create a README (if not done already). In GitKraken I push that code. Alternative is to use GitHub Desktop for that. I like GitKraken because it provides a very unserstandable control of folders, files and branches. 

video 6: Place the correct python in ouw env, i.e. python-6.3.x. At https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL

I use following code in VSCode terminal:
--------------------------------
cls
cd c:\Users\hansh\anaconda3\envs\Django-Try-V1\
activate Django-Try-V1 
conda install python=3.6
--------------------------------
On my computer, this will change python version 3.8 to python 3.6.13

Next step is to install Django Base Code
--------------------------------
cls
pip install "Django>=3.2.5,<3.3"
python -V
django-admin --version
cd trydjangov1
--------------------------------
This installed Django 3.2.7 on my conmputer
You should now be in the github-folder on your computer:
C:\Users\hansh\anaconda3\envs\Django-Try-V1\trydjangov1\

Next step is to create our first Django Project!

--------------------------------
python -m django startproject trydjango  .
pip freeze >requirements.txt
conda list >requirementsconda.txt 
requirements.txt
requirementsconda.txt
dir
python manage.py runserver
--------------------------------
This leads you to: Django version 3.2.7, using settings 'trydjango.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

Open the browser and view the rocket-page of your Django Project. This a the default Django Page and this page proofs that your project is started correctly. Also, you find 2 txt files with the requitements of your project.

Close the browser by CTRL-C (on windows). Ignore te error messages! That will be solved.

If all works as expected push the code to github through GitKraken. That way you always may return to this point and start over again from this point.

video 7: we already did setup our VSCode. At https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL
Always close properly!:
CTRL-C (close browser)
Close the env
--------------------------------
deactivate
--------------------------------
After saving all files, close all screens/programs. The (Django-Try-V1) will disapear at the beginning of c:\Users\...  
Close all software packages: anaconda, vscode, gitkraken, github desktop.

#############################################################
Startup Workflow next day:
Video 8-9: Get started using the project and open the yourtube channel at https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL
1. Open VSCode open Recent: trydjangov1 folder (VSCode opens your last folder!): You should see now the folder trydjangoV1 and subfolder trydjango and a few files including manage.py, the brain of Django. 
Next we start our Django Project, add an APP called articles, create a superuser (your Windows USERS-name, password admin123, and migrate the database block Django automatically provides, and start the server).

Make sure the terminal is opened with CMD!
STEP 1 Activate the env while you are in the correct dir TRYDJANGOV1
--------------------------------
cls
cd C:\Users\hansh\anaconda3\envs\Django-Try-V1\trydjangov1\
activate Django-Try-V1
dir
--------------------------------
You now should find manage.py and the Django project trydjango in the directory! The env is activated with (Django-Try-V1) c:\Users\......

STEP 2 
We add an APP articles, create the db, create a superuser (I) by in terminal run the following code:
--------------------------------
cls
python manage.py startapp articles
python manage.py migrate
python manage.py createsuperuser

myemail@gmail.com
admin123
admin123
Y
python manage.py runserver
 
--------------------------------
Open the browser at http://127.0.0.1:8000/admin, login with your Users-Name and admin123. Now you will see that you are registered in the Users DB! That means all basic Django functionalities work fine, OUT of the BOX! You can add another user or remove that one again. All without a line of code written! In the URL remove the /admin/auth/user/ and view the default landing HTML page of Django again!

By clicking on Django Documentation you enter the offical 1000+ pages of the documentation V 3.2.x! Register for free to be able to connect to the community of millions of programmers etc.

Video 10-11: Create first web page at https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL
Create trydjango/views.py file in VSCode. Place the following code there:
STEP 1: in VSCode add Python for VSCode (install the plugin from the icon with blocks left side)
Step 2: add code
--------------------------------
"""
To render html web pages
"""
from django.http import HttpResponse

HTML_STRING = """
<h1>Hello World</h1>
"""

def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a respons (We pick to return the respons)
    """
    print(1000 * 100 ) #python code

    return HttpResponse(HTML_STRING)
--------------------------------

STEP 3: create the URL routing for the webpage, handle first URL-Routing
In trydjango/urls.py replace line 16 and a few by:

--------------------------------
from django.contrib import admin
from django.urls import path

from .views import home_view

urlpatterns = [
    path('', home_view), # index/home/root
    path('admin/', admin.site.urls),
]
--------------------------------

Run de server: python mange.py runserver
Open http://127.0.0.1:8000/ and view the 'Hello World' message!


Video 12: Enriching Views
Some extra coding in views.py with random and extra python

Video 13: traydjango.views.py Dynamic data from the database, not from views.py file
articles.views.py add models title and content
--------------------------------
from django.shortcuts import render

# Create your views here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
--------------------------------

Video 14: Place articles in settings.py & Migrate the models title and content
STEP 1
--------------------------------
.....#under INSTALLED APPS (remove this line).......
    'django.contrib.staticfiles',
    'articles',
]
--------------------------------

In de django-package code at C:\Users\hansh\anaconda3\envs\Django-Try-V1\Lib\site-packages\django\contrib you will find all installed apps.
STEP 2
Migrate after closing the browser CTRL-C
--------------------------------
python manage.py makemigrations
python manage.py migrate
--------------------------------
This results into:
(Django-Try-V1) C:\Users\hansh\anaconda3\envs\Django-Try-V1\trydjangov1>python manage.py migrate
Operations to perform:
  Apply all migrations: admin, articles, auth, contenttypes, sessions
Running migrations:
  Applying articles.0001_initial... OK

Video 15-16 Writing data to DB into title and content fields  
STEP 1: Add interactive coding to trydjango.views.py 

Use the Python Shell: (CTRL-C first, cls) to work in your env (use manage.py! to enter your django project)
--------------------------------
cls 
python manage.py shell 
from articles.models import Article
obj = Article(title='This is my first title', content='Hello world')  
obj.save()
obj2 = Article.objects.create(title='This is my other title', content='Hello again')
obj.id
obj2.id                                                               
obj3 = Article()
obj3.title = "Another title"
obj3.content = "some more content"
obj.save()
obj3
obj3.save()
obj3
obj3.id
3
a = Article.objects.get(id=1)
a.title
a.content
--------------------------------
Start the browser. That shows in the browser: Hello This is my other title (id: 2)
Hello again!

Change the code in trydjang.views.py:
--------------------------------
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
    random_id = random.randint(1, 4)
    article_obj = Article.objects.get(id=random_id)
    article_obj = Article.objects.get(id=2)
    # Django Templates
    H1_STRING = f"""
    <h1>Hello {article_obj.title} (id: {article_obj.id})</h1>
    """
    P_STRING = f"""
    <p> {article_obj.content}!</p>
    """
    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)
--------------------------------


For detailed codes from video look into following github address: https://github.com/codingforentrepreneurs/Try-Django-3.2/blob/main/references/Writing%20%26%20Reading%20Data%20via%20models.md


Video 17 templates
Create a folder TRYDJANGOV1.templates with 2 files. Add base.html and home-view.html

Replace and paste following parts the trydjango.views.py code:
--------------------------------
    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content 
    }

    # Django Templates
    HTML_STRING = """
    <h1>Hello {title} (id: {id})</h1>
    <p> {content}!</p>
    """.format(**context)

    return HttpResponse(HTML_STRING)
--------------------------------

and paste in templates.home-view.html
--------------------------------
    <h1>Hello {title} (id: {id})</h1>
    <p> {content}!</p>
--------------------------------

Now place/replace trydjango.views.py
--------------------------------
"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
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

    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content 
    }

    # Django Templates
    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = """
    # <h1>Hello {title} (id: {id})</h1>
    # <p> {content}!</p>
    #  """.format(**context)
    return HttpResponse(HTML_STRING)
--------------------------------

    Change in stetting [DIRS]
--------------------------------
            'DIRS': ['templates'],
--------------------------------

Runserver and view:
Hello {article_obj.title} (id: {article_obj.id})
{article_obj.content}!
The replacements are not processed yet! The substitution is not working yet! You need {{ }}, not { } in the templates.home-views.html file:
--------------------------------
<h1>Hello {{ title }} (id: {{ id }})</h1>
<p> {{ content }}!</p>
--------------------------------
Voila: Hello This is my other title (id: 2)
Hello again

Now create the proper html files:
base.html
--------------------------------
<!DOCTYPE html>
<html>
<head>
    <body>
        {% block content %}
        {% endblock content %}
    </body>
</head>
</html>
--------------------------------

home-view.html
--------------------------------
{% extends "base.html" %}

{% block content %}
<h1>Hello {{ title}} (id: {{ id }})</h1>
<p> {{ content }}!</p>
{% endblock content %}  
--------------------------------

Make templates known in settings.py
--------------------------------
...
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
print("BASE_DIR", BASE_DIR)
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / "templates"
        ],
...
--------------------------------

The latest code for trydjango.views.py
--------------------------------
"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
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

    context = {
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content 
    }

    # Django Templates
    HTML_STRING = render_to_string("home-view.html", context=context)
    # HTML_STRING = """
    # <h1>Hello {title} (id: {id})</h1>
    # <p> {content}!</p>
    #  """.format(**context)
    return HttpResponse(HTML_STRING)
    --------------------------------

    NOW you know how the Django Model-View-Template MVT-system works!!!!!!!!!!!!!!!

Video 18 Lists of articles
articles.models.py
--------------------------------
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()
--------------------------------
trydjango.views.py
--------------------------------
"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a respons (We pick to return the respons)
    """
    name = "justin"
    random_id = random.randint(2, 3)
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "object": article_obj,
        "title": article_obj.title,
        "id": article_obj.id,
        "content": article_obj.content 
    }

    # Django Templates
    HTML_STRING = render_to_string("home-view.html",
    context=context)
    # HTML_STRING = """
    # <h1>Hello {title} (id: {id})</h1>
    # <p> {content}!</p>
    #  """.format(**context)
    return HttpResponse(HTML_STRING)
--------------------------------
Templates: base.html
--------------------------------
<!DOCTYPE html>
<html>
<head>
    <body>
        {% block content %}
        {% endblock content %}
    </body>
</head>
</html>
--------------------------------
Templates: Home-view.html
--------------------------------
{% extends "base.html" %}

{% block content %}
<h1>Hello {{ object.title}} (id: {{ id }})!</h1>
<p> {{ content }}!</p>

<ul>
    {% for x in object_list %}
        {% if x.title %}
            <li><a href='/articles/{{ x.id }}/'>{{ x.title }} - 
            {{ x.content }}</a></li>
        {% endif %}
    {% endfor %}        
</ul>

{% endblock content %}
--------------------------------

    Hello This is my other title (id: 2)!

Hello again!

    This is my first title - Hello world
    This is my other title - Hello again
    Another title - some more content
    This is my first title - Hello world

Video 19 URL dynamic routing
How to dynamically route user input of URLs? We have to indicate this at the project-level trydjango.urls.py because the same is used in all apps.

Start trydjango.urls.py
--------------------------------
urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
]
--------------------------------
change trydjango.urls.py to:
--------------------------------
from django.contrib import admin
from django.urls import path, re_path

from .views import home_view

urlpatterns = [
    path('', home_view),
    path('articles/<int:id>/', home_view), # new version, error correctionline 17  with path, +re_path
    path('admin/', admin.site.urls),
]
--------------------------------

In trydjango.views.py, you have to add *args, **kwargs
--------------------------------
    path('', home_view),
    path('articles/<int:id>/', home_view), # new version, error correctionline 17  with path, +re_path
    path('admin/', admin.site.urls),
--------------------------------

The python problem is solved in django by the *args, **kwargs!

This can be compacted by and you can place this code into the articles.views.py for use in all apps! That is as I understand this.

Now final codes:
articles.views.py
--------------------------------
from django.shortcuts import render

from .models import Article #class

# Create your views here.
def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": article_obj,
    }
    return render(request, "articles/details.html",
    context=context)
--------------------------------
trydjango.urls.py
--------------------------------
from django.contrib import admin
from django.urls import path, re_path

from articles import views
from .views import home_view

urlpatterns = [
    path('', home_view),
    path('articles/<int:id>/', views.article_detail_view), # new version, error correctionline 17  with path, +re_path
    path('admin/', admin.site.urls),
]
--------------------------------
Error in browser: Exception Value: articles/details.html
Solution of course: Create templates\articles\details.html
Create details.html
--------------------------------
{% extends "base.html" %}

{% block content %}

<h1>{{ object.title }}</h1>
<p>{{ object.content }}</p>

{% endblock content %}
--------------------------------

The server gives at: http://127.0.0.1:8000/articles/2/ 
Hello World
This is my other title
Hello again

Back to home page http://127.0.0.1:8000/
gives error home_view() missing 1 required positional argument: 'id'

SOLUTION:
place in trydrango.views.py line 9 None in line:
--------------------------------
def home_view(request, id=None, *args, **kwargs): 
--------------------------------

http://127.0.0.1:8000/ is showing the details now!

Lessons learned are:
1. The path URL first: with arbitrary number like <int:id> or <int:year> etc..
2. The view folloes and needs to handle the arguments (..view(request, id=None)
3. Last, render the view in detail.html

Video 20 The admin
https://www.youtube.com/watch?v=Y2oDKZ7tqn4&list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL&index=20&t=2s

identital commands:
python manage.py == python -m django == django-admin

I already created a superuser before (Video 20 presents that only at this time)
Create a sample customer and view the built in functionalities and the standard groups.

Video 21 Register Model in the Admin
https://www.youtube.com/watch?v=d1kU_rXX-pA&list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL&index=21

Go to C:\Users\hansh\anaconda3\envs\Django-Try-V1\trydjangov1\articles\admin.py
--------------------------------
from django.contrib import admin

# Register your models here.
# Create your models here.
from .models import Article

admin.site.register
--------------------------------

If needed close CTRL-C server, open again and view the admin at http://127.0.0.1:8000/admin/
You will view the Articles added!

So far we have all code in place to handle CONTENT:
Create
Maintain
Show

Now create a list to have a more friendly presentation:
--------------------------------
from django.contrib import admin

# Register your models here.
# Create your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
   list_display = ['id', 'title']
   search_fields = ['title', 'content']
   
admin.site.register(Article, ArticleAdmin)
--------------------------------
The 'title' is the place where we can indicate the list of columns.
You have to CTRL-C and restart the server to view the changes!!!!!!!!!!