from . import views as views
from django.urls import path

urlpatterns = [
    path('', views.notifications_view, name='notifications'),
]
