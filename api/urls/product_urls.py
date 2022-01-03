from django.urls import path
from rest_framework import views
from api.views import product_views

urlpatterns = [
    path('', product_views.getProducts, name='products'),
    path('create/', product_views.createProduct, name='create_product'),
    path('upload/', product_views.uploadImage, name='upload_image'),
    path('item/<str:pk>/', product_views.getProductDetails, name='product_details'),
    path('toprated/', product_views.getTopRatedProducts, name='top_rated'),
    path('update/<str:pk>',product_views.updateProduct, name="update_product"),
    path('delete/<str:pk>',product_views.deleteProduct, name="delete_product"),
]