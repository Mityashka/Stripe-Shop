from django.urls import path
from . import views

app_name = 'shopapp'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('item/<int:pk>/', views.item_detail_view, name='item_details'),
    path('buy/<int:pk>/', views.buy_item, name='buy_item'),
    path('success/', views.success_view, name='success'),
    path('cancel/', views.cancel_view, name='cancel'),
]