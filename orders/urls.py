from django.urls import path
from .views import *

app_name ="orders"
urlpatterns = [
    path('', main, name="main"),
    path('<int:id>/new/', new, name="new"),
    path('create/', create, name="create")
]