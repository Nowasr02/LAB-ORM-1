from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.home_view, name="home_view"),
    path("create/", views.create_post_view, name="create_post_view"),
    path("details/<int:post_id>/", views.post_details_view, name="post_details_view"),
    path("update/<int:post_id>/", views.update_post_view, name="update_post_view"),
    path("delete/<int:post_id>/", views.delete_post_view, name="delete_post_view"),
    
]