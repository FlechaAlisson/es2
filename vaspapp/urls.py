from django.urls import path
from . import views

urlpatterns = [
    # path("", views.home, name="home"),
    path("aluno/<int:pk>/", views.aluno_view, name="aluno_view"),
    path("aluno_novo", views.aluno_create, name="aluno_novo"),
    # path("<category>/", views.blog_category, name="blog_category"),
]