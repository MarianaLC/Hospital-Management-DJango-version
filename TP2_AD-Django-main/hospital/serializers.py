from rest_framework import serializers
from .models import *


class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'


class OutroArtigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outro_Artigo
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UtenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utente
        fields = '__all__'


class FuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Funcionario
        fields = '__all__'


class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = '__all__'


class FarmaceuticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farmaceutico
        fields = '__all__'


class EnfermeiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enfermeiro
        fields = '__all__'


class StockmedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock_med
        fields = '__all__'


class StockartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock_art
        fields = '__all__'
