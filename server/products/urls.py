from django.urls import path

from .views import ProductViewSet

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',  # /api/products
        'post': 'create',  # /api/products
    })),
    path('products/<str:id>', ProductViewSet.as_view({
        'get': 'retrieve',  # /api/products<str:id>
        'put': 'update',  # /api/products<str:id>
        'delete': 'destroy',  # /api/products<str:id>
    })),
]
