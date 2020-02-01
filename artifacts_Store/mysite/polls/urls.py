from django.urls import path
from . import views

app_name='polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:artifact_id>/', views.detail, name='detail'),
    path('contactus/', views.contactus, name='contactus'),
    path('^$', views.index, name='index'),
]

