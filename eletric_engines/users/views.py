from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User, Group
from django.urls import reverse_lazy
from .forms import Record, UpdateGrup
from django.shortcuts import get_object_or_404

# Create your views here.

class Registration(CreateView):
   
    template_name = 'registration_useres/registration_useres.html'
    form_class = Record
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Users')
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        return url


class GrupUpdate(UpdateView):
    model = User
    fields= ['username', 'email']
    template_name = 'registration_useres/registration_useres.html'
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        grupo = get_object_or_404(Group, name='Users')
        url = super().form_valid(form)
        self.object.groups.remove(grupo)
        self.object.save()

        grupo = get_object_or_404(Group, name='Admin')
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        return url

    def get_object(self):
        return self.request.user
