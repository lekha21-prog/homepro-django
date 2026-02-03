from django.urls import path
from . import views

urlpatterns = [
    path('providers/', views.service_provider_list, name='providers'),
    path('category/<int:category_id>/', views.category_providers, name='category_providers'),
]



