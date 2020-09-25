from django.urls import path
from django.contrib.auth import views as auth_views
from .views import Services_index, Parts_index
from .views import Services_record
from .views import Services_update
from .views import Services_delete

urlpatterns = [
    path('services_index/', Services_index.as_view(), name='services_index'),
    path('services_record/', Services_record.as_view(), name='services_record'),
    path('services_update/<int:pk>', Services_update.as_view(), name='services_update'),
    path('services_delete/<int:pk>', Services_delete.as_view(), name='services_delete'),
    path('parts_index/',Parts_index.as_view(),name='parts_index'),
]