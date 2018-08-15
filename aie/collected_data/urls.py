from . import views as views
from django.urls import path

urlpatterns = [
    path('', views.get_data_view, name='get_data'),
]
