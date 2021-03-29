from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

#def ingresar(request):
    #if request.method == 'POST':
     #   form = AuthenticationForm(data = request.POST)
      #  if form.is_valid():
       #     user = form.get_user()
        #    login(request, user)
         #   return redirect('GuardiasDisponibles_app:disponibles')
   # else:
    #    form = AuthenticationForm()

    #return render(request,'login.html',{'form':form})

#def salir(request):
 #   if request.method == 'POST':
  #      logout(request)
   #     return redirect('/login')



class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

