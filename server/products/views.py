from rest_framework import viewsets


class ProductViewSet(viewsets.ViewSet):
    def list(self, request):  # /api/products [GET]
        pass

    def create(self, request):  # /api/products [POST]
        pass

    def retrieve(self, request, pk = None):  # /api/products/<str:id> [GET]
        pass

    def update(self, request, pk = None):  # /api/products/<str:id> [PUT]
        pass

    def delete(self, request, pk = None):  # /api/products/<str:id> [DELETE]
        pass
