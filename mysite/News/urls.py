from News.models import BookMarks
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('full/<int:id>/', views.full),
    path('login/', views.User_login, name='login'),
    path('register/', views.user_register, name='index'),
    path('book/<int:n_id>/', views.create_bookmark, name="book"),
    path('GetBook/', views.get_bookmark, name="GetBook"),
    path('editor/',views.Editor),
    path('addNews/',views.AddNews),
    path('editNews/<int:id>/',views.EditNews)
]