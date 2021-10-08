from django.contrib.auth import authenticate, login 
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
    if request.method == "POST": 
        username = request.POST.get("username")
        password = request.POST.get("password")
        # print(username, password) remove these kind of lines in production!!!
        user = authenticate(request, username=username,
        password=password)
        if user is None:
            context = {"error": "You used an invalid username of password."}
            return render(request, "accounts/login.html", context)
        login(request, user)  
        return redirect('/') #add /admin > / home-view redirect to render, redirect
    return render(request, "accounts/login.html", {})


def logout_view(request):
    return render(request, "accounts/logout.html", {})

def register_view(request):
    return render(request, "accounts/register.html", {})
