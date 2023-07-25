from rest_framework import serializers
from cmcbackend.models import CryptoCoins, Currency


# class CryptoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cryptos
#         fields = ["id", "name", "description"]


# class CategoriesSerializer(serializers.ModelSerializer):
# timestamp = serializers.DateTimeField()
# error_code = serializers.IntegerField()
# error_message = serializers.CharField()
# elapsed = serializers.IntegerField()
# credit_count = serializers.IntegerField()

# class Meta:
#     model = Categories
#     fields = "__all__"


# class CryptocurrencySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Cryptocurrency
#         fields = "__all__"


class CryptoCoinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CryptoCoins
        fields = "__all__"


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"


# class TestSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Coinstest
#         fields = "__all__"
