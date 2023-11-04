from django.urls import path
from . import views
urlpatterns = [
    path('',views.showproduct,name='showproduct'),
    path('productdetail/<int:pk>/',views.productdetail,name='productdetail'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('updateproduct/<int:pk>/',views.updateproduct,name='updateproduct'),
    path('deleteproduct/<int:pk>/',views.deleteproduct, name='deleteproduct')
]
