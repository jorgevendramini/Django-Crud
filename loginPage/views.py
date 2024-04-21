from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages import constants


def login_user(request):
    if request.method == "GET":
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        user = auth.authenticate(request, username=username, password=senha)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Welcome back!")
            return redirect("/todos/todo_list")
        else:
            messages.error(request, "Usuário ou senha incorretos")
            return redirect("/loginPage/login")
    else:
        return render(request, "authenticate/login.html", {})


def register_user(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")
        confirmar_senha = request.POST.get("confirmar_senha")

        users = User.objects.filter(username=username)

        if users.exists():
            messages.add_message(
                request, constants.ERROR, "Já existe um usuário com esse username"
            )
            return redirect("/loginPage/register")

        if senha != confirmar_senha:
            messages.add_message(
                request, constants.ERROR, "A senha e o confirmar senha devem ser iguais"
            )
            return redirect("/loginPage/register")

        if len(senha) < 6:
            messages.add_message(
                request, constants.ERROR, "A senha deve ter mais de 6 dígitos"
            )
            return redirect("/loginPage/register")

        try:
            User.objects.create_user(username=username, email=email, password=senha)
            return redirect("/loginPage/login")
        except:
            print("Erro 4")
            return redirect("/loginPage/register")


def sair(request):
    auth.logout(request)
    return redirect("/loginPage/login")
