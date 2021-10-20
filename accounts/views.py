from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm 
from django.shortcuts import render, redirect

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj = form.save()
        return redirect('/login') 
    context = {"form":form}     
    return render(request, "accounts/register.html", context)

# Create your views here.
def login_view(request):
    # if request.user.is_autheticated:
    #    return render(request, "accounts/already-logged-in.html", {})
    # that is taken care of in the login.html file! 
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
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request, "accounts/logout.html", {})

