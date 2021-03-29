from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from ..Agenda.models import Guardia, Medico

class indexView(LoginRequiredMixin, ListView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    template_name = "disponibles.html"
    model = Guardia
    context_object_name = "guardiasDisponibles"
    #paginate_by = 30

    def get_queryset(self):
        return Guardia.objects.filter(medico__usuario = self.request.user.id)


def asignar(request, slug):
    Guardia.objects.filter(id = slug).update(usuario = request.user)
    userId = request.user
    return redirect('/asignadas/{}'.format(userId))

