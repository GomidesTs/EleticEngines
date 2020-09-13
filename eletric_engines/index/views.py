from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.contrib import messages

# Create your views here.

class Index(TemplateView):
    template_name = 'index/index.html'

class Main(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = 'main/main.html'

class Price_list(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    group_required = u'Admin'
    template_name = 'price_list/price_list.html'
