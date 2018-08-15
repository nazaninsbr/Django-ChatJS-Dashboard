from . import views as views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('api/all/data/', views.get_all_time_data, name='api_get_data'),
    path('api/week/data/', views.get_week_data, name='api_get_week_data'),
]
