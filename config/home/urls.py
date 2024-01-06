from django.urls import path
from home.views import introduction, todo, detail




urlpatterns = [
    path("", introduction),
    path("todo/", todo),
    path("todo/detail/<int:todo_id>/", detail)
]