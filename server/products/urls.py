from django.urls import path

from .views import ProductViewSet

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',  # /api/products
        'post': 'create',  # /api/products
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrieve',  # /api/products<str:pk>
        'put': 'update',  # /api/products<str:pk>
        'delete': 'destroy',  # /api/products<str:pk>
    })),
]
