from django.urls import path
from .views import (
    LaptopList, LaptopDetail, LaptopCreate, 
    LaptopUpdate, LaptopDelete
)

urlpatterns = [
    path('', LaptopList.as_view(), name='laptop_list'),
    path('<int:pk>/', LaptopDetail.as_view(), name='laptop_detail'),
    path('create/', LaptopCreate.as_view(), name='laptop_create'),
    path('<int:pk>/update/', LaptopUpdate.as_view(), name='laptop_update'),
    path('<int:pk>/delete/', LaptopDelete.as_view(), name='laptop_delete'),
]