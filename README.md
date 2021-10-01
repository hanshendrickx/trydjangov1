# trydjangov1

This course I followed develops code that will be followed in detail. The course source is 
This course I followed develops code that will be followed in detail. The course source is available on YouTube at https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL. the site providing this course is https://www.codingforentrepreneurs.com/. They provide a lot of courses for React, Python, HTML and so on at https://www.codingforentrepreneurs.com/projects and https://www.codingforentrepreneurs.com/courses. The author is Justin Mitchel https://www.codingforentrepreneurs.com/u/jmitchel3.  

Happy coding and follow the video's at https://www.youtube.com/playlist?list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL

Video 1: Welcome
Video 2: Demo after xx parts
Video 3: Requirements. Personally I love to maintain my Python Environments through the free individual Anaconda for Data Scientists. I describe that in the wordfile on my Hard Disk under the name Django-Try-V1_Video_Course. A copy will become available on github.
I use Anaconda-Python, Virtual env python 3.6.x, GitHub, GitHub Desktop, GitKraken, Visual Studio Code. You may follow the course as is. It makes use of another way of creating environments.
Video 4: Python Virtual Environment
Video 5: setup on windows

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

Video 6: setup Django Project. I use following codes. I have setup my env in Anaconda Django-Try-V1 and made the connection to the github Repository trydjangov1. In VSCode I open that Folder and create a README (if not done already). In GitKraken I push that code. Alternative is to use GitHub Desktop for that. I like GitKraken because it provides a very unserstandable control of folders, files and branches. 

video 6: Place the correct python in ouw env, i.e. python-6.3.x
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

If all works as expected push the code to github. That way you always may return to this point and start over again from this point.


