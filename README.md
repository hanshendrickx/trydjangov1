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
