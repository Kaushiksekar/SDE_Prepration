from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostsPageView.as_view(), name="posts"),
]
