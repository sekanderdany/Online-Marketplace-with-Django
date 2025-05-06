from django.urls import path

from . import views

app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='index'),
]
# Compare this snippet from puddle/puddle/urls.py: