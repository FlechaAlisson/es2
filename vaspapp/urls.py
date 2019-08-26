from django.urls import path
from . import views
from .views import AlunoCreate, AlunoUpdate, AlunoDelete

urlpatterns = [
    # path("", views.home, name="home"),
    # path("aluno/", views.aluno_view, name="aluno-list"),
    # path("aluno/<int:pk>/", views.aluno_view, name="aluno_view"),
    path("aluno/add/", AlunoCreate.as_view(), name="aluno-add"),
    path("aluno/<int:pk>/", AlunoUpdate.as_view(), name="aluno-update"),
    path("aluno/<int:pk>/delete", AlunoDelete.as_view(), name="aluno-delete"),
    # path("<category>/", views.blog_category, name="blog_category"),
]