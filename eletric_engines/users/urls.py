from django.urls import path
from . import views
from .views import Registration, GrupUpdate

urlpatterns = [
    path('registration/', Registration.as_view(), name='registration'),
    path('update/', GrupUpdate.as_view(), name='update'),
]
