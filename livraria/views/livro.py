from rest_framework.viewsets import ModelViewSet
# from rest_framework.permissions import IsAuthenticated
from livraria.models import Livro
from livraria.serializers import LivroSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer
    # permission_classes = [IsAuthenticated]