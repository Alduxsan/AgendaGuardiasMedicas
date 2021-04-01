from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout

def ingresar(request):
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('GuardiasDisponibles_app:disponibles')
    else:
        form = AuthenticationForm()

    return render(request,'login.html',{'form':form})

def salir(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login')
