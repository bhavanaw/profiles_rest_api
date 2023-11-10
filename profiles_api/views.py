from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    "Test API View"
    def get(self, request, format=None):
        """Returns. alist of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function(get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the mosth control over your application logic',
            'Is mapped manually to URLS',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})