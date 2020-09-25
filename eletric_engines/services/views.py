from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.contrib import messages
from .forms import Record
from.models import Services

# Create your views here.

class Services_index(GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    group_required = [ u'Admin',  u'Users', u'Employees']
    template_name = 'services_index/services_index.html'

class Parts_index (GroupRequiredMixin, LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    group_required = [u'Admin', u'Users', u'Enployees']
    template_name = 'parts_index/parts_index.html'

class Services_record(GroupRequiredMixin, LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = [u'Admin', u'Users', u'Enployees']
    template_name = 'services_record/services_record.html'
    form_class = Record
    success_url = reverse_lazy('services_index')


class Services_update(GroupRequiredMixin, LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = [u'Admin', u'Enployees']
    model = Services
    fields= ['delivery_date']
    template_name = 'services_record/services_record.html'
    success_url = reverse_lazy('services_index')

class Services_delete(GroupRequiredMixin, LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = [u'Admin', u'Enployees']
    model = Services
    template_name = 'services_record/services_record.html'
    success_url = reverse_lazy('services_index')