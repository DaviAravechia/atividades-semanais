from rest_framework import serializers
from models import produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = produto
        fields = '__all__'


        # fields = ['nome','categoria','preco','quantidade_em_estoque','data_criacao']