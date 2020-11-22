from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('item_list/', views.PostList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)