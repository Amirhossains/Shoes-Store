from django.urls import path

from .views import ShoesList, ShoesDetail

urlpatterns = [
    path('list/', ShoesList.as_view(), name='shoesmodel-list'),
    path('list/<int:pk>/', ShoesDetail.as_view(), name='shoesmodel-detail'),

]