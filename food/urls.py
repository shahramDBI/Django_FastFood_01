from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    path('', views.index, name='index'),
    path('item/', views.item, name='item'),
    # /food/1
    path('<int:item_id>/', views.detail, name='detail'),
    # Add Item
    path('add/', views.create_item, name='create_item'),
    # edit
    path('update/<int:id>/', views.update_item, name='update_item'),
    # delete
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
]

