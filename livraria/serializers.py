from rest_framework.serializers import ModelSerializer
# from rest_framework.viewsets import ModelViewSet


from livraria.models import Categoria, Editora, Autor
# Livro, 

class CategoriaSerializer(ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"

class EditoraSerializer(ModelSerializer):
    class Meta:
        model = Editora
        fields = "__all__"

# class LivroSerializer(ModelSerializer):
#     class Meta:
#         model = Livro
#         fields = "__all__"
#         depth = 1


# class LivroDetailSerializer(ModelSerializer):
#     class Meta:
#         model = Livro
#         fields = "__all__"
#         depth = 1

# class LivroViewSet(ModelViewSet):
#     queryset = Livro.objects.all()

#     def get_serializer_class(self):
#         if self.action in ["list", "retrieve"]:
#             return LivroDetailSerializer
#         return LivroSerializer
    
class AutorSerializer(ModelSerializer):
    class Meta:
        model = Autor
        fields = "__all__"