from django.db import models


class Currency(models.Model):
    code = models.CharField(max_length=10, primary_key=True)
    value = models.DecimalField(max_digits=30, decimal_places=20, null=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.code


class CryptoCoins(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    last_updated = models.DateTimeField()
    date_added = models.DateTimeField()
    price = models.DecimalField(max_digits=30, decimal_places=20)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


# class Categories(models.Model):
#     id = models.CharField(primary_key=True)
#     name = models.CharField(max_length=255)
#     title = models.CharField(max_length=255, default="")
#     description = models.TextField()
#     num_tokens = models.IntegerField()
#     avg_price_change = models.FloatField()
#     market_cap = models.DecimalField(max_digits=50, decimal_places=20)
#     market_cap_change = models.FloatField()
#     volume = models.DecimalField(max_digits=50, decimal_places=20)
#     volume_change = models.FloatField()
#     last_updated = models.DateTimeField()

#     def __str__(self):
#         return self.name


# class Cryptocurrency(models.Model):
#     id = models.PositiveIntegerField(primary_key=True)
#     name = models.CharField(max_length=255)
#     symbol = models.CharField(max_length=10)
#     slug = models.CharField(max_length=255)
#     cmc_rank = models.PositiveIntegerField()
#     num_market_pairs = models.PositiveIntegerField()
#     circulating_supply = models.BigIntegerField()
#     total_supply = models.BigIntegerField()
#     max_supply = models.BigIntegerField(null=True, blank=True)
#     last_updated = models.DateTimeField()
#     date_added = models.DateTimeField()
#     tags = models.JSONField(default=list)
#     platform = models.CharField(max_length=255, null=True, blank=True)

# # Quote fields
# usd_price = models.DecimalField(max_digits=20, decimal_places=8)
# usd_volume_24h = models.DecimalField(max_digits=20, decimal_places=2)
# usd_percent_change_1h = models.DecimalField(max_digits=10, decimal_places=2)
# usd_percent_change_24h = models.DecimalField(max_digits=10, decimal_places=2)
# usd_percent_change_7d = models.DecimalField(max_digits=10, decimal_places=2)
# usd_market_cap = models.DecimalField(max_digits=20, decimal_places=2)
# usd_last_updated = models.DateTimeField()

# btc_price = models.DecimalField(max_digits=20, decimal_places=8)
# btc_volume_24h = models.DecimalField(max_digits=20, decimal_places=2)
# btc_percent_change_1h = models.DecimalField(max_digits=10, decimal_places=2)
# btc_percent_change_24h = models.DecimalField(max_digits=10, decimal_places=2)
# btc_percent_change_7d = models.DecimalField(max_digits=10, decimal_places=2)
# btc_market_cap = models.DecimalField(max_digits=20, decimal_places=2)
# btc_last_updated = models.DateTimeField()

# def __str__(self):
#     return self.name
