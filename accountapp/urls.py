from django.urls import path
from accountapp.views import hello_world

app_name = 'accountapp'


urlpatterns = [
    path('hello_newworld/', hello_world, name="hello_world")
]