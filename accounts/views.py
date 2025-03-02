from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import User
from .forms import UserUpdateForm, PasswordUpdateForm
from django.contrib.auth import update_session_auth_hash


class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "You are already logged in, Logout first")
            return redirect("index")
        return render(request, "accounts/login.html")

    def post(self, request):
        uname = request.POST.get("username", "")
        passwd = request.POST.get("password", "")
        user = authenticate(username=uname, password=passwd)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in")
            return redirect("index")
        else:
            messages.warning(request, "Username or password is incorrect")
        return render(request, "accounts/login.html")

@method_decorator(login_required, name="dispatch")
class Logout(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Logged out")
        return redirect("accounts:login")

@method_decorator(login_required, name="dispatch")
class Profile(View):
    def get(self, request):
        user_form = UserUpdateForm(instance=request.user)
        password_form = PasswordUpdateForm(user=request.user)
        context = {
            'user_form': user_form,
            'password_form': password_form
        }
        return render(request, 'accounts/profile.html', context)

    def post(self, request):
        if 'update_profile' in request.POST:
            user_form = UserUpdateForm(request.POST, instance=request.user)
            password_form = PasswordUpdateForm(user=request.user)
            if user_form.is_valid():
                user_form.save()
                messages.success(request, 'Your profile has been updated!')
                return redirect('accounts:profile')
        elif 'change_password' in request.POST:
            user_form = UserUpdateForm(instance=request.user)
            password_form = PasswordUpdateForm(user=request.user, data=request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password has been updated!')
                return redirect('accounts:profile')

        context = {
            'user_form': user_form,
            'password_form': password_form
        }
        return render(request, 'accounts/profile.html', context)
    
class Register(View):
    def get(self, request):
        if request.user.is_authenticated:
            messages.info(request, "You are already logged in")
            return redirect("index")
        return render(request, "accounts/register.html")
    
    def post(self, request):
        data = request.POST
        passwd1 = data.get("password1", "")
        passwd2 = data.get("password2","")
        if passwd1 and (passwd1 != passwd2):
            messages.warning(request, "Passwords do not match")
            return redirect("accounts:register")
        
        email, username, firstname = data.get("email"), data.get("username"), data.get("firstname")
        if not (email and username and firstname):
            messages.info(request, "Email, username, and first name required")
            return redirect("accounts:register")
        
        user = User.objects.filter(Q(email=email) | Q(username=username))
        if not user.exists():
            user = User(email=email, username=username, first_name=firstname)
            if lastname := data.get("lastname"):
                user.last_name = lastname
            user.set_password(passwd1)
            user.save()
            messages.success(request, "User created")
            login(request, user)
            messages.success(request, "Logged in")
            return redirect("index")

        messages.info(request, "User already exists")
        return redirect("accounts:register")
