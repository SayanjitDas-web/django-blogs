from django.urls import path
from .views import get_all_post, get_single_post, create_post, register, add_comment, add_like

urlpatterns = [
    path('posts/', get_all_post, name="get_all_post"),
    path('posts/<int:id>', get_single_post, name="get_single_post"),
    path('posts/<int:id>/comment/', add_comment, name="add_comment"),
    path('posts/<int:id>/like/', add_like, name="add_like"),
    path('create/', create_post, name="create_post"),
    path('register/', register, name="register")
]
