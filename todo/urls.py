
from django.urls import path

from todo.views import home, todo_add

urlpatterns = [
    path("", home, name="home"),
    path("add/", todo_add, name="add"),

]