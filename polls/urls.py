from django.urls import path
from . import views

urlpatterns = [
    path('item_list/', views.PostList.as_view())
]
