from django.urls import path
from . import views

urlpatterns = [
    path('/<slug:area>/<int:age>/<slug:gender>', views.item_list, name='item_list')
]
